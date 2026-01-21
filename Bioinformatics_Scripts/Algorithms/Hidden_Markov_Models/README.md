# Hidden Markov Model (HMM)
This project implements a discrete Hidden Markov Model (HMM) for sequence analysis. It includes core inference and learning algorithms—Viterbi, Forward, Backward, Forward–Backward (posterior decoding), and Baum–Welch—showing how hidden state processes can be inferred from observable symbol sequences such as DNA bases.

## Overview
A Hidden Markov Model represents a system where the true state sequence is unobserved, but leaves probabilistic traces through emitted symbols. Each hidden state produces observations according to its own emission distribution, while transitions between states follow a Markov process.

This implementation focuses on the full HMM workflow: evaluating how likely a sequence is under a model, inferring the most probable hidden state path, quantifying uncertainty at each position, and learning model parameters directly from data.

The algorithm works as follows:

### Initialization
The model is defined by a set of hidden states, an observation alphabet, initial state probabilities (π), a transition matrix (A), and an emission matrix (B). Given an observation sequence (for example, "GGCACTGAA"), the HMM provides a probabilistic framework for reasoning about the unseen state sequence that generated it.

### Viterbi Decoding 
The Viterbi algorithm computes the single most likely sequence of hidden states that could have produced the observations. Using dynamic programming in log space, it tracks the best-scoring path to each state at every time step, along with traceback pointers. Backtracking from the highest-scoring final state yields the maximum a posteriori (MAP) state path.

### Forward and Backward Algorithms
The Forward algorithm recursively accumulates the probability of observing prefixes of the sequence, while the Backward algorithm works from the end to accumulate suffix probabilities. Together, they provide the total likelihood of the observation sequence under the model and form the backbone of more advanced inference.

### Forward–Backward (Posterior Decoding)
By combining Forward and Backward probabilities, the model computes posterior probabilities over states at each position in the sequence. Rather than committing to a single path, this reveals uncertainty and ambiguity, yielding 
𝑃(state(t)|oberservations) for every position.

### Baum–Welch (EM Training)
The Baum–Welch algorithm uses an Expectation–Maximization (EM) procedure to learn model parameters when state labels are unknown. Expected state occupancies and transitions are computed from Forward–Backward probabilities, then used to re-estimate π, A, and B. Iterating this process improves model fit until convergence.

### Applications
This implementation reflects how HMMs are used in practice across domains such as genomics (e.g., CpG island detection, chromatin state annotation), speech recognition, and natural language processing. It brings together decoding, likelihood estimation, uncertainty quantification, and unsupervised learning in a single cohesive framework.


