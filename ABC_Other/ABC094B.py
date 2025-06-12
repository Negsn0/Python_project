N , M , X = map(int, input().split())

A = list(map(int, input().split()))

num = 0

for i in range(M):
    if A[i] < X and A[i+1] > X:
        num = i + 1
    #ここはOK
    elif A[0] > X or A[M-1] < X:
        print(0)
        exit()

if M - num < num:
    print(M-num)
    exit()
print(num)
