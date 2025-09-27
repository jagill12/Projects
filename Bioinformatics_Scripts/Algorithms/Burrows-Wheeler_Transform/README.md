# Burrows–Wheeler Transform (BWT)

This project implements the Burrows–Wheeler Transform, a reversible text transformation widely used in compression algorithms and sequence alignment tools. It rearranges an input string into a form that groups similar characters together, improving compressibility and enabling rapid searching.

## Overview
The Burrows–Wheeler Transform is a key preprocessing step in bioinformatics tools such as Bowtie and BWA. It reorders the input string’s rotations to exploit character redundancy, while maintaining enough information to reconstruct the original sequence.

The algorithm works as follows:

**Rotation Matrix Construction:**  
All cyclic rotations of the input string are generated and sorted lexicographically.

**Last Column Extraction:**  
The last character of each sorted rotation is concatenated to form the transformed string (the BWT).

**Reversibility:**  
Although the BWT appears scrambled, it retains implicit ordering information. Using this structure, the original string can be reconstructed without additional data.

**Applications:**  
The BWT enables efficient suffix array construction and fast substring matching, forming the backbone of FM-index–based aligners and modern text compression schemes.
