import numpy as np

def cal_score(matrix, seq1, seq2, i, j, match, mismatch, gap):
    """
    Calculate score for position (i,j) in scoring matrix, also record move to trace back
    """
    diag_score = matrix[i-1, j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
    up_score = matrix[i-1, j] + gap
    left_score = matrix[i, j-1] + gap
    
    scores = [0, diag_score, up_score, left_score]
    max_score = max(scores)
    move = scores.index(max_score)  # 0-END, 1-DIAG, 2-UP, 3-LEFT
    
    return max_score, move

def traceback(seq1, seq2, traceback_matrix, max_pos):
    """
    Traceback through the matrix to determine the optimal local alignment
    """
    aligned_seq1, aligned_seq2 = [], []
    i, j = max_pos
    
    while traceback_matrix[i, j] != 0:
        if traceback_matrix[i, j] == 1:  # Diagonal (match/mismatch)
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif traceback_matrix[i, j] == 2:  # Up (gap in seq2)
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append('-')
            i -= 1
        elif traceback_matrix[i, j] == 3:  # Left (gap in seq1)
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j-1])
            j -= 1
    
    return "".join(aligned_seq1[::-1]), "".join(aligned_seq2[::-1])

def smith_waterman(seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Smith-Waterman algorithm for local alignment
    """
    m, n = len(seq1), len(seq2)
    score_matrix = np.zeros((m+1, n+1), dtype=int)
    traceback_matrix = np.zeros((m+1, n+1), dtype=int)
    max_score, max_pos = 0, (0, 0)
    
    # Fill the scoring and traceback matrices
    for i in range(1, m+1):
        for j in range(1, n+1):
            score, move = cal_score(score_matrix, seq1, seq2, i, j, match, mismatch, gap)
            score_matrix[i, j] = score
            traceback_matrix[i, j] = move
            if score > max_score:
                max_score, max_pos = score, (i, j)
    
    # Perform traceback
    aligned_seq1, aligned_seq2 = traceback(seq1, seq2, traceback_matrix, max_pos)
    
    return aligned_seq1, aligned_seq2, score_matrix

if __name__ == "__main__":
    # Example usage
    seq1 = 'TACTTAG'
    seq2 = 'CACATTAA'
    aligned_seq1, aligned_seq2, score_matrix = smith_waterman(seq1, seq2)

    print(aligned_seq1)
    print(aligned_seq2)
    print(score_matrix)
