import numpy as np
X,Y = map(int,input().split())
A = np.zeros((6,6))
for i in range(1,7):
    for j in range(1,7):
        A[i,j]=(i,j)

print(A)