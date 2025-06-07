N,D=map(int, input().split())
A = list(map(int, input()))

AA = set(A)

count = len(A) - len(AA)

A = list(AA)

while True:
    for i in range(A - 1):
        if abs(A[i]-A[i+1]) == D:
            count +=1
            A.pop(i)

print(count)
