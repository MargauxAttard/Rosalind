import sys
import numpy
import string
import random
import matplotlib.pyplot as plt


A = [];
C = [];
D = [];
E = [];
F = [];
G = [];
H = []
I = [];
K = [];
L = [];
M = [];
N = [];
P = [];
Q = []
R = [];
S = [];
T = []
V = []
W = []
Y = []


def computestats(familymember):
    members = []


    A.append('A'); C.append('C'); D.append('D');
    E.append('E'); F.append('F'); G.append('G'); H.append('H');
    I.append('I'); K.append('K'); L.append('L');
    M.append('M');N.append('N'); P.append('P');
    Q.append('Q'); R.append('R'); S.append('S'); T.append('T');
    V.append('V');W.append('W'); Y.append('Y');

    for mem in familymember:
        members.append(mem)
        length = 20

    #print 'Member', members

    for words in xrange(length):
        num_A = members[words].count('A'); A.append(float(num_A) / length)
        num_C = members[words].count('C'); C.append(float(num_C) / length)
        num_D = members[words].count('D'); D.append(float(num_D) / length)
        num_E = members[words].count('E'); E.append(float(num_E) / length)
        num_F = members[words].count('F'); F.append(float(num_F) / length)
        num_G = members[words].count('G'); G.append(float(num_G) / length)
        num_H = members[words].count('H'); H.append(float(num_H) / length)
        num_I = members[words].count('I'); I.append(float(num_I) / length)
        num_K = members[words].count('K'); K.append(float(num_K) / length)
        num_L = members[words].count('L'); L.append(float(num_L) / length)
        num_M = members[words].count('M'); M.append(float(num_M) / length)
        num_N = members[words].count('N'); N.append(float(num_N) / length)
        num_P = members[words].count('P'); P.append(float(num_P) / length)
        num_Q = members[words].count('Q'); Q.append(float(num_Q) / length)
        num_R = members[words].count('R'); R.append(float(num_R) / length)
        num_S = members[words].count('S'); S.append(float(num_S) / length)
        num_T = members[words].count('T'); T.append(float(num_T) / length)
        num_V = members[words].count('V'); V.append(float(num_V) / length)
        num_W = members[words].count('W'); W.append(float(num_W) / length)
        num_Y = members[words].count('Y'); Y.append(float(num_Y) / length)

    # profile = numpy.row_stack([A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W])
    profile = list([A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W])

    print A ; print C; print D; print E;  print F; print G; print H; print I
    print K; print L;print M; print N;  print P; print Q; print R
    print S; print T;  print V; print W;  print Y;

    #print "Matrix:", profile
    return profile

def split_nmers(database):
    m = 20
    n_mers = [database[i:i+m] for i in xrange(len(database)-(m-1))]
    return n_mers


def compute_score(nMers, profile):
    # column score = sum of:
    # (prob in profile for letter)* s(letter in profile,letter in scoring)
    # threshold = (random - smallest) /2
    column_scores = []
    homolog_scores = []
    match= 2
    mismatch = -1
    for nMer in nMers:
        column_score = 0.0
        for i in range(len(nMer)):
            for x in range(len(profile)):
                if nMer[i] is profile[x][0]:
                    column_score += profile[x][i+1] * match
                else:
                    column_score += profile[x][i+1] * mismatch
            column_scores.append(column_score)
        #print "c-scores for:", nMer , column_score
        homolog_score = 0.0
        for score in column_scores:
            homolog_score += score
        homolog_scores.append([nMer,int(homolog_score)])
        column_scores = []
    homolog_scores = sorted(homolog_scores, key=lambda score: score[1])
    for homolog in homolog_scores:
        print homolog
    return homolog_scores


def make_scoreMatrix(scoringMatrix):
    matrix = numpy.loadtxt(scoringMatrix)
    return matrix

