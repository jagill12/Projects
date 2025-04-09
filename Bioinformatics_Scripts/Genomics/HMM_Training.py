import math
import matplotlib.pyplot as plt

baseIDx = {"A": 0, "C": 1, "G": 2, "T": 3}

def main():

    base_dir = "C:/Users/johna/OneDrive/Documents/BINF 6400/Problem Set 5"

    spaciiFA = f"{base_dir}/MSpacii.fa"
    pathogenFA = f"{base_dir}/Pathogen.fa"
    spaciiFA_T = f"{base_dir}/MSpacii_training.fa"
    pathogenFA_T = f"{base_dir}/Pathogen_training.fa"

    spaciiID2seq = getSeq(spaciiFA)
    pathogenID2seq = getSeq(pathogenFA)

    #Initialize and train models.
    spaciiTrainModel = [[0 for _ in range(4)] for _ in range(4)]
    pathTrainModel = [[0 for _ in range(4)] for _ in range(4)]

    print("Training Spacii Model...")
    spaciiTrainModel = trainModel(spaciiTrainModel, spaciiFA_T, "Spacii")
    print("\nTraining Pathogen Model...")
    pathTrainModel = trainModel(pathTrainModel, pathogenFA_T, "Pathogen")

    #Score sequences.
    markovScoresSpacii = []
    markovScoresPath = []

    for ID in spaciiID2seq.keys():
        score = getLogLike(spaciiTrainModel, pathTrainModel, spaciiID2seq[ID])
        markovScoresSpacii.append(score)

    for ID in pathogenID2seq.keys():
        score = getLogLike(spaciiTrainModel, pathTrainModel, pathogenID2seq[ID])
        markovScoresPath.append(score)

    plt.hist(
        [markovScoresPath, markovScoresSpacii],
        bins=20,
        label=["Pathogen", "Spacii"],
        rwidth=1,
        density=True,
    )
    plt.legend(loc='upper right')
    plt.xlabel("Log-Likelihood Scores")
    plt.ylabel("Density")
    plt.title("Score Distributions for Pathogen and Spacii")
    plt.savefig(f"{base_dir}/part_1_score_distributions.png")
    plt.show()

    scoresOutputText(markovScoresSpacii, markovScoresPath, base_dir)

def getLogLike(model1, model2, seq):
    Pmod1 = 0  #Log probability for model 1.
    Pmod2 = 0  #Log probability for model 2.

    #Iterate through sequence pairs.
    for i in range(len(seq) - 1):
        curr_base = baseIDx[seq[i]]
        next_base = baseIDx[seq[i + 1]]
        #Add log probabilities for both models.
        Pmod1 += math.log(model1[curr_base][next_base] + 1e-10)
        Pmod2 += math.log(model2[curr_base][next_base] + 1e-10)

    return Pmod1 - Pmod2

def trainModel(model, data, model_name):
    counts = [[0 for _ in range(4)] for _ in range(4)]

    id2seq = getSeq(data)

    #Count transitions.
    for seq in id2seq.values():
        for i in range(len(seq) - 1):
            curr_base = baseIDx[seq[i]]
            next_base = baseIDx[seq[i + 1]]
            counts[curr_base][next_base] += 1

    #Convert counts to probabilities.
    for i in range(4):
        row_sum = sum(counts[i])
        if row_sum > 0:
            model[i] = [count / row_sum for count in counts[i]]

    print(f"{model_name} Model Transition Matrix:")
    print_matrix_with_labels(model)
    return model

def print_matrix_with_labels(matrix):

    labels = ["A", "C", "G", "T"]
    print("      " + "  ".join(labels))
    for i, row in enumerate(matrix):
        print(f"{labels[i]}: {['%.4f' % x for x in row]}")

def getSeq(filename):
    with open(filename, "r") as f:
        id2seq = {}
        currkey = ""

        for line in f:
            if line.startswith(">"):
                currkey = line.rstrip()[1:]
                id2seq[currkey] = ""
            else:
                id2seq[currkey] += line.rstrip()
    return id2seq

def scoresOutputText(markovScoresSpacii, markovScoresPath, base_dir):
    output_file = f"{base_dir}/results.tab"
    with open(output_file, "w") as f:
        f.write("SpaciiScores\tPathogenScores\n")
        for sp_score, pa_score in zip(markovScoresSpacii, markovScoresPath):
            f.write(f"{sp_score}\t{pa_score}\n")

main()
