def patternMatching (dna, kmer): 
    locus = []
    for i in xrange(len(dna)-len(kmer)+1):
        if dna[i:i+len(kmer)] == kmer:
            locus.append(str(i))
            
    return ' '.join(locus)
    
with open ('input.txt') as input: 
    pattern, text = [line.strip() for line in input.readlines()]
    
print patternMatching (text, pattern)