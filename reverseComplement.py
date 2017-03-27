def reverseComplement (pattern): 
    strand = []
    for i in xrange (len(pattern)):
        if pattern[i] == 'A': 
            strand.append('T')
        elif pattern[i] == 'T':
            strand.append('A')
        elif pattern[i] == 'C':
            strand.append('G')
        elif pattern[i] == 'G': 
            strand.append('C')
    
    s = strand[::-1]
    return ''.join(s)
    
    
with open ('input.txt') as input: 
    dna = input.readline()
    
print reverseComplement(dna)