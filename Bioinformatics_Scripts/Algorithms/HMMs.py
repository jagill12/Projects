import numpy as np
import pandas as pd

class HiddenMarkovModel:
    def __init__(self, states, observations, init_probs, trans_probs, emit_probs):
        self.states = states
        self.obs = observations
        self.init_probs = init_probs
        self.trans_probs = trans_probs
        self.emit_probs = emit_probs
        self.state_index = {state: i for i, state in enumerate(self.states)}
        self.index_state = {i: state for state, i in self.state_index.items()}

    def viterbi(self, obs_sequence):
        n_states = len(self.states)
        n_obs = len(obs_sequence)
        viterbi_matrix = np.zeros((n_states, n_obs))
        traceback = np.zeros((n_states, n_obs), dtype=int)

        for state in self.states:
            i = self.state_index[state]
            viterbi_matrix[i, 0] = np.log(self.init_probs[state]) + np.log(self.emit_probs[state][obs_sequence[0]])
            traceback[i, 0] = 0

        for t in range(1, n_obs):
            for curr_state in self.states:
                j = self.state_index[curr_state]
                max_prob, max_state = max(
                    (
                        viterbi_matrix[i, t-1] +
                        np.log(self.trans_probs[prev_state][curr_state]) +
                        np.log(self.emit_probs[curr_state][obs_sequence[t]]),
                        i
                    )
                    for prev_state, i in self.state_index.items()
                )
                viterbi_matrix[j, t] = max_prob
                traceback[j, t] = max_state

        best_last_state = np.argmax(viterbi_matrix[:, -1])
        best_prob = float(np.exp(viterbi_matrix[best_last_state, -1]))

        best_path = [0] * n_obs
        best_path[-1] = best_last_state
        for t in range(n_obs - 2, -1, -1):
            best_path[t] = traceback[best_path[t + 1], t + 1]

        best_states = [self.index_state[i] for i in best_path]
        return best_states, best_prob

    def forward_algorithm(self, obs_sequence):
        n_states = len(self.states)
        n_obs = len(obs_sequence)
        fwd = np.zeros((n_states, n_obs))

        for i, state in enumerate(self.states):
            fwd[i, 0] = self.init_probs[state] * self.emit_probs[state][obs_sequence[0]]

        for t in range(1, n_obs):
            for j, curr_state in enumerate(self.states):
                fwd[j, t] = sum(
                    fwd[i, t-1] * self.trans_probs[self.states[i]][curr_state]
                    for i in range(n_states)
                ) * self.emit_probs[curr_state][obs_sequence[t]]

        return fwd

    def backward_algorithm(self, obs_sequence):
        n_states = len(self.states)
        n_obs = len(obs_sequence)
        bwd = np.zeros((n_states, n_obs))

        for i in range(n_states):
            bwd[i, n_obs - 1] = 1

        for t in range(n_obs - 2, -1, -1):
            for j, curr_state in enumerate(self.states):
                bwd[j, t] = sum(
                    bwd[i, t+1] *
                    self.trans_probs[curr_state][self.states[i]] *
                    self.emit_probs[self.states[i]][obs_sequence[t+1]]
                    for i in range(n_states)
                )
        return bwd

    def forward_backward(self, obs_sequence):
        fwd = self.forward_algorithm(obs_sequence)
        bwd = self.backward_algorithm(obs_sequence)
        n_states = len(self.states)
        n_obs = len(obs_sequence)
        posterior = np.zeros((n_states, n_obs))

        for t in range(n_obs):
            for j in range(n_states):
                posterior[j, t] = fwd[j, t] * bwd[j, t]
        posterior /= posterior.sum(axis=0)
        return posterior

