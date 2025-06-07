# 時間かかりすぎ
N,K = map(int, input().split())
A_i = 0
a = []
if N < K:
    print(1)
    exit()
for i in range(K):
    a.append(1)
for i in range(K,N+1): #個々の部分忘れてた。
    A_i = sum(a)
    a.pop(0)
    a.append(A_i)
print(A_i%(10**9))

# N, K = map(int, input().split())
# MOD = 10**9

# if N < K:
#     print(1)
#     exit()

# a = [1] * K
# total = sum(a) % MOD

# for i in range(K, N+1):
#     a.append(total)
#     total = (total * 2 - a[i-K]) % MOD

# print(a[N])
