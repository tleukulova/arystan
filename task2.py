def myfunction(matrix):
    s = [sum(row) for row in matrix]
    #index of maximum sum in each row
    index = s.index(max(s))
    del matrix[index]
    return matrix

n = int(input())
matrix = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

new_matrix = myfunction(matrix)
for e in new_matrix:
    print(e)

    