#Tol stands for tolerance, aka convergence threshold
    def baum_welch(self, observations_list, n_iter=100, tol=1e-4):
        n_states = len(self.states)

        for _ in range(n_iter):
            total_init = np.zeros(n_states)
            total_trans = {s: {s2: 0.0 for s2 in self.states} for s in self.states}
            total_emit = {s: {o: 0.0 for o in self.obs} for s in self.states}
            total_gamma = {s: 0.0 for s in self.states}
            prev_init = self.init_probs.copy()
            prev_trans = {s: self.trans_probs[s].copy() for s in self.states}
            prev_emit = {s: self.emit_probs[s].copy() for s in self.states}

            for obs_sequence in observations_list:
                fwd = self.forward_algorithm(obs_sequence)
                bwd = self.backward_algorithm(obs_sequence)
                prob_obs = np.sum(fwd[:, -1])

                gamma = (fwd * bwd) / prob_obs
                xi = np.zeros((n_states, n_states, len(obs_sequence) - 1))

                for t in range(len(obs_sequence) - 1):
                    denom = 0.0
                    for i in range(n_states):
                        for j in range(n_states):
                            denom += (
                                fwd[i, t] *
                                self.trans_probs[self.states[i]][self.states[j]] *
                                self.emit_probs[self.states[j]][obs_sequence[t+1]] *
                                bwd[j, t+1]
                            )
                    for i in range(n_states):
                        for j in range(n_states):
                            xi[i, j, t] = (
                                fwd[i, t] *
                                self.trans_probs[self.states[i]][self.states[j]] *
                                self.emit_probs[self.states[j]][obs_sequence[t+1]] *
                                bwd[j, t+1]
                            ) / denom

                for i in range(n_states):
                    state_i = self.states[i]
                    total_init[i] += gamma[i, 0]

                    for j in range(n_states):
                        state_j = self.states[j]
                        total_trans[state_i][state_j] += np.sum(xi[i, j, :])

                    total_gamma[state_i] += np.sum(gamma[i, :])

                    for k in self.obs:
                        total_emit[state_i][k] += sum(
                            gamma[i, t] for t in range(len(obs_sequence)) if obs_sequence[t] == k
                        )

            self.init_probs = {s: total_init[i] / len(observations_list) for i, s in enumerate(self.states)}

            for i in range(n_states):
                state_i = self.states[i]
                total = sum(total_trans[state_i].values())
                if total == 0:
                    for state_j in self.states:
                        self.trans_probs[state_i][state_j] = 1.0 / n_states
                else:
                    for j in range(n_states):
                        state_j = self.states[j]
                        self.trans_probs[state_i][state_j] = total_trans[state_i][state_j] / total

            for state in self.states:
                if total_gamma[state] == 0:
                    for obs in self.obs:
                        self.emit_probs[state][obs] = 1.0 / len(self.obs)
                else:
                    for obs in self.obs:
                        self.emit_probs[state][obs] = total_emit[state][obs] / total_gamma[state]

            delta_init = max(abs(self.init_probs[s] - prev_init[s]) for s in self.states)
            delta_trans = max(
                abs(self.trans_probs[s1][s2] - prev_trans[s1][s2])
                for s1 in self.states for s2 in self.states
            )
            delta_emit = max(
                abs(self.emit_probs[s][o] - prev_emit[s][o])
                for s in self.states for o in self.obs
            )

            if delta_init < tol and delta_trans < tol and delta_emit < tol:
                break

        return self.init_probs, self.trans_probs, self.emit_probs
    
# ------------------- MAIN SECTION -------------------

#Observation sequence
obs_sequence = "GGCACTGAA"

#States and observations
states = ["I", "R"]
observations = ["A", "C", "G", "T"]

#Initial, transition, and emission probabilities
init_probs = {
    "I": 0.2,
    "R": 0.8
}

trans_probs = {
    "I": {"I": 0.7, "R": 0.3},
    "R": {"I": 0.1, "R": 0.9}
}

emit_probs = {
    "I": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
    "R": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3}
}

#Create model
model = HiddenMarkovModel(states, observations, init_probs, trans_probs, emit_probs)

# ---- Run Viterbi BEFORE training ----
viterbi_path, viterbi_prob = model.viterbi(obs_sequence)
print("Most Likely Viterbi Path (Before Training):", viterbi_path)
print("Probability of Viterbi Path:", viterbi_prob)

# ---- Run Forward-Backward ----
state_probs = model.forward_backward(obs_sequence)
df_probs = pd.DataFrame({
    'Observation': [f'Obs {i+1}' for i in range(state_probs.shape[1])],
    'I': state_probs[0],
    'R': state_probs[1]
}).set_index('Observation')

print("\nForward-Backward State Probabilities:")
print(df_probs)

# ---- Run Baum-Welch Training ----
model.baum_welch(obs_sequence, n_iter=10)

print("\n--- After Baum-Welch Training ---")
print("Updated Initial Probabilities:", model.init_probs)
print("Updated Transition Probabilities:", model.trans_probs)
print("Updated Emission Probabilities:", model.emit_probs)

# ---- Run Viterbi AGAIN AFTER training ----
viterbi_path_trained, viterbi_prob_trained = model.viterbi(obs_sequence)
print("\nMost Likely Viterbi Path (After Training):", viterbi_path_trained)
print("Probability of Viterbi Path:", viterbi_prob_trained)
