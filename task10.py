n = int(input())

for i in range(1, n+1):
    natizhe = 2 ** i
    if natizhe <= n:
        print(natizhe)
