from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def calculate_coverage(reads, contig_length):
    """
    Calculate the coverage of reads across the contig.
    Return an array with the coverage for each position.
    """
    coverage = np.zeros(contig_length)

    for read in reads:
        start = 0
        end = min(len(read), contig_length) 
        coverage[start:end] += 1

    return coverage

def show_coverage(contigs, reads):
    """
    Visualizes the combined coverage across all contigs in a single graph.
    """
    combined_coverage = []

    for index, contig in enumerate(contigs):
        coverage = calculate_coverage(reads, len(contig))
        combined_coverage.append(coverage)
    
    combined_coverage = np.concatenate(combined_coverage)

    plt.figure(figsize=(15, 5))
    plt.plot(combined_coverage)
    plt.xlabel('Position across All Contigs')
    plt.ylabel('Coverage')
    plt.title('Combined Coverage Across All Contigs')
    plt.show()

def readReads(filename):
    """
    Reads the sequences from the input file and returns a list of sequences.
    """
    reads = []
    with open(filename, 'r') as file:
        for line in file:
            read = line.strip()
            if read:
                reads.append(read)
    print(f"Reads loaded: {len(reads)}")
    return reads

def findOverlap(a, b, k):
    """
    Finds the overlap between two reads `a` and `b` of length `k` or greater.
    Returns the overlap length if found, otherwise 0.
    """
    max_overlap = 0
    min_len = min(len(a), len(b))

    #Ensure k is not greater than the smallest read length.
    k = min(k, min_len)

    for i in range(k, min_len + 1):
        if a[-i:] == b[:i]:
            max_overlap = i

    return max_overlap

def mergeReads(reads, k):
    """
    Merges reads by finding overlaps of length `k` or greater.
    Returns a list of assembled contigs.
    """
    merge_count = 0  #Counter to track merges.
    max_iterations = 10000  #Max number of merges to protect from memory overflow.
    last_num_reads = len(reads)  #Track the last number of reads.

    while merge_count < max_iterations:
        max_overlap = 0
        best_pair = (None, None)
        
        for i in range(len(reads)):
            for j in range(len(reads)): 
                if i != j:  # Ensure you're not comparing the read to itself
                    overlap_len = findOverlap(reads[i], reads[j], k)
                    if overlap_len > max_overlap:
                        max_overlap = overlap_len
                        best_pair = (i, j)


        #If no overlap is greater than or equal to k, we are done.
        if max_overlap < k:
            print(f"Breaking loop after {merge_count} merges. No overlap greater than or equal to k found.")
            break

        #Merge the best pair. This is a debugging step that allows easier interpretation of the merging process.
        i, j = best_pair
        print(f"Merging reads[{i}] and reads[{j}] with overlap length {max_overlap}.")
        reads[i] = reads[i] + reads[j][max_overlap:]
        del reads[j]
        merge_count += 1

        #Check if no new merges were made (convergence).
        if len(reads) == last_num_reads:
            print("No reduction in number of reads. Stopping merging to avoid infinite loop.")
            break

        #Update last number of reads for next iteration.
        last_num_reads = len(reads)

    print(f"Total number of contigs after merging: {len(reads)}")  #Check final number of contigs.
    return reads

def writeContigs(contigs, output_file):
    """Writes contigs to a FASTA file."""
    with open(output_file, 'w') as file:
        for index, contig in enumerate(contigs):
            file.write(f">contig_{index + 1}\n")
            file.write(f"{contig}\n")

def assemble_reads(input_file, output_file, k=10):

    reads = readReads(input_file) 

    contigs = mergeReads(reads, k)

    writeContigs(contigs, output_file)

    show_coverage(contigs, reads)

def main():

    BASE_DIR = Path(__file__).resolve().parent

    #input data folder (you include this in the repo).
    DATA_DIR = BASE_DIR / "Input"

    #output folder created automatically.
    OUTPUT_DIR = BASE_DIR / "Output"
    OUTPUT_DIR.mkdir(exist_ok=True)

    input_file = DATA_DIR / "seqReadFile2023.txt"
    output_file = OUTPUT_DIR / "contigs.fasta"

    k = 10  #Minimum overlap length.

    assemble_reads(input_file, output_file, k)

    print(f"Assembly complete. Contigs written to {output_file.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
