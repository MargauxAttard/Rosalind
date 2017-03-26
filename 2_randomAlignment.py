import sys,random
import matplotlib.pyplot as plt
import numpy as np
from numpy import unravel_index, zeros

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

def randomDNA(sizeOfSeq):
    DNA = ''
    for x in xrange(sizeOfSeq):
        DNA += random.choice('ACGT')
    return DNA

# set up inputs
seqs = open(sys.argv[1]).readlines()[:-1]
seqs = [seq.strip() for seq in seqs]
P1 = [1,-30,0]
P2 = [1,-30,-20]

# compute P1 alignments
P1lengths = []
print "P1 ALIGNMENTS:"
for i in range (0,len(seqs),2):
    alignment = localAlignment(seqs[i], seqs[i+1], P1[0], P1[1], P1[2])
    print alignment[0]
    print alignment[1]
    print alignment[2]
    print ""
    P1lengths.append(len(alignment[0]))
print ""

# compute P2 lengths
P2lengths = []
print "P2 ALIGNMENTS:"
for i in range (0,len(seqs),2):
    alignment = localAlignment(seqs[i], seqs[i+1], P2[0], P2[1], P2[2])
    print alignment[0]
    print alignment[1]
    print alignment[2]
    print ""
    P2lengths.append(len(alignment[0]))
"""
# do P1 histogram
plt.hist(P1lengths)
plt.title('P1 Alignment Lengths, n = 1000')
plt.xlabel('L_P1(1000)')
plt.ylabel('Frequency')
plt.show()

# do P2 histogram
plt.hist(P2lengths)
plt.title('P2 Alignment Lengths, n = 1000')
plt.xlabel('L_P2(1000)')
plt.ylabel('Frequency')
plt.show()
"""
N = [50,100,200,500]
LP1 = []
eP1 = []
LP2 = []
eP2 = []

for n in N:
    # generate random sequences
    seqs = []
    for seq in xrange(200): 
        seqs.append(randomDNA(n))
        
    # compute lengths of alignments
    lengthsP1 = []
    lengthsP2 = []
    for i in range (0, len(seqs), 2): 
        alignment = localAlignment(seqs[i], seqs[i+1], P1[0], P1[1], P1[2])
        lengthsP1.append(len(alignment[0]))
        alignment = localAlignment(seqs[i], seqs[i+1], P2[0], P2[1], P2[2])
        lengthsP2.append(len(alignment[0]))
        
    # get averages
    LP1.append(np.mean(lengthsP1))
    LP2.append(np.mean(lengthsP2))
    
    # get standard deviations
    eP1.append(np.std(lengthsP1))
    eP2.append(np.std(lengthsP2))

# add the one we've already done (n = 1000)
N.append(1000)
LP1.append(np.mean(P1lengths))
LP2.append(np.mean(P2lengths))
eP1.append(np.std(P1lengths))
eP2.append(np.std(P2lengths))

# do scatter plot
plt.errorbar(N,LP1,yerr=eP1,label='L_P1(n)')
plt.errorbar(N,LP2,yerr=eP2,label='L_P2(n)')
plt.legend(loc='upper left')
plt.xlabel('n')
plt.ylabel('LP(n)')
plt.show()