import math

A,B=map(int,input().split())

N=math.floor(A/B)

if A/B - N > 0.5:
    print(N+1)
else:
    print(N)