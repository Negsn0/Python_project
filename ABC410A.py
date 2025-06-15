N = int(input())

A = list(map(int, input().split()))

K = int(input())
count = 0

for i in range(N):
    if K <= A[i] :
        count += 1

print(count)