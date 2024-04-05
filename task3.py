array = [21,26,46,87,41,5,16,10,15,3,8,70]
count = 0
for i in range(len(array)):
    if i%2 == 0:
        if array[i-1] % 2 != 0:
            count += array[i-1]
print(array)
print(count)