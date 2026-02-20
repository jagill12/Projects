# ORF Analysis and Distribution Characterization
## Overview
This directory contains two related scripts that explore Open Reading Frames (ORFs) from complementary perspectives. An ORF in a biological context is a trascripbable region of DNA based on a start codon and stop codon.
The first script investigates how ORFs arise statistically by analyzing randomly generated DNA sequences, while the second applies ORF detection and scoring methods to real sequence data. Together, these two scripts
demonstrate the likelihood of ORFs occuring by chance, and the additional filtering necessary to identify biologically significant candidates. In that way, the workflow of these scripts moves from simulation to analysis: first
by establishing expectations for ORF behavior in an unconstrained sequence space following blind probabilities, then by applying structured detection and motif scoring to assembled contigs.

## Script 1 - Long Read Distribution
```
  -File: src/Long_Read_Distribution.py
```
This script generates random DNA sequences and scans them for valid Open Reading Frames based on start codons, stop codons, and reading frame constraints. The aim is to observe how often ORFs appear in sequences that contain no biological signal, which 
provides intuition for why ORF detection alone is not sufficient evidence of gene content.

### Method
  - First it generates random nucleotide sequences, giving equal probabilities to A, T, C, and G
  - ORFs are then identified using:
    - The start codon ATG; the stop codons TAA, TAG, and TGA; and a preserved reading frame where the length is divisible by three (since codons are 3 nucleotides).
  - Then it collects ORF lengths across many simulated sequences
  - Generates a histogram to visualize the distribution of ORF lengths
  - And finally, the script estimates the fraction of sequences containing ORFs longer than 60 nucleotides.
Using the default parameters (1000 sequences of length 600), approximately 17.5% of simulated sequences contained at least one ORF longer than 60 nucleotides. The results can vary slightly, but they follow that general trend, which highlights how
frequently coding-like structures can arise purely by chance in random DNA.

### Output
The script produces a .PNG file containing a histogram that visualizes the distribution of ORF lengths, and console output reporting the fraction of sequences containing long ORFs.
A copy of the resulting visualization is included in this directory's Output/ folder as "Figure_1.png." The script does not automatically export this image, it was manually saved and uploaded here.

## Script 2 - ORF Detection and Motif Scoring
```
  - File: src/ORF_Detection_and_Motif_Scoring.py
```
The second script analyzes contigs stored in a FASTA file and identifies biologically valid ORFs, then evaluates those ORFs using a positional scoring motif.

### Method
  1. Read contigs from an input FASTA file.
  2. Detect ORFs using:
     - start codons (ATG, GTG)
     - stop codons (TAA, TAG, TGA)
     - frame preservation (divisible by 3)
     - minimum ORF length >= 60 nucleotides
  3. Slides a 13-base window across each ORF.
  4. Scores each window using a position-specific scoring matrix.
  5. Records subsequences exceeding a defined quality threshold.
The result is both a structural identification of ORFs, and an additional scoring layer used to highlight regions that may represent stronger coding candidates.

### Output
The script generates a FASTA-style results file containing all valid ORFs with positional metadata, and a secordary section listing high-scoring 13 bp motif regions.
The output location in this directory is Outpu/orf_results.fasta

### Input
The only necessary input for this directory is spaceSeq.fa, a FASTA file containing contigs analyzed for ORFs for the second script.

## Running the Scripts
From the project root directory:

  - python src/Long_Read_Distribution.py
  - python src/ORF_Detection_and_Motif_Scoring.py

Outputs are written to the Output/ directory.

## Repository Structure:
```
Long_Read_Distribution/
│
├── Input/
│   └── spaceSeq.fa
│
├── Output/
│   ├── Figure_1.png
│   └── orf_results.fasta
│
├── src/
│   ├── Long_Read_Distribution.py
│   └── ORF_Detection_and_Motif_Scoring.py
│
└── README.md
```
## Conceptual Takeaway
Open Reading Frames are a necessary, but incomplete signal for identifying protein-coding regions of DNA. Random DNA frequently produces ORFs that satisfy structural constraints, meaning additional statistical or motif-based evidence
is required to prioritize biologically meaningful candidates.

By pairing simulation with sequence analysis, it becomes apparent how computational genomics balances pattern detection with statistical interpretation within the context of gene discovery.
