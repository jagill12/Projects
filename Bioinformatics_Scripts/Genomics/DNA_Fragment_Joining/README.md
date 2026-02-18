# Fragment Joining
## Overview
This script simulates a simplified version of early genome assembly: you start with a pile of short DNA fragments (sequencing reads) and iteratively join them together by finding overlaps between read ends.The result is a set of longer
assembled sequences (contigs) written to a FASTA file, plus a simple coverage-style visualization meant to help interpret how much read support exists across the contigs.

Modern assemblers use De Bruijn graphs and error modeling, this is not meant to compete with them. The goal of this script is to implement the core idea behind overlap-layout style assembly in an easy-to-read-and-run way. I have a script showcasing
my aptitude with De Bruijn graphs in my Projects/Bioinformatics_Scripts/Algorithms directory.

## What this script does
Given a .txt file containing DNA fragments (one per read line), this script: 
  - Loads all reads into memory
  - Searches for overlaps between every pair of reads
  - Repeatedly merges the pair with the largest suffix-preffix overlap, so long as the overlap is at least of length k
  - Stops when no overlap >= k remains, or if merge safeguards trigger
  - Writes the final contigs to a FASTA file
  - Plots a combined coverage-style graph across all contigs

## How it works
### Overlap Detection
Given two reads, a and b, the script checks to see if the suffix of a matches the prefix of b for any overlap length i >= k. If matches exist, it uses the largest overlap length found.
### Greedy Merging
At each iteration, the script picks the best overlap found across all read pairs and merges that pair. This is a greedy strategy, meaning it makes the best local choice at each step rather than optimizing globally.

Because it's greedy, it can be sensitive to repeats and ambiguous overlaps, which is expected for this style of assembler.

## Inputs and Outputs
### Input
  - Input/seqReadFil2023.txt
      - This is a plain text file containing DNA reads, one per line
### Outputs
This script creads an outputs/ folder automatically, and writes a FASTA file to it containing the assembled contigs:
  - outputs/contigs.fasta
It also displays a coverage plot as a support visualization. The reads are not aligned to contigs by position in the script; rather, the plot refelcts read length stacking across contigs instead of exact genomic length.

## Parameters 
k is th eminimum overlap length, set at 
```
k = 10
```
Increasing k makes the merging stricter and can result in more contigs, while decreasing k can ease merging but may result in incorrect merges through repeats, or weak overlaps.

## Dependencies
  - Python 3.x
  - numpy
  - matplotlib
### Install Dependencies
```
pip install numpy matplotlib
```
## Running the Script
From the project's root directory (DNA_Fragment_Joining):
```
python src/Fragment_Joining.py
```
Assembled contigs will be written to 
```
Output/contigs.fasta
```
## Repository structure
```
DNA_Fragment_Joining/
│
├── Input/
│   └── seqReadFile2023.txt
│
├── Output/
│   └── (created automatically at runtime)
│
├── src/
│   └── Fragment_Joining.py
│
└── README.md
```
