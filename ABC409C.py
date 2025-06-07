N , L = map(int, input().split())

d = list(map(int, input().split()))

for n in range(1,len(d)):
    d[n] = ( d[n-1] + d[n] ) % L
