#Жол санын енгіземіз
row = int(input())
#Баған санын енгіземіз
column = int(input())

#Екіөлшемді массивке элементтерін енгіземіз
matrix = []
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)

count_even = 0
for i in range(row):
    for j in range(column):
        if matrix[i][j] % 2 == 0:
            count_even += 1

print(count_even)
