N = int(input())
A = list(map(int, input().split()))

A_max = max(A)

k = 0
count = N

for n in range(1,A_max):
    count_n = A.count(n)
    count -= count_n
    if count >= n:
        k = n
    elif count < n:
        break

print(n)