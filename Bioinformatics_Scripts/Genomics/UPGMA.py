distanceMatrix = [
    [0, 12, 12, 13, 15, 15],
    [12, 0, 2, 6, 8, 8],
    [12, 2, 0, 6, 9, 9],
    [13, 6, 6, 0, 8, 8],
    [15, 8, 9, 8, 0, 4],
    [15, 8, 9, 8, 4, 0],
]
speciesList = ["M_Spacii", "T_Pain", "G_Unit", "Q_Doba", "R_Mani", "A_Finch"]

def UPGMA(dM, species, output_file):
    with open(output_file, "w") as f:
        while len(dM) > 1:
            leastRow, leastCol = findSmallest(dM)

            distance = dM[leastRow][leastCol] / 2

            species = updateSpecies(species, distance, leastRow, leastCol)

            dM = updateMatrix(dM, leastRow, leastCol)

            f.write("Updated Distance Matrix:\n")
            for row in dM:
                f.write(" ".join(map(str, row)) + "\n")
            f.write("Updated Species: " + str(species) + "\n\n")
        
        f.write(f"Final Tree: {species[0]}\n")
    return species[0]  

def findSmallest(dM):
    smallest_value = float("inf")
    row, col = -1, -1
    for i in range(len(dM)):
        for j in range(i + 1, len(dM)):
            if dM[i][j] < smallest_value:
                smallest_value = dM[i][j]
                row, col = i, j
    return row, col

def updateSpecies(species, distance, r, c):
    species[r] = f"({species[r]}:{distance},{species[c]}:{distance})"
    del species[c]
    return species

def updateMatrix(dM, row, col):
    newMat = []
    n = len(dM)

    newRow = [(dM[row][i] + dM[col][i]) / 2 for i in range(n) if i != row and i != col]

    #Build the new matrix.
    for i in range(n):
        if i != row and i != col:
            newRowI = [dM[i][j] for j in range(n) if j != row and j != col]
            newMat.append(newRowI)

    for i in range(len(newMat)):
        newMat[i].append(newRow[i])
    newMat.append(newRow + [0])
    
    return newMat

output_file = "C:/Users/johna/OneDrive/Documents/BINF 6400/Problem Set 4/John_Gill_UPGMA_output.txt"
final_tree = UPGMA(distanceMatrix, speciesList, output_file)
print(f"Final tree has been written to {output_file}.")
