from numpy import unravel_index, zeros
import numpy as np

def initializeScore (score):
    row, column = score.shape
    for i in range(row):
        score[i,0] = -i*indel
    for j in range(column):
        score[0,j] = -j*indel
        
def globalAlignment(v,w):
    #initialize
    vLength = len(v)
    wLength = len(w)
    score = np.zeros([vLength+1, wLength+1])
    initializeScore(score)
    backtrack = np.zeros([vLength+1, wLength+1])
    
    #Fill in score and backtrack matrices
    for i in range(1, 1+vLength):
        for j in range(1, 1+wLength):
            mate = match
            if v[i-1] != w[j-1]:
                mate = mismatch
            scores = [score[i-1][j]+indel, score[i][j-1]+indel, score[i-1][j-1]+mate]
            score[i][j] = max(scores)
            #scores = [score[i-1,j]-indel, score[i][j-1]-indel, score[i-1][j-1] + matrix[v[i-1],w[j-1]]]
            #score[i,j] = max(scores)
            backtrack[i][j] = scores.index(score[i][j])    
    
    #insert indel penalties
    insertIndel = lambda indel, i: indel[:i] + '-' + indel[i:]
    
    #aligned strings as input strings
    vAligned, wAligned = v, w
    
    #position of highest scoring cell
    i,j = len(v), len(w)
    maxScore = str(score[i][j])
    
    #backtrack
    while i*j != 0: 
        if backtrack[i][j] == 0:
            i -= 1
            wAligned = insertIndel(wAligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            vAligned = insertIndel(vAligned, i)
        else: 
            i -= 1
            j -= 1
    for repeat in xrange(i):
        wAligned = insertIndel(wAligned, 0)
    for repeat in xrange(j):
        vAligned = insertIndel(vAligned, 0)
        
    return maxScore, vAligned, wAligned
 
def localAlignment(v, w):
    
    #initialize matrices
    matrix = [[0.0 for i in range(len(v)+1)] for j in range(2)]
    maxScore, maxI, maxJ = -1, 0, 0
    
    #fill in score and backtrack
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            i1 = (i-1)%2
            i2 = i%2
            mate = match
            if v[i-1] != w[j-1]:
                mate = mismatch
            scores = [matrix[i1][j]+indel, matrix[i2][j-1]+indel, matrix[i1][j-1]+mate, 0]
            matrix[i2][j] = max(scores)
            
            if matrix[i2][j] > maxScore:
               maxScore, maxI, maxJ = matrix[i2][j], i, j
    
    vPrefix = v[0:maxI][::-1]
    wPrefix = w[0:maxJ][::-1]

    matrixP = [[0.0 for i in range(len(v)+1)] for j in range(2)]
    maxScoreP, maxIP, maxJP = -1, 0, 0
    
    #fill in score and backtrack
    for i in xrange(1, len(vPrefix)+1):
        for j in xrange(1, len(wPrefix)+1):
            i1 = (i-1)%2
            i2 = i%2
            mate = match
            if vPrefix[i-1] != wPrefix[j-1]:
                mate = mismatch
            scoresP = [matrixP[i1][j]+indel, matrixP[i2][j-1]+indel, matrixP[i1][j-1]+mate, 0]
            matrixP[i2][j] = max(scoresP)
            
            if matrixP[i2][j] > maxScoreP:
               maxScoreP, maxIP, maxJP = matrixP[i2][j], i, j
    
    vSub = vPrefix[0:maxIP][::-1]
    wSub = wPrefix[0:maxJP][::-1]   
    
    GA = globalAlignment(vSub, wSub)
    return GA

match = 1
mismatch = -10
indel = -1
#seq1 = 'ACGGT'
#seq2 = 'GCGTT'

with open ('p4seqs.txt') as input: 
    v = input.readline()
    w = input.readline()
 
alignment = localAlignment(v, w)
print '\n'.join(alignment)
