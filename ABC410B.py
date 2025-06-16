N , Q = map(int, input().split())
X = list(map(int, input().split()))

B = []
C = [0 for i in range(N)]


for i in range(Q):
    if X[i] > 0:
        B.append(X[i])
        C[X[i] - 1] += 1
    else:
        CC = C[0]
        temp = 0
        for k in range(1,N):
            if CC > C[k]:
                CC = C[k]
                temp = k
        B.append(temp + 1)
        C[ temp ] += 1
print(*B)