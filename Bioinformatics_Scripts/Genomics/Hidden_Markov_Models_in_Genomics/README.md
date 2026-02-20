# Hidden Markov Models in Genomics
## Overview
This project explores how probabilistic sequence models can be used to distinguish biological sequence behavior and simulate gene structure using Hidden Markov Models (HMMs). The work in this directory is divided into two complementary
parts. The first script is a training script, which trains organism-specific Markov models directly from genomic sequence data and evaluates how well those models can distinguish two species when inspecting samples that contain 
both of their DNA mixed together. The second script applies those learned statistical properties conceptually by constructing a three-state HMM that simulates Open Reading Frames (ORFs) using different nucleotide transition dynamics, then examines
how gene-length distributions emerge therein.

Together, these scripts demonstrate both sides of HMM usage in genomis: model learning from real data; and sequence generation using probabilistic biological assumptions.

## Project Structure
```
Hidden_MarkovModels_in_Genomics/
│
├── Input/
│   ├── Training_Input/
│   │   ├── MSpacii.fa
│   │   ├── Pathogen.fa
│   │   ├── MSpacii_training.fa
│   │   └── Pathogen_training.fa
│   │
│   └── ORF_HMM_Input/
│       (reserved for future inference inputs)
│
├── Output/
│   ├── Training_Output/
│   └── ORF_HMM_Output/
│
├── src/
│   ├── ORF_HMM_Training.py
│   └── ORF_HMM.py
│
└── README.md
```
## Part 1 - Model Training
### Purpose
This script trains first-order Markov (dinucleotide) models from genomic FASTA sequences belonging to two organisms: Spacii and a Pathogen. The transition probabilities are learned directly from observed sequence data.
Each model caputres how likely one nucleotide is to follow another, producing organism-specific transition matrices that encode statistical sequence structure.

### Inputs
Located in:
```
Input/Training_Input/
```
  - MSpacii_training.fa - sequences used to train the Spacii model
  - Pathogen_training.fa - sequences used to train the Pathogen model
  - MSpacii.fa - evaluation sequences scored against both models
  - Pathogen.fa - evaluation sequences scored against both models
The separation between training and evaluation data mirrors real modeling workflows, preventing the scoring phase from simply memorizing the training set.

### What the Script Does
  1. Counts nucleotide transitions across training sequences.
  2. Converts counts into probability transition matrices.
  3. Computes log-likelihood scores for each sequence under both models.
  4. Measures how strongly sequences resemble one organism versus the other.
  5. Visualizes score distribuitions between species.
### Outputs
Written to:
```
Output/Training_Output/
```
  - part_1_score_distributions.png
      - Histogram comparing log-likelihood score distributions for both organisms.
  - results.tab
      - Tab-separated table containing sequence scores under each model.
### Significance
This stage establishes that genomic sequence composition alone contains enough statistic signaling to separate organisms probabilistically. The resulting dinucleotide behavior becomes the biological foundation used conceptually in Part 2.

## Part 2 - ORF Simulation with a Three-State HMM (ORF_HMM.py)
### Purpose
Where the first script learns sequence statistics from real genomes, this script moves in the opposite direction: it generates sequences using a Hidden Markov Model designed to mimic gene structure.

The model consists of three hidden states:
  - Start state - emits start codons
  - Coding state - emits coding codons according to learned nucleotide dynamics
  - Stop state - emits stop codons and terminates ORFs
Dinucleotide transition behavior derived from Part 1 is embedded into the emission process, allowing simulated genomes to inherit organism-specific statistical properties.

### Why This Script Has no External Inputs
Unlike the training stage, this script does not read external files. All parameters required for simulation are already encoded inside the model:
  - Transition probabilities between biological states
  - Codon definitions
  - Organism-specific dinucleotide matrices
This reflects a common modeling workflow: once parameters are learned, the generative model becomes self-contained. The goal here is not classification but exploration of emergent behavior - specifically how ORF length distributions arise from
probabilistic rules.

### What the Script Does
  1. Initializes a three-state Hidden Markov Model.
  2. Generates synthetic genomic sequences through stochastic state transitions.
  3. Extracts the first valid ORF from each generated sequence.
  4. Repeats simulations hundreds of times per organism model.
  5. Compares ORF length distributions between simulated organisms.

### Outpus
Written to:
```
Output/ORF_HMM_Output/
```
  - John_Gill_ORF_Spacii_Part_2.txt
    - Generated sequences and first ORFs for the Spacii model.
  - John_Gill_ORF_Pathogen_Part_2.txt
    - Generated sequences and first ORFs for the Pathogen model.
  - Spacii_ORF_distribution.png
    - Histogram of simulated ORF lengths.
  - Combined_ORF_distribution.png
    - Direct comparison of ORF lenght distributions between models.
      
### Significance
This stage demonstrates how relatively simple probabilistic rules can preproduce structured biological outcomes. Differences in nucleotdie transition behavrio propagate upward into measurable differences in 
gene-length distributions, illustrating how statistical properteis of genomes influce higher-level biological patterns.

### Requirements
  - Python 3.x
  - matplotlib
    
Install dependencies:
```
pip install matplotlib
```
## Running the Scripts
From the project root:
```
python src/ORF_HMM_Training.py
```
Then run the simulation:
```
python src/ORF_HMM.py
```
Outputs are created automatically inside the appropriate Output/ subdirectories

## Takeaways
The intent of this project was beyond detecting ORFs directly; this project models the probabilistic processes that make ORFs statistically likely to exist in the first place. By separating training and simulation into distinct stages, the 
workflow mirrors how probabilistic models are developed and explored in compuptational genomics research.
