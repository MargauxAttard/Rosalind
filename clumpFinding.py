"""
Given integers L and t, a string Pattern forms an (L,t)-clump inside a larger string Genome
If there is an interval of Genome of length L in which Pattern appears at least t times

Given: a string Genome and integers k, L, and t
Return: all distinct k-mers forming (L, t)-clumps in Genome
"""

""" Checks that a given set of t kmers falls within a clump of size L """
def clumpLength(kmr, t, L):
    for i in xrange (len(kmr)-t+1):
        if kmr[t+i-1] - kmr[i] <= L: 
            return True
    return False
    
with open ('input.txt') as input: 
    genome, [k, L, t] = [line.strip() if index==0 else map(int, line.strip().split()) for index, line in enumerate(input.readlines())]
    
#find kmers, count number of appearances, store indicies
kmers = dict()
for i in xrange(len(genome)-k+1):
    if genome[i:i+k] in kmers:
        kmers[genome[i:i+k]][0] += 1
        kmers[genome[i:i+k]][1].append(i)
    else:
        kmers[genome[i:i+k]] = [1, [i]]
        
#narrow down to kmers that occur at least t times
tKmers = [[allKmers[0], allKmers[1][1]] for allKmers in kmers.items() if allKmers[1][0] >= t]

#narrow down to interval L
kmerClumps = []
for tKmer in tKmers: 
    if clumpLength(tKmer[1], t, L):
        kmerClumps.append(tKmer[0])
        
#print solution
print ' '.join(kmerClumps)
       