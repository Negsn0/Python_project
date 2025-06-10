K, N = map(int, input().split())
A = list(map(int, input().split()))

flag = 1
dis = K - A[N-1] + A[0]

for i in range(N-1):
    if dis < A[i+1] - A[i]:
        dis = A[i+1] - A[i]
        flag = i + 1

print(K - dis)