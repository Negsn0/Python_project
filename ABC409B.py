N = int(input())
A = list(map(int, input().split()))

A_max = max(A)

k = 0
count = N

for n in range(1,A_max+1):
    count_n = A.count(n-1)
    count -= count_n
    if count >= n:
        k = n
    elif count < n:
        break

print(k)