import random
import sys

def randomDNA(sizeOfSeq):
    DNA = ''
    for x in xrange(sizeOfSeq):
        DNA += random.choice('ACGT')
    return DNA

def calcFreq(seqs):
    A, T, C, G = 0, 0, 0, 0
    freq = list()
    for seq in seqs:
        for c in seq:
            if c == 'A':
                A +=1
            if c == 'T':
                T +=1
            if c == 'G':
                G += 1
            if c == 'C':
                C += 1
    total = A + T + G + C
    freq.append(['A', (float(A)/total)])
    freq.append(['T', (float(T) / total)])
    freq.append(['G', (float(G) / total)])
    freq.append(['C', (float(C) / total)])
    return freq

numberOfSeq = int(sys.argv[1])
sizeOfSeq = int(sys.argv[2])

#generate 500 random sequences 
results = []
for x in xrange(int(numberOfSeq)*2):
    results.append(randomDNA(int(sizeOfSeq)))
print '\n'.join(results)
print calcFreq(results)
