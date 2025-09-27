# De Bruijn Graph Assembly

This project implements a De Bruijn graph–based algorithm for sequence assembly. It reconstructs an original string or genome from short overlapping substrings (k-mers), demonstrating the core principle used in many modern genome assemblers.

## Overview
The De Bruijn graph approach models sequence assembly as a graph traversal problem. Overlapping k-mers from the input are represented as directed edges between nodes defined by (k-1)-mers. The graph encodes how fragments overlap and can be traversed to reconstruct the original sequence.

The algorithm works as follows:

**K-mer Generation:**  
The input string is decomposed into all possible k-mers of a chosen length.

**Graph Construction:**  
Each (k-1)-mer becomes a node. Directed edges connect nodes whose k-mers overlap by (k-2) bases.

**Eulerian Path Search:**  
An Eulerian path (a trail visiting every edge exactly once) is found through the graph. This path represents the correct order of overlapping fragments.

**Sequence Reconstruction:**  
Starting from the first node, the original string is reconstructed by following the path and appending the last base of each successive node.

This method illustrates how genome assemblers like Velvet and SOAPdenovo piece together large sequences from short reads, leveraging graph theory to solve complex reconstruction problems efficiently.
