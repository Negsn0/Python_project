import numpy as np
N, M, C = map(int, input().split())
B = list(map(int, input().split()))

A = [list(map(int, input().split())) for i in range(N)]

count = 0


for j in range(N):
    s = 0
    for k in range(M):
        s += A[j][k]*B[k]
    if s > -C:
        count += 1

print(count)