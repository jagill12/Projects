from typing import List, Tuple, Dict
import numpy as np
import ete3
from itertools import combinations
from Project5_smith_waterman import *

def read_fasta(filename: str) -> Dict[str, str]:
    """Reads sequences from FASTA file.

    Args:
        filename (str): Path to FASTA file containing HIV RT sequences

    Returns:
        Dict[str, str]: Dictionary mapping sequence IDs to sequences

    Examples:
        >>> seqs = read_fasta("lafayette_SARS_RT.fasta")
        >>> len(seqs) > 0
        True
    """
    sequences = {}
    with open(filename, "r") as file:
        seq_id = None
        seq = []
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = "".join(seq)
                seq_id = line[1:].split()[0] 
                seq = []
            else:
                seq.append(line)
        if seq_id:
            sequences[seq_id] = "".join(seq) 
    return sequences

def build_distance_matrix(sequencesdict: Dict[str, str]) -> Tuple[np.ndarray, List[str]]:
    """Builds distance matrix using Smith-Waterman scores.

    Args:
        sequences (Dict[str, str]): Dictionary of HIV RT sequences

    Returns:
        Tuple[np.ndarray, List[str]]: Distance matrix and list of sequence IDs

    Examples:
        >>> seqs = read_fasta("lafayette_SARS_RT.fasta")
        >>> mat, ids = build_distance_matrix(seqs)
        >>> mat[0:3, 0:3]  # Show 3x3 slice of distance matrix
        array([[0.000, 0.004, 0.012],
              [0.004, 0.000, 0.012],
              [0.012, 0.012, 0.000]])
        >>> len(ids)  # Number of sequences
        19
    """
    n = len(sequencesdict)
    labels = list(sequencesdict.keys())
    distance_matrix = np.zeros((n, n))

    for i, j in combinations(range(n), 2):
        seq1, seq2 = sequencesdict[labels[i]], sequencesdict[labels[j]]
        _, _, score_matrix = smith_waterman(seq1, seq2)

        max_score = np.max(score_matrix)
        distance = 1 - (max_score / max(len(seq1), len(seq2)))

        distance_matrix[i, j] = distance_matrix[j, i] = distance

    return distance_matrix, labels

def get_min_distance(matrix):
    ''' Function to find the smallest value off-daigonal in the distance
    matrix provided. This is used in the UPGMA algorithm.
    
    Args: 
        matrix (2D numpy array): a distance matrix

    Returns:
        min (float): The smallest distance in the matrix
        pos (tuple): The x and y position of the smallest distance
    
    '''
    min_val = np.inf
    min_pos = (-1, -1)

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i, j] < min_val:
                min_val = matrix[i, j]
                min_pos = (i, j)
    return min_val, min_pos

def compute_q_matrix(matrix):
    n = len(matrix)
    Q = np.zeros((n, n))

    r = np.sum(matrix, axis=1)

    for i in range(n):
        for j in range(n):
            if i != j:
                Q[i, j] = (n - 2) * matrix[i, j] - r[i] - r[j]
            else: 
                Q[i, j] = np.inf

    return Q

def neighbor_joining(
    distance_matrix: np.ndarray,
    labels: List[str]
) -> str:
    """Implements Neighbor-Joining algorithm for phylogenetic tree construction.

    Args:
        distance_matrix (np.ndarray): Distance matrix from Smith-Waterman scores
        labels (List[str]): Sequence identifiers

    Returns:
        str: Newick format tree string

    Examples:
        >>> seqs = read_fasta("lafayette_SARS_RT.fasta")
        >>> mat, ids = build_distance_matrix(seqs)
        >>> tree = neighbor_joining(mat, ids)
        >>> tree.startswith("((DM1:0.002,DM2:0.002)")  # Start of Newick string
        True
        >>> tree.count(",")  # Number of separators in tree
        18
    """
    #First we need to initialize clusters of similar groups from the distance matrix
    n = len(labels)

    class Node:
        def __init__(self, identifier, children=None): 
            self.identifier = identifier
            self.children = children if children is not None else [] 

        def is_leaf(self):
            return not self.children

    tree = {label: Node(label) for label in labels}    

    while n > 2:
        
        #Make Q-matrix
        Q = compute_q_matrix(distance_matrix)
        
        #Find minimum distance in Q-matrix
        _, (i, j) = get_min_distance(Q)
        
        #Compute branch lengths
        r = distance_matrix.sum(axis=1)
        d_i = (distance_matrix[i, j] + (r[i] - r[j]) / (n - 2)) / 2
        d_j = distance_matrix[i, j] - d_i

        #Create new cluster (node with children) updated with branch legnths
        new_cluster = f"({labels[i]}:{d_i:.4f},{labels[j]}:{d_j:.4f})"
        tree[new_cluster] = Node(new_cluster, children=[tree[labels[i]], tree[labels[j]]])

        #Compute new distances for merged node
        new_distances = (distance_matrix[i, :] + distance_matrix[j, :] - distance_matrix[i, j]) / 2
        new_distances = np.delete(new_distances, [i, j])

        #Update distance matrix
        distance_matrix = np.delete(distance_matrix, [i, j], axis = 0)
        distance_matrix = np.delete(distance_matrix, [i, j], axis = 1)
        distance_matrix = np.vstack((distance_matrix, new_distances))  # Wrap in tuple
        distance_matrix = np.hstack((distance_matrix, np.append(new_distances, 0).reshape(-1, 1)))  # Wrap in tuple


        #Update clusters
        labels.pop(max(i, j))
        labels.pop(min(i, j))
        labels.append(new_cluster)
        
        n -= 1

    #Merge last 2 clusters
    final_tree = f"({labels[0]}:{distance_matrix[0, 1]:.4f},{labels[1]}:{distance_matrix[0, 1]:.4f});"
    return final_tree
    
def plot_tree(newick_tree: str, filename="phylogenetic_tree.png") -> None:
    """Plots phylogenetic tree using ete3.

    Args:
        newick_tree (str): Tree in Newick format
    """
    tree = ete3.Tree(newick_tree)
    ts = ete3.TreeStyle()
    ts.show_leaf_name = True
    ts.show_branch_length = True
    ts.mode = "r" 
    tree.render(filename, tree_style=ts)
    return tree.render("%%inline", tree_style=ts)

if __name__ == "__main__":

    # Read HIV RT sequences
    print("Reading sequences...")
    sequences = read_fasta("lafayette_SARS_RT.fasta")
    
    # Build distance matrix using Smith-Waterman
    print("Building distance matrix...")
    dist_matrix, seq_ids = build_distance_matrix(sequences)
    
    # Generate unrooted tree using Neighbor-Joining
    print("Making tree...")
    tree = neighbor_joining(dist_matrix, seq_ids)

    # Plot tree
    print("Plotting tree...")
    plot_tree(tree)
