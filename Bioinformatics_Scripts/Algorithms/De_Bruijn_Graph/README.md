# De Bruijn Graph (String Reconstruction)

## Overview
This project implements a simple De Bruijn graph builder and Eulerian traversal algorithm in Python. It constructs a graph from an input string and a chosen k-mer length, then performs a randomized Eulerian walk to reconstruct the original string. The script demonstrates the fundamental principles behind how De Bruijn graphs are used in fields like bioinformatics and text processing.

## What a De Bruijn Graph Is
A De Bruijn graph is a way to represent overlapping substrings (k-mers) of a sequence as nodes and edges. Each node represents a substring of length `k-1`, and each edge represents a k-mer connecting two nodes. If one substring overlaps with another by `k-2` characters, there is an edge between them.

This graph structure captures how short pieces of a sequence fit together. By finding an Eulerian path — a path that uses every edge exactly once — you can reconstruct the original string.

## Why It Matters
In bioinformatics, De Bruijn graphs are central to genome assembly. DNA sequencing often produces millions of short reads. These reads overlap with each other, and by building a De Bruijn graph of all the k-mers, tools like SPAdes and Velvet can reconstruct the original genome sequence.  
Outside biology, the same principle applies to text reconstruction, error correction, and network traversal problems, where finding an Eulerian path can solve complex ordering or reconstruction tasks.

## What This Script Does
This script builds a De Bruijn graph from a single input string and reconstructs the original string through a randomized Eulerian walk.

- It builds the graph by sliding a window of length `k` across the input and connecting overlapping substrings (`k-1`-mers).
- It stores edges in an adjacency list (`defaultdict(list)`).
- It randomly chooses outgoing edges during traversal to reduce deterministic bias.
- It performs a recursive Eulerian walk that removes edges as they are used.
- It reconstructs the original string from the resulting path.

Because the traversal is randomized, repeated runs can produce different but valid Eulerian paths, which can be useful when exploring different graph configurations or resolving ambiguities in complex graphs.

## Example
Input string:
"fool me once shame on shame on you fool me"

perl
Copy code
K-mer length:
6

sql
Copy code

Steps performed:
1. Build nodes for every 5-character substring (`k-1`).
2. Add directed edges for every 6-character substring.
3. Start the walk from the first node.
4. Randomly traverse edges until every edge is used exactly once.
5. Reconstruct the string from the Eulerian path.

Output:
['fool ', 'ool m', 'ol me', ...] # The path through the graph
fool me once shame on shame on you fool me # Reconstructed string

sql
Copy code

## Installation
Clone this repository or copy the script into your project. No external libraries are required beyond Python’s standard library.

git clone https://github.com/yourusername/Projects.git
cd Projects/Bioinformatics_Scripts/Algorithms/De_Bruijn_Graph

shell
Copy code

## Usage
Interactive run:
python De_Bruijn_Graph.py

css
Copy code

Within the script:
```python
dbg = DeBruijnGraph("fool me once shame on shame on you fool me", 6)
walk = dbg.print_eulerian_walk()
reconstructed = walk[0] + ''.join(node[-1] for node in walk[1:])
print(reconstructed)
Applications
Genome assembly from short sequencing reads

Error correction in long sequences

Text reconstruction from overlapping fragments

Graph theory and combinatorial problems involving Eulerian paths

Future Improvements
Add validation to check if the graph has a valid Eulerian path before traversal.

Extend support for multiple sequences (like handling many reads from a sequencing dataset).

Implement an iterative version of the walk to handle very large graphs without recursion depth issues.

Copy code
