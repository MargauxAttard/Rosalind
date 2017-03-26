def localAlignment(v, w, match, mismatch, indel):
    
    #initialize matrices
    matrix = np.zeros([len(v)+1, len(w)+1])
    backtrack = np.zeros([len(v)+1, len(w)+1])
    maxScore, maxI, maxJ = -1, 0, 0
    
    #fill in score and backtrack
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            mate = match
            if v[i-1] != w[j-1]:
                mate = mismatch
            scores = [matrix[i-1][j]+indel, matrix[i][j-1]+indel, matrix[i-1][j-1]+mate, 0]
            matrix[i][j] = max(scores)
            backtrack[i][j] = scores.index(matrix[i][j])
            
            if matrix[i][j] > maxScore:
               maxScore, maxI, maxJ = matrix[i][j], i, j
    
    #insert indel via lambda function
    insertIndel = lambda seq, i:seq[:i] + '-' + seq[i:]
       
    #get position with highest score
    i,j = np.unravel_index(matrix.argmax(), matrix.shape)
    maxScore = str(matrix[i][j])
            
    #align strings up to position of high score
    vAligned, wAligned = v[:i], w[:j]

    #Backtrack to start of matrix alignment starting at highest scoring cell
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            wAligned = insertIndel(wAligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            vAligned = insertIndel(vAligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1
            
    #Cut strings at end of backtrack
    vAligned = vAligned[i:]
    wAligned = wAligned[j:]
    
    return maxScore, vAligned, wAligned
    
from numpy import unravel_index, zeros
import numpy as np
import argparse 
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('seq_file',help="input FASTA file")
parser.add_argument('-m','--match',required=True,help="match score")
parser.add_argument('-s','--mismatch',required=True,help="mismatch penalty")
parser.add_argument('-d','--indel',required=True,help="indel penalty")
args = parser.parse_args()
file = args.seq_file
match = int(args.match)
mismatch = int(args.mismatch)
indel = int(args.indel)

input = open(file).read().split('>')[1:]
v = input[0].splitlines()[1]
w = input[1].splitlines()[1]
    
alignment = localAlignment(v, w, match, mismatch, indel)
print '\n'.join(alignment)
