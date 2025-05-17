N,K = map(int, input().split())

A = list(map(int, input().split()))

p = 1

for i in range(N):
    p = A[i] * p
    if len(str(p)) > K:
        p = 1

print(p)