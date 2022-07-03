#Program to transpose the matrix

S = [[2,7],[4,5],[3,8]]
P = [[0,0,0],[0,0,0]]
for i in range (len(S)):
    for j in range (len(S[0])):
        P[j][i]=S[i][j]
        for w in S:
            print(w)