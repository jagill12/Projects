# Gibbs Motif Finder

This project implements a Gibbs sampling algorithm to discover conserved sequence motifs in genomic data. It identifies shared short patterns (motifs) — such as promoter elements — across a set of biological sequences by iteratively refining predictions based on probabilistic modeling.

## Overview

Gibbs sampling is a Markov Chain Monte Carlo (MCMC) method that estimates the most likely motif positions by repeatedly sampling possible motif locations and updating probabilities based on observed data. This implementation is designed to find motifs like Shine-Dalgarno sequences in bacterial promoters.

The algorithm works as follows:

1. **Initialization:**  
   Each input sequence is assigned a random starting position for a motif of length *k*.

2. **Iterative Sampling:**  
   - One sequence is randomly removed from consideration.  
   - A **Position Frequency Matrix (PFM)** and corresponding **Position Weight Matrix (PWM)** are built from the remaining sequences.  
   - The removed sequence is scanned for the most probable motif position (on both forward and reverse strands) using the PWM.  
   - That best position is reinserted into the motif set.

3. **Convergence Check:**  
   Information content (IC) is tracked across iterations. If the average IC stabilizes below a defined threshold, the sampler stops early.

4. **Final Motif Construction:**  
   After convergence, a final PFM is built from the optimized motif positions and visualized as a sequence logo.

This approach is widely used in computational biology to uncover transcription factor binding sites and other conserved regulatory elements.
