A = []
for i in range(3):
    A += list(map(int, input().split()))
N = int(input())
B = []
for n in range(N):
    k = int(input())
    if k in A:
        B.append(A.index(k))

conditions = [
[0,1,2],
[3,4,5],
[6,7,8],
[0,3,6],
[1,4,7],
[2,5,8],
[0,4,8],
[2,4,6]]

for i in range(8):
    if all(cond in B for cond in conditions[i]):
        print("Yes")
        exit()

print("No")