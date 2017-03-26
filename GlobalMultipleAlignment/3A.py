import sys,random
import matplotlib.pyplot as plt
import numpy

def localAlignment(v, w, match, mismatch, indel):
    
    #initialize matrices
    matrix = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
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
    #i,j = np.unravel_index(matrix.argmax(), matrix.shape)
    #maxScore = str(matrix[i][j])
            
    #align strings up to position of high score
    vAligned, wAligned = v[:maxI], w[:maxJ]

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
    
    return (vAligned,wAligned)

def randomDNA(sizeOfSeq):
    DNA = ''
    for x in xrange(sizeOfSeq):
        DNA += random.choice('ACGT')
    return DNA
    
# set up inputs
seqs = open(sys.argv[1]).readlines()[:-1]
seqs = [seq.strip() for seq in seqs]
penalty = [-30, -20, -10, -1, -0.5, -0.33, -0.25, 0]
error = []
LPN = []


for p in penalty:  
    # compute lengths of alignments
    lengths = []
    for i in range (0, len(seqs), 2): 
        alignment = localAlignment(seqs[i], seqs[i+1], 1, p, p)
        lengths.append(len(alignment[0]))
        
    # get averages
    LPN.append(numpy.mean(lengths))
    
    # get standard deviations
    error.append(numpy.std(lengths))
    
# do scatter plot
plt.errorbar(penalty,LPN,yerr=error,label='L_P(1000)')
plt.legend(loc='upper left')
plt.xlabel('Mismatch=Indel=p')
plt.ylabel('L_P(1000)')
plt.show()
