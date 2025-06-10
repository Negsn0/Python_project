N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append(A.index(i+1)+1)
print(*B)