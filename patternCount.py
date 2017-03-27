"""
The number of times a kmer pattern appears as a substring of text
"""
def patternCount(v,w):
    count = 0
    for i in xrange (len(v)-len(w)+1):
        if v[i:i+len(w)] == w:
            count = count+1
    return count
    
with open ('DNAStrings.txt') as input:
    text = input.readline()
    pattern = input.readline()
    
print patternCount(text,pattern)