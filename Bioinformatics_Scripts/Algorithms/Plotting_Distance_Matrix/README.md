# Distance Matrix Construction and Phylogenetic Tree Plotting

This project computes a pairwise distance matrix from biological sequences and uses it to construct and visualize a phylogenetic tree with the Neighbor Joining algorithm. It connects local sequence alignment, distance-based comparison, and tree inference in a single, interpretable pipeline.

## Overview

A distance matrix provides a compact way to represent how similar or different a set of sequences are from one another. Each entry in the matrix corresponds to the distance between a pair of sequences, with smaller values indicating greater similarity.

In this project, distances are derived from Smith Waterman local alignment scores and then used as the input to Neighbor Joining, a classical algorithm for building unrooted phylogenetic trees from distance data.

The workflow is organized as follows.

### Read FASTA Sequences

Sequences are read from a FASTA file and stored in a dictionary keyed by sequence identifier. These sequences form the basis for all downstream comparisons.

### Build the Distance Matrix

Every pair of sequences is locally aligned using Smith Waterman. The maximum alignment score is normalized by sequence length and converted into a distance value between zero and one.

These values populate a symmetric distance matrix with zeros along the diagonal. This matrix summarizes similarity relationships across the entire sequence set.

### Neighbor Joining Tree Construction

The distance matrix is iteratively transformed to identify the closest sequence clusters. At each step, Neighbor Joining merges two clusters, assigns branch lengths, and updates the matrix to reflect the new grouping.

This process continues until a single unrooted tree remains, represented in Newick format.

### Tree Visualization

The resulting Newick tree is rendered using ete3. Branch lengths and leaf labels are displayed to make the inferred relationships easy to interpret.

### Notes

This project highlights the central role of distance matrices in phylogenetics. By separating similarity measurement from tree construction, it makes each step explicit and easy to inspect, while illustrating how classical alignment and clustering algorithms work together in practice.
