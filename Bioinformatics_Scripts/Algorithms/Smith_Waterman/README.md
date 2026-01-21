# Smith-Waterman Local Sequence Alignment

This project implements the Smith-Waterman algorithm for local sequence alignment. It identifies the highest-scoring matching subsequences between two strings and outputs both the alignment and the corresponding scoring matrix.

## Overview

Local alignment focuses on finding the best matching region between two sequences, rather than aligning them end-to-end. Smith-Waterman uses dynamic programming to compute a score matrix that reflects matches, mismatches, and gaps. The highest-scoring cell identifies the end of the optimal local alignment, which is then recovered via traceback.

This algorithm underpins other sequence-based projects, such as phylogenetic tree construction, where pairwise similarity needs to be quantified before building distance matrices.

The workflow is as follows.

### Scoring Matrix Calculation

The scoring matrix is filled iteratively. For each cell, scores are calculated for:

a diagonal move (match or mismatch)

an upward move (gap in the second sequence)

a leftward move (gap in the first sequence)

zero (to allow local alignment restarts)

The highest of these values becomes the cell score, and the corresponding move is recorded in a traceback matrix.

### Traceback to Determine Alignment

Starting from the cell with the maximum score, the traceback matrix is followed to reconstruct the optimal local alignment. The path stops when a zero cell is reached. This produces two aligned sequences with gaps as needed.

### Output

The algorithm returns:

the aligned subsequences

the scoring matrix, which provides a full view of local similarity

### Notes

This implementation highlights how dynamic programming can efficiently solve sequence alignment problems. It forms a foundation for downstream analyses, including pairwise distance computation and phylogenetic tree construction, by providing a rigorous measure of sequence similarity.
