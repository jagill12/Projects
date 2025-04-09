import random
import matplotlib.pyplot as plt

base_dir = "C:/Users/johna/OneDrive/Documents/BINF 6400/Problem Set 5"

start_codon = ["ATG"] 
stop_codons = ["TAA", "TAG", "TGA"] 
coding_codons = [
    codon for codon in [f"{a}{b}{c}" for a in "ACGT" for b in "ACGT" for c in "ACGT"]
    if codon not in start_codon + stop_codons
]  #All codons excluding Start and Stop codons.

#Initial probabilities for each codon type.
total_codons = len(start_codon) + len(coding_codons) + len(stop_codons)
k_0 = [
    len(start_codon) / total_codons,  #Probability of starting in any state is now proportional to the percentage of total codons that each codon type takes up.
    len(coding_codons) / total_codons, 
    len(stop_codons) / total_codons, 
]

#Transition matrix.
A = [
    [0.0, 1.0, 0.0],  #From Start to Start, Coding and Stop.
    [0.0, 0.95, 0.05],  #From Coding to Start, Coding and Stop.
    [0.2, 0.8, 0.0],  #From Stop to Start, Coding and Stop.
]

#Dinucleotide transition matrices from part 1.
spacii_dinucleotide_matrix = [
    [0.3855, 0.1122, 0.1121, 0.3902],
    [0.3869, 0.1116, 0.1124, 0.3892],
    [0.3881, 0.1115, 0.1144, 0.3860],
    [0.3887, 0.1133, 0.1133, 0.3848],
]

pathogen_dinucleotide_matrix = [
    [0.4417, 0.0758, 0.1105, 0.3720],
    [0.3876, 0.1666, 0.0683, 0.3775],
    [0.4069, 0.1675, 0.1650, 0.2607],
    [0.3302, 0.1183, 0.1109, 0.4406],
]

baseIDx = {"A": 0, "C": 1, "G": 2, "T": 3}

#Emit a codon using dinucleotide probabilities.
def emit_codon(prev_base, dinucleotide_matrix):
    codon = prev_base
    for _ in range(2): #Emit 2 additional bases to make a codon.
        next_base = random.choices(["A", "C", "G", "T"], weights=dinucleotide_matrix[baseIDx[codon[-1]]])[0]
        codon += next_base
    return codon

#Generate sequences with Three-State HMM.
def generate_orf_sequence(x, dinucleotide_matrix):
    sequence = []
    state = random.choices([0, 1, 2], weights=k_0)[0] #Initial state based on k_0.
    first_ORF_sequence = []
    first_ORF_found = False
    ORF_in_progress = False

    prev_base = random.choice(["A", "C", "G", "T"]) 

    for _ in range(x):
        if state == 0: #Start state.
            codon = random.choice(start_codon) 
            sequence.append(codon)
            if not first_ORF_found:
                first_ORF_sequence.append(codon)
                ORF_in_progress = True
            state = 1  #Transition to Coding.

        elif state == 1: #Coding state.
            codon = emit_codon(prev_base, dinucleotide_matrix)
            sequence.append(codon)
            if ORF_in_progress:
                first_ORF_sequence.append(codon)
            state = random.choices([1, 2], weights=A[1][1:])[0] #Transition to Coding or Stop.
            prev_base = codon[-1] #Update previous base for emission.

        elif state == 2: #Stop state.
            codon = random.choice(stop_codons)
            sequence.append(codon)
            if ORF_in_progress:
                first_ORF_sequence.append(codon)
                first_ORF_found = True
                ORF_in_progress = False
            state = random.choices([0, 1], weights=A[2][:2])[0]  #Transition to Start or Coding.
            prev_base = random.choice(["A", "C", "G", "T"]) #Reset base.

    #Check if the first ORF is incomplete.
    if first_ORF_sequence and not first_ORF_found:
        return sequence, first_ORF_sequence, False

    return sequence, first_ORF_sequence, True

def run_simulation(x, num_sequences, dinucleotide_matrix, model_name):
    ORF_lengths = []
    output_file = f"{base_dir}/John_Gill_ORF_{model_name}_Part_2.txt"

    with open(output_file, "w") as f:
        f.write(f"Sequences and First ORFs for {model_name} Model:\n\n")
        for i in range(num_sequences):
            valid_ORF = False
            while not valid_ORF: #Keep rerunning until a valid ORF is found.
                sequence, first_ORF_sequence, valid_ORF = generate_orf_sequence(x, dinucleotide_matrix)
                if not valid_ORF:
                    print(f"The first ORF did not reach a stop codon before the total emissions counter. Rerunning Sequence {i + 1}...")

            ORF_length = len(first_ORF_sequence)
            ORF_lengths.append(ORF_length)

            f.write(f"Sequence {i+1} (Full Contig): {''.join(sequence)}\n")
            f.write(f"First ORF (Codons): {' '.join(first_ORF_sequence)}\n")
            f.write(f"First ORF Length: {ORF_length} codons\n\n")

    return ORF_lengths

def plot_orf_distribution(ORF_lengths, model_name):
    plt.hist(ORF_lengths, bins=20, density=True, alpha=0.7, edgecolor="black")
    plt.xlabel("ORF Length (codons)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of First ORF Lengths ({model_name} Model)")
    plt.savefig(f"{base_dir}/{model_name}_ORF_distribution.png")
    plt.show()

def main():
    x = 300  #Emissions per sequence.
    num_sequences = 250

    print("Running Spacii simulation...")
    spacii_ORF_lengths = run_simulation(x, num_sequences, spacii_dinucleotide_matrix, "Spacii")
    plot_orf_distribution(spacii_ORF_lengths, "Spacii")

    print("Running Pathogen simulation...")
    pathogen_ORF_lengths = run_simulation(x, num_sequences, pathogen_dinucleotide_matrix, "Pathogen")
    plot_orf_distribution(pathogen_ORF_lengths, "Pathogen")

    plt.hist(
        [spacii_ORF_lengths, pathogen_ORF_lengths],
        bins=20,
        label=["Spacii", "Pathogen"],
        density=True,
        alpha=0.7,
        edgecolor="black",
    )
    plt.xlabel("ORF Length (codons)")
    plt.ylabel("Frequency")
    plt.title("Comparison of ORF Length Distributions")
    plt.legend()
    plt.savefig(f"{base_dir}/Combined_ORF_distribution.png")
    plt.show()

main()
