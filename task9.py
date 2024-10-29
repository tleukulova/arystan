n = int(input())
array = []

for i in range (1, n+1):
    element = int(input())
    array.append(element)
    
zhup = 0
taq = 0

for i in range (1, len(array)):
    if array[i] % 2 == 0:
        zhup += 1
    else:
        taq += 1
        
print(zhup, " ", taq)
