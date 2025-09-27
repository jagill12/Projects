# Hidden Markov Model (HMM)

This project implements a discrete Hidden Markov Model with the **Viterbi**, **Forward**, **Backward**, **Forward–Backward (posterior decoding)**, and **Baum–Welch (EM training)** algorithms. It demonstrates probabilistic sequence modeling and inference on symbolic observations (e.g., DNA bases).

## Overview
A Hidden Markov Model describes a system with **hidden states** that emit **observable symbols** according to state-specific distributions, while transitioning between states via a Markov process. This implementation supports:
- **Most likely state path** with Viterbi (MAP decoding)
- **Sequence likelihood** with Forward/Backward
- **Per-position state posteriors** with Forward–Backward
- **Parameter learning** from data with Baum–Welch (EM)

The algorithm works as follows:

### Initialization
- Define the state set, observation alphabet, **initial probabilities** π, **transition matrix** A, and **emission matrix** B.
- Provide an observation sequence (e.g., `"GGCACTGAA"`).

### Viterbi (Most Likely Path)
- Dynamic programming in log-space computes, for each time step, the best score for ending in each state plus a traceback pointer.
- Backtrack from the best final state to recover the **single most likely** hidden-state sequence.

### Forward / Backward (Likelihood)
- **Forward** recursively accumulates probabilities of partial prefixes; **Backward** accumulates suffixes.
- The total likelihood of the observation sequence is obtained from the final forward column (or initial backward column).

### Forward–Backward (Posterior Decoding)
- Element-wise product of Forward and Backward probabilities yields **unnormalized posteriors** over states at each position.
- Column-wise normalization gives **P(state_t | observations)** for every position, enabling **uncertainty-aware** decoding.

### Baum–Welch (EM Training)
- Using Forward/Backward, compute **γ** (state posteriors) and **ξ** (expected transitions) for each sequence.
- **M-step:** Re-estimate π, A, B from expected counts; iterate until parameter changes fall below a tolerance or max iterations reached.
- Result: data-driven parameters that improve fit without known state labels.

This end-to-end implementation mirrors how HMMs are used in genomics (e.g., CpG island detection, chromatin states), speech, and NLP—combining **decoding**, **likelihood computation**, and **unsupervised training** in one toolkit.
