import numpy as np
import seqlogo
from data_readers import *
from seq_ops import get_seq, reverse_complement
from motif_ops import *

def GibbsMotifFinder(seqs, k, seed=42, iterations=1000, convergence_threshold=0.001, window_size=50):
    '''
    Function to find a pfm from a list of strings using a Gibbs sampler
    
    Args: 
        seqs (str list): a list of sequences, not necessarily in same lengths
        k (int): the length of motif to find
        seed (int, default=42): seed for np.random

    Returns:
        pfm (numpy array): dimensions are 4xlength
        
    '''
    #Set random seed to make results reproducible.
    np.random.seed(seed)
    
    #Initialize motif positions randomly.
    positions = [np.random.randint(0, len(seq) - k + 1) for seq in seqs]
    ic_history = [] #Initialize an information content (IC) list.
    prev_ic = 0 

    for iter_num in range(iterations):
        #Randomly pick a sequence to leave out.
        idx = np.random.randint(len(seqs))
        removed_seq = seqs[idx]
        del positions[idx]
        
        #Build PFM excluding the removed sequence.
        selected_kmers = [seqs[j][positions[j]:positions[j] + k] for j in range(len(positions))] #Extracts the current motif from all other sequences, excluding the removed sequence.
        pfm = build_pfm(selected_kmers, k) #Build a Position Frequency Matrix (PFM) from the selected kmers.
        pwm = build_pwm(pfm) #Convert the PFM to a PWM.
        
        #Scan removed sequence for best motif position.
        best_score = float('-inf') #Initializing "best score" to negative infinity allows us to track the highest scoring position.
        best_position = 0 #Initialize the best position.
        best_strand = '+'
        for i in range(len(removed_seq) - k + 1): #Iterate over all possible k-mers in the removed sequence.
            kmer = removed_seq[i:i + k]
            rev_kmer = reverse_complement(kmer)

            score_fwd, _, _ = score_sequence(kmer, pwm)
            score_rev, _, _ = score_sequence(rev_kmer, pwm)

            if score_fwd > best_score: #Update the best position to the position with the highest motif score. 
                best_score = score_fwd
                best_position = i
                best_strand = '+'
            if score_rev > best_score:
                best_score = score_rev
                best_position = i
                best_strand = '-'
        
        #Reinsert best position.
        positions.insert(idx, best_position)

        ic = pfm_ic(pfm)
        ic_history.append(ic)

        if iter_num >= window_size:
            recent_ic_avg = np.mean(ic_history[-window_size:])
            if abs(recent_ic_avg - prev_ic) < convergence_threshold:
                print(f"Convergence reached at iteration {iter_num}")
                break
            prev_ic = recent_ic_avg
    
    #Build final PFM.
    final_kmers = [seqs[i][positions[i]:positions[i] + k] for i in range(len(seqs))] #Extract the final set of motifs.
    pfm = build_pfm(final_kmers, k) #Constructs a final pfm.
    
    return pfm

def main():
    # Read promoters and store in a list of strings
    seq_file = "GCF_000009045.1_ASM904v1_genomic.fna"
    gff_file = "GCF_000009045.1_ASM904v1_genomic.gff"

    seqs = []

    for name, seq in get_fasta(seq_file):
        for gff_entry in get_gff(gff_file):
            if gff_entry.type == 'CDS':
                promoter_seq = get_seq(seq, gff_entry.start, gff_entry.end, gff_entry.strand, 50)
                
                # Pre-filter for sequences that contain part of the Shine-Dalgarno motif
                if "AGGAGG" in promoter_seq:
                    seqs.append(promoter_seq)

    # Run the Gibbs sampler
    promoter_pfm = GibbsMotifFinder(seqs, 10)

    # Plot the final PFM that is generated
    seqlogo.seqlogo(seqlogo.CompletePm(pfm=promoter_pfm.T), format='png', filename="motif_logo.png")


if __name__ == "__main__":
    main()
