# Coding vs Noncoding Classification and Phylogenetic Reconstruction
## Overview
This project came in two parts: one script dedicated to determining the likelihood of regions of DNA sequences in FASTA files being coding versus noncoding,
based on codon substitution probability models, and a second script focused on reconstructing evolutionary relationships between species using a 
distance-based phylogenetic approach (UPGMA).

The first component approaches gene identification from an evolutionary perspective. Rather than searching for known motifs or annotations, sequences are evaluated by comparing how likely observed codon changes are under two competing
models: one representing coding regions, and another representing noncoding regions. By accumulating log-likelihood scores across aligned sequences, the script determines which evolutionary model better explains the observed mutations. 

The second component shifts focus from individual sequence regions to species-level relationships. Using a predefined distance matrix, the UPGMA algorithm iteratively clusters species according to their evolutionary similarity, producing a hierarchical tree that 
represents inferred ancestry under a molecular clock assumption.

Taken together, the two scripts demonstrate complementary ideas in comparitive genomics: evolutionary signals can be used both to infer functional genomic regions and to reconstruct phylogenetic structure across species. 

Both source scripts can be found in the "src" folder of this directory.

## Functionality

### Script 1 - Coding vs Noncoding Classification
The first script evaluates whether aligned DNA sequence regions are more consistent with evolutionary behavior expected from coding or noncoding DNA. The approach used in this script uses two competing models 
for probabistic comparison -- one for coding, and one for noncoding -- instead of relying on annotation databases or predefined gene boundaries.

There are two substitution matrices provided: one trained on coding regions, and another that represents noncoding sequence evolution. Each matrix contains transition probabilities describing the likelihood
of one codon mutating into another over evolutionary time periods.

Fjor each shared sequence ID between an ancestral species and a descendant species:
  - sequences are read from FASTA files
  - codons are compared positionally between species
  - subsitution probabilities are retrived from both models
  - and log-likelihood scores are accumulated across the sequence

The final output reports whether each sequence is more likely coding or noncoding, along with the accumulated scores from both models.

This portion of the project reflects the core concept in comparitive genomics that functional regions of DNA are identifiable by the evolutionary restrictions and permissions for mutation there.

### Script 2 - Phylogenetic Reconstruction with UPGMA (Unweighted Pair Group Method with Arithmetic Mean)
The second script focuses on evolutionary relationships at the species level rather than individual sequences of DNA. It takes a pairwise distance matrix that describes the evolutionary divergence between species,
then constructs a phylogenetic tree using the UPGMA algorithm.

The UPGMA algorithm works by repeatedly identifying the closest pair of species, or clusters, and merging them into a shared ancestory. After each merge, the distance matrix is modified via recalculation using average linkage,
and the process repeats until a single hierarchical tree remains. 

The script records each intermediate clustering step during execution, which includes the updated distance matrices and species groupings. The final result is written in a nested tree format that represents inferred ancestry. 

## Required Input Files
Only the first script, Coding_vs_Noncoding_Scoring.py, requires input files. Those are three FASTA files and two substitution model files.
### FASTA Files
  1. Ancestor.fa
     - Contains ancestral reference sequences used as the baseline for evolutionary comparison
  2. Spacii.fa
     - Descendant species sequences aligned to the ancestor.
  3. Spacii_2100.fa
     - An alternate descendant dataset used to inspect how classification results can change under continued evolution.
     - 
All FASTA files share matching sequence identifiers that allow corresponding regions to be directly compared.

### Substitution Model Files
  1. codingMode.tab
     - Represents mutation behavior in coding regions of DNA.
  2. noncodingModel.tab
     - Represents mutation behavior in noncoding regions of DNA.
Each row and column corresponds to a codon, and entries represent transition probabilities between codons.

## Output Files
These scripts produce a total of three output files between the two of them.

### Coding Classification Outputs
  1. John_Gill_Model_Output.txt
     - Classification results comparing the ancestor to the primary descendant.
  2. John_Gill_Model_Output_2100.txt
     - Classification results comparing the ancestor to the alternate descendant.
Each file lists sequence IDs alongside their coding and noncoding log-likelihood scores as well as the classification decision.
Example:
```
Sequence_12 is likely coding (cScore: -1243.52, nScore: -1388.11)
```
### UPGMA Phylogenetic Reconstruction Output
  1. John_Gill_UPGMA_output.txt
     - Documents the iterative clustering process performed by the UPGMA algorithm, including updated distance matrices following each merge and the final inferred tree structure, written on one line.
