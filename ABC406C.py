N = int(input())

P = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(4,N-i+1):
        A = P[i:j+i]
        count1 = 0
        count2 = 0
        for k in range(j-2):
            if A[k]<A[k+1] and A[k+1]>A[k+2]:
                count1 += 1
            elif A[k]>A[k+1] and A[k+1]<A[k+2]:
                count2 += 1
        if count1 == 1 and count2 == 1 and A[0]<A[2]:
            count = 1 + count

print(count)