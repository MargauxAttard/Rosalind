def frequentKmer (text, k): 
    kmer = dict()
    for i in xrange (len(text)-k+1):
        if text[i:i+k] in kmer:
            kmer[text[i:i+k]] += 1
        else: 
            kmer[text[i:i+k]] = 1 
    return kmer


         
with open ('input.txt') as input: 
    dna, k = [line.strip() for line in input.readlines()]
    k = int(k)
    
kmers = frequentKmer(dna,k)
longestKmer = [text[0] for text in kmers.items() if text[1] == max(kmers.values())]
print ' '.join(longestKmer)