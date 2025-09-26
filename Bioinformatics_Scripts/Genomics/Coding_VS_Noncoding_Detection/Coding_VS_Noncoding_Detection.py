import math

'''John Gill: Genomics in Bioinformatics - Project 4 pt.1: Coding/Noncoding Matrices.
    This program reads in a number of .fasta files as well as a coding and a noncoding
    matrix file. The coding and noncoding matrix files consist of codon scores that are
    mapped to the modelCodons list in this script. Coding and noncoding scores are each saved
    into memory from their respective files, then sequences of two species are read per codon. The first is an
    ancestral species, and the second is a descendent species. Those codons from each file are compared to 
    a score in the coding and noncoding files based on the row (as the first species's codon at that index) and
    the column (as the second species's codon at that index). The score for each is then added to two growing
    scores for every codon for each ID between the two species files: one for coding probabilities, and 
    one for noncoding probabilities. Then the largest score is saved and used to determine whether that
    ID between those two species represents coding or noncoding.'''

file_directory = "C:/Users/johna/OneDrive/Documents/BINF 6400/Problem Set 4/"
ancestor_path = file_directory + "Ancestor.fa"
spacii_path = file_directory + "Spacii.fa"
spacii_2100_path = file_directory + "Spacii_2100.fa"
coding_model_path = file_directory + "codingModel.tab"
noncoding_model_path = file_directory + "noncodingModel.tab"
output_file_path = file_directory + "John_Gill_Model_Output.txt"
output_file_2100_path = file_directory + "John_Gill_Model_Output_2100.txt"

modelCodons = [
    'TTT', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG',
    'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC', 'GTA', 'GTG',
    'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC', 'CCT', 'CCC',
    'CCA', 'CCG', 'ACT', 'ACC', 'ACA', 'ACG', 'GCT', 'GCC',
    'GCA', 'GCG', 'TAT', 'TAC', 'CAT', 'CAC', 'CAA', 'CAG',
    'AAT', 'AAC', 'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG',
    'TGT', 'TGC', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG',
    'GGT', 'GGC', 'GGA', 'GGG', 'TGG', 'TAA', 'TAG', 'TGA'
]

def getProbs(file_path):
    """Reads a probability matrix from a file."""
    
    with open(file_path, 'r') as f:
        pMatrix = []
        for line in f:
            tmp = line.rstrip().split("\t")
            tmp = [float(i) for i in tmp]
            pMatrix.append(tmp)
    return pMatrix

def getSeq(file_path):
    """Reads sequences from a FASTA file."""

    with open(file_path, 'r') as f:
        id2seq = {}
        current_key = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                current_key = line[1:].split("|")[0]  
                id2seq[current_key] = ""
            else:
                id2seq[current_key] += line
    return id2seq

def scoreModels(ancestor_path, spacii_path, output_path):
    """Scores sequences and writes results to the output file."""

    codingMatrix = getProbs(coding_model_path)  
    noncodingMatrix = getProbs(noncoding_model_path)  

    id2ancestorSeq = getSeq(ancestor_path)
    id2spaciiSeq = getSeq(spacii_path)

    allIDs = list(id2ancestorSeq.keys()) 

    with open(output_path, "w") as output_file:

        for ID in allIDs:
            if ID not in id2spaciiSeq:
                continue 

            cScore = 0 
            nScore = 0 

            ancestor_seq = id2ancestorSeq[ID]
            spacii_seq = id2spaciiSeq[ID]

            for i in range(len(ancestor_seq) - 3):
                codon1 = ancestor_seq[i:i+3]
                codon2 = spacii_seq[i:i+3]

                if codon1 in modelCodons and codon2 in modelCodons:
                    row = modelCodons.index(codon1)
                    col = modelCodons.index(codon2)

                    cScore += math.log(codingMatrix[row][col])
                    nScore += math.log(noncodingMatrix[row][col])

            if cScore > nScore:
                output_file.write(f"{ID} is likely coding (cScore: {cScore}, nScore: {nScore})\n")
            else:
                output_file.write(f"{ID} is likely NOT coding (cScore: {cScore}, nScore: {nScore})\n")

scoreModels(ancestor_path, spacii_path, output_file_path)
scoreModels(ancestor_path, spacii_2100_path, output_file_2100_path)
