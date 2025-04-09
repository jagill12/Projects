import re

'''John Gill: Genomics in Bioinformatics - Project 2.
    This project takes in a .fa input file, strips it line-by-line
    and finds valid Open Reading Frames within each contig based on starting
    sequences, stop sequences, whether the ORF is divisible by 3, and if
    the nucleotide base pairs are >= 60. If all of those criteria are met,
    that ORF is saved as "valid ORF." Then each valid ORF is scored
    according to a scoring matrix, and the high-scoring ORFs are saved
    into a separate list for display as well.'''

def scanSeq(sequence):
    orf_seqs = []
    start_positions = []
    orf_lengths = []
    
    start_codons = [m.start() for m in re.finditer('ATG|GTG', sequence)]
    stop_codons = [m.start() for m in re.finditer('TAA|TAG|TGA', sequence)]

    for start in start_codons:
        for stop in stop_codons:
            if stop > start and (stop - start) % 3 == 0:
                orf_seq = sequence[start:stop+3]
                if len(orf_seq) >= 60:  #Check minimum length condition.
                    orf_seqs.append(orf_seq)
                    start_positions.append(start)
                    orf_lengths.append(len(orf_seq))
                break
    return orf_seqs, start_positions, orf_lengths

#scoreMotif function to slide across the entire ORF and check every 13bp sequence.
def scoreMotif(orf_seq, quality_score_cutoff=7.5):
    base_idx = { 'A' : 0, 'T' : 1, 'C' : 2, 'G' : 3 }
    motif = [
        [.5, .5, .5, .5, 0, 0, 0, 0, 0, 2, -99, -99, .5],  # A
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -99, 2, -99, 0],       # T
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -99, -99, -99, 0],     # C
        [.5, .5, .5, .5, 0, 0, 0, 0, 0, .5, -99, 2, 0]     # G
    ]
    
    high_score_sequences = []

    #Slide through and score every 13bp sequence.
    for i in range(len(orf_seq) - 12):
        seq_13bp = orf_seq[i:i+13]
        
        score = 0
        for j, base in enumerate(seq_13bp):
            if base in base_idx:
                score += motif[base_idx[base]][j]
            else:
                raise ValueError(f"Unexpected base '{base}' in the sequence.")

        if score > quality_score_cutoff:
            high_score_sequences.append((seq_13bp, i, score))

    return high_score_sequences

#Function to identify ORFs and write output to a file.
def identify_ORFs(input_content, output_file, quality_score_cutoff=7.5, min_orf_length=60):
    with open(output_file, 'w') as outfile:
        contig_count = -1  #Start from 0.
        orf_count = 0  #Counter for ORFs across all contigs.
        current_sequence = ""
        contig_label = ""
        
        valid_orfs = []
        high_score_13bp = []

        for line in input_content:
            line = line.strip()
            if line.startswith(">"):  #Start of a new contig.
                if current_sequence:
                    orfs, starts, lengths = scanSeq(current_sequence)
                    for i, orf in enumerate(orfs):

                        orf_count += 1
                        
                        label = f">{contig_label}|Length {lengths[i]}|at position {starts[i]}|ORF {orf_count}"
                        orf_entry = f"{label}\n{orf}\n"
                        
                        valid_orfs.append(orf_entry)

                        #Slide through ORF for 13bp sequences with score > 7.5.
                        high_score_sequences = scoreMotif(orf, quality_score_cutoff)
                        for seq, pos, score in high_score_sequences:
                            high_score_13bp.append(f"From {contig_label}, ORF {orf_count}: ORF position {pos} with score {score}\n{seq}\n")
                
                #Reset for the new contig.
                contig_count += 1
                contig_label = f"contig {contig_count}"
                current_sequence = ""
            else:
                current_sequence += line.strip()

        #Process the last contig after the loop finishes.
        if current_sequence:
            orfs, starts, lengths = scanSeq(current_sequence)
            for i, orf in enumerate(orfs):
                orf_count += 1
                label = f">{contig_label}|Length {lengths[i]}|at position {starts[i]}|ORF {orf_count}"
                orf_entry = f"{label}\n{orf}\n"
                
                valid_orfs.append(orf_entry)

                #Slide through ORF for 13bp sequences with score > 7.5.
                high_score_sequences = scoreMotif(orf, quality_score_cutoff)
                for seq, pos, score in high_score_sequences:
                    high_score_13bp.append(f"From {contig_label}, ORF {orf_count}: 13bp sequence at ORF position {pos} with score {score}\n{seq}\n")

        outfile.write("The ORFs will be listed first.\n"
                      "Then there is a second section beneath with high-scoring 13bp sequences from each ORF.\n")
        for orf in valid_orfs:
            outfile.write(orf)

        outfile.write("\nEach 13bp sequence from each ORF with a score greater than 7.5:\n")
        for seq in high_score_13bp:
            outfile.write(seq)

def main():
    input_file = 'c:/Users/johna/OneDrive/Documents/BINF 6400/Problem Set 2/spaceSeq.fa'
    output_file = 'c:/Users/johna/OneDrive/Documents/BINF 6400/Problem Set 2/John_Gill_Homework_2_orf_output.fasta'

    with open(input_file, 'r') as infile:
        input_content = infile.readlines()

    identify_ORFs(input_content, output_file)

    print(f"ORF identification complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
