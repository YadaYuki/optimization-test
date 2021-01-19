pi = [1,0]
P = [[0.9,0.1],[0.2,0.8]]
b = {"A":[0.8,0.3],"B":[0.2,0.7]}
E = 1
output = input("Output is :")

probability_mat = [[0 for i in range(len(pi))] for i in range(len(output))]

probability_mat[0][0] = P[0][0] * b[output[0]][0]
probability_mat[0][1] = P[0][1] * b[output[0]][1]

for i in range(1,len(output)):
    for j in range(len(pi)):
        for k in range(len(pi)):
            probability_mat[i][j] += probability_mat[i-1][k] * P[k][j] * b[output[i]][j]
            
print(probability_mat)
