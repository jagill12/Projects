import random
import re
import matplotlib.pyplot as plt

'''John Gill: Genomics in Bioinformatics - Project 2. 
This script generates n sequences of random nucleotide base pairs equal to sequence length,
then scans them for Open Reading Frames (ORFs) based on start codon and stop codon locations,
and if the range between them is divisible by 3 (codon length). It then saves all valid ORFs,
visualizes the distribution of ORF lengths, and shows ORFs longer than 60 bp.'''

START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]
bases = ["A", "T", "C", "G"]

def generate_sequence(length):
    return ''.join(random.choice(bases) for _ in range(length))

def find_orfs(sequence):
    orfs = []
    for match in re.finditer(START_CODON, sequence):
        start = match.start()
        for stop in STOP_CODONS:
            stop_pos = sequence.find(stop, start + 3)
            if stop_pos != -1 and (stop_pos - start) % 3 == 0: #Must be divisible by 3.
                orf = sequence[start:stop_pos + 3]
                orfs.append(orf)
                break
    return orfs

def generate_orf_lengths(num_sequences, seq_length):
    orf_lengths = []
    for i in range(num_sequences):
        seq = generate_sequence(seq_length)
        orfs = find_orfs(seq)
        for orf in orfs:
            orf_lengths.append(len(orf))
    return orf_lengths

#Function to count sequences with ORFs greater than a certain length.
def count_long_orfs(num_sequences, seq_length, min_orf_length=60):
    count = 0
    for i in range(num_sequences):
        seq = generate_sequence(seq_length)
        orfs = find_orfs(seq)
        for orf in orfs:
            if len(orf) > min_orf_length:
                count += 1
                break  #Only count sequences with at least one long ORF.
    return count / num_sequences  #Fraction of sequences with ORFs > min_orf_length.

def visualize_orf_lengths(orf_lengths):
    plt.hist(orf_lengths, bins=20, edgecolor='black')
    plt.title('Distribution of ORF Lengths')
    plt.xlabel('ORF Length (nucleotides)')
    plt.ylabel('Frequency')
    plt.show()

def main():

    num_sequences = 1000  #Number of sequences to generate.
    seq_length = 600      #Length of each sequence.
    orf_lengths = generate_orf_lengths(num_sequences, seq_length)

    print("Visualizing ORF length distribution...")
    visualize_orf_lengths(orf_lengths)

    print("\nCounting sequences with ORFs > 60 nucleotides...")
    short_seq_length = 150
    fraction_with_long_orfs = count_long_orfs(num_sequences, short_seq_length)
    print(f"Fraction of sequences with ORFs > 60 nucleotides: {fraction_with_long_orfs:.4f}")

if __name__ == "__main__":
    main()
