N = int(input())
d = list(map(int, input().split()))

mid = N // 2
d.sort()
Knum = d[N//2] - d[N//2 - 1]

print(Knum)