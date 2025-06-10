N = int(input())

for i in range(11):
    if N < 2 ** i:
        print(2**(i-1))
        exit()
    elif N == 2 ** i:
        print(2 ** i)
        exit()