def randomizer():
    random_string = ''
    for i in range(20):
        random_string += random.choice("ACDEFGHIKLMNPQRSTVWY")
    return random_string

def true_homolog(scores, random_score):
    true_homo = []
    total = []
    pVal = []
    for score in scores:
        if score <= random_score:
            true_homo.append(score)
    return true_homo
    #return total
        #elif score > random_score: 
         #   true_homo.append(score)
    #pVal: (number of scores in random scores greater than or equal to score S/ total number of random scores)
    #how often you get the same score as your best match in the database
    #print true_homo
    


if __name__ == '__main__':
    family1 = open('Family2.txt')
    family_members = family1.read()
    member = family_members.split('\n')

    new_member = zip(*member)
    str1=map(''.join, new_member)

    number_members = len(str1)

    profile_matrix = computestats(str1)


    database = open('database.txt')
    db = database.read()


    nMers = split_nmers(db)
    #print "nMers:", nMers


    score_m = open('Matrix.txt', 'rb')
    matrix = [row.strip().split() for row in score_m]

    #print matrix


    homologs = compute_score(nMers, profile_matrix)
    test = []
    for homo in homologs:
        test.append(homo[1])

    #r_score = random_score[0][1]
    
    
    r = []
    random1 = randomizer()
    r1 = [random1]
    random_score1 = compute_score (r1, profile_matrix)
    r.append(random_score1)
    random2 = randomizer()
    r2 = [random2]
    random_score2 = compute_score (r2, profile_matrix)
    r.append(random_score2)
    random3 = randomizer()
    r3 = [random3]
    random_score3 = compute_score (r3, profile_matrix)
    r.append(random_score3)
    random4 = randomizer()
    r4 = [random4]
    random_score4 = compute_score (r4, profile_matrix)
    r.append(random_score4)
    random5 = randomizer()
    r5 = [random5]
    random_score5 = compute_score (r5, profile_matrix)
    r.append(random_score5)
    random6 = randomizer()
    r6 = [random6]
    random_score6 = compute_score (r6, profile_matrix)
    r.append(random_score6)
    random7 = randomizer()
    r7 = [random7]
    random_score7 = compute_score (r7, profile_matrix)
    r.append(random_score7)
    random8 = randomizer()
    r8 = [random8]
    random_score8 = compute_score (r8, profile_matrix)
    r.append(random_score8)
    random9 = randomizer()
    r9 = [random9]
    random_score9 = compute_score (r9, profile_matrix)
    r.append(random_score9)
    random10 = randomizer()
    r10 = [random10]
    random_score10 = compute_score (r10, profile_matrix)
    r.append(random_score10)
    print "List of random scores: ", r
    #r = [-174, -172, -164, -182, -177, -186, -174, -182, -171, -192]
    r = [-8156, -8657, -8662, -6349, -8661, -8662, -8653, -6565, -8273, -6960]
    avgRandom = numpy.mean(r)
    r_score = int(avgRandom)
    true = true_homolog(test, r_score)
    #print 'True homologs: ', true
    #print "Average random score is: ",  avgRandom
    bestMatch = max(true)
    #print bestMatch
    pValList = []
    for h in homologs: 
        for rs in r:
            #print "Random score less than homolog score: ", rs
            #print "Homolog score: ", h[1]
            if int(rs) >= int(h[1]): 
                #print "Random score greater than homolog score:", rs
                #print "Homolog score less than random", h[1]
                pValList.append(rs)
            pVal = len(pValList)/1000
            if pVal == 0: 
                pVal = "Nearly 0" 
        print "Homolog:",h[0], " Homolog Score:" , h[1], " P-value:", pVal
        
    plt.hist(true, bins = 30)
    plt.xlabel("Score")
    plt.ylabel("Number Of Homologs")
    plt.show()
  
    plt.hist(homologs, bins = 30)
    plt.xlabel('Score')
    plt.ylabel('Number of Homologs')
    plt.show()

