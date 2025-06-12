N = int(input())
v = list(map(int, input().split()))
v.sort()
v[0]= (0.5**(N-1))*v[0]
for i in range(1,N):
    v[i] = (0.5**(N-i))*v[i]

print(sum(v))