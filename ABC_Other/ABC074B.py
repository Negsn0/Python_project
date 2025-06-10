N = int(input())
K = int(input())
X = list(map(int, input().split()))

total = 0

for i in range(N):
    if X[i] < K - X[i]:
        total += 2 * X[i]
#        print("a")
    else:
        total += 2 * (K - X[i])
#        print("b")

print(total)