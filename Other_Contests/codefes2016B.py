N, A, B = map(int, input().split())
S = list(input())

AB = A + B

count = 0
countA = 0
countB = 0

for i in range(N):
    k = S[i]
    if k == 'a' and count < AB :
        print("Yes")
        countA += 1
    elif k == 'b' and countB < B and count < AB:
        print("Yes")
        countB += 1
    else:
        print("No")
    count = countA + countB


