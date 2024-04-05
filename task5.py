size = int(input())
k = int(input())
matrix = []
for i in range(size):
    a = []
    for j in range(size):
        a.append(int(input()))
    matrix.append(a)

count = 0
for i in range(size):
    for j in range(size):
        if matrix[i][j] % 10 == k:
            count += matrix[i][j]

print(count)