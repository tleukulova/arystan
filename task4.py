array = [141, 605, 786, 177, 989, 666, 909,545,100, 101]
for i in range(len(array)):
    if array[i] % 10 == array[i] // 100:
        print(array[i])