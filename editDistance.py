def editDistance(string1, string2):
    from numpy import zeros

    Matrix = zeros((len(string1)+1,len(string2)+1), dtype=int)
    for i in range(1,len(string1)+1):
        Matrix[i][0] = i
    for j in range(1,len(string2)+1):
        Matrix[0][j] = j

    #Get Matrix entries
    for i in xrange(1,len(string1)+1):
        for j in xrange(1,len(string2)+1):
            if string1[i-1] == string2[j-1]:
                Matrix[i][j] = Matrix[i-1][j-1]
            else:
                Matrix[i][j] = min(Matrix[i-1][j]+1, Matrix[i][j-1]+1, Matrix[i-1][j-1]+1)
    return Matrix[len(string1)][len(string2)]

with open('in.txt') as input:
    string1, string2 = [line.strip() for line in input.readlines()]

#get distances
distance = editDistance(string1, string2)
print str(distance)