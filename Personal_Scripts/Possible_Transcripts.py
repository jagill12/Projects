# codons mapped to their corresponding amino acids
codon_to_amino_acid = {
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",
    "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
    "CAU": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
    "AGA": "Arginine", "AGG": "Arginine",
    "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine",
    "AUG": "Methionine",
    "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
    "AAU": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",
    "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
    "GAU": "Aspartic Acid", "GAC": "Aspartic Acid",
    "GAA": "Glutamic Acid", "GAG": "Glutamic Acid",
    "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
}

# amino acids mapped to their corresponding codons
amino_acid_to_codons = {
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "Tyrosine": ["UAU", "UAC"],
    "STOP": ["UAA", "UAG", "UGA"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
    "Proline": ["CCU", "CCC", "CCA", "CCG"],
    "Histidine": ["CAU", "CAC"],
    "Glutamine": ["CAA", "CAG"],
    "Arginine": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Isoleucine": ["AUU", "AUC", "AUA"],
    "Methionine": ["AUG"],
    "Threonine": ["ACU", "ACC", "ACA", "ACG"],
    "Asparagine": ["AAU", "AAC"],
    "Lysine": ["AAA", "AAG"],
    "Valine": ["GUU", "GUC", "GUA", "GUG"],
    "Alanine": ["GCU", "GCC", "GCA", "GCG"],
    "Aspartic Acid": ["GAU", "GAC"],
    "Glutamic Acid": ["GAA", "GAG"],
    "Glycine": ["GGU", "GGC", "GGA", "GGG"]
}

# amino acids' abridged names mapped to their full names
abridged_to_full_name = {
    "Phe": "Phenylalanine",
    "Leu": "Leucine",
    "Ser": "Serine",
    "Tyr": "Tyrosine",
    "Cys": "Cysteine",
    "Trp": "Tryptophan",
    "Pro": "Proline",
    "His": "Histidine",
    "Gln": "Glutamine",
    "Arg": "Arginine",
    "Ile": "Isoleucine",
    "Met": "Methionine",
    "Thr": "Threonine",
    "Asn": "Asparagine",
    "Lys": "Lysine",
    "Val": "Valine",
    "Ala": "Alanine",
    "Asp": "Aspartic Acid",
    "Glu": "Glutamic Acid",
    "Gly": "Glycine",
    "STOP": "STOP"
}

# Reverse dictionary to map full names to abridged names
full_to_abridged_name = {v: k for k, v in abridged_to_full_name.items()}

def codonlist(transcript):
    sequence_full = ""
    sequence_abridged = ""
    final = len(transcript) // 3
    read = 0

    while read < final:
        codon = transcript[read*3:read*3+3]  # Determine the current codon

        if codon in codon_to_amino_acid:
            amino_acid_full = codon_to_amino_acid[codon]
            amino_acid_abridged = full_to_abridged_name[amino_acid_full]
            if amino_acid_full == "STOP":
                break
            sequence_full += amino_acid_full + " "
            sequence_abridged += amino_acid_abridged + " "
        else:
            print(f"Invalid codon: {codon}")
            break

        read += 1

    return sequence_full.strip(), sequence_abridged.strip()

def count_possible_transcripts(amino_acids):
    total_transcripts = 1  # Initialize total transcripts count

    for amino_acid in amino_acids:
        # Translate abridged names to full names if necessary
        if amino_acid in abridged_to_full_name:
            amino_acid = abridged_to_full_name[amino_acid]
        
        if amino_acid not in amino_acid_to_codons:
            print(f"Invalid amino acid: {amino_acid}")
            return 0
        total_transcripts *= len(amino_acid_to_codons[amino_acid])
    
    return total_transcripts

def main():
    choice = input("Choose an option:\n1. Sequence a protein by codons\n2. Determine possible sequences by amino acid sequence\nEnter 1 or 2: ")
    
    if choice == '1':
        transcript = input("Give me an RNA transcript consisting of only A, C, U, or G characters and I will tell you the specific amino acid sequence it encodes.")
        
        # Capitalize all letters
        transcript = transcript.upper()
        
        # Remove spaces
        transcript = transcript.replace(" ", "")
        
        
        valid_characters = {'A', 'C', 'U', 'G'}
        if all(char in valid_characters for char in transcript):
            
            amino_acid_sequence_full, amino_acid_sequence_abridged = codonlist(transcript)
            print(f"The amino acid sequence is: {amino_acid_sequence_full}")
            print(f"The abridged amino acid sequence is: {amino_acid_sequence_abridged}")
        else:
            print("Invalid input. The transcript should only contain A, C, U, or G characters.")
    
    elif choice == '2':
        amino_acids = input("Enter a list of amino acids (full names or abridged names) separated by spaces: ").split()
        total_transcripts = count_possible_transcripts(amino_acids)
        print(f"Total number of possible transcripts: {total_transcripts}")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
