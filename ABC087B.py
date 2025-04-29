A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

# 500円の枚数
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            Y = 500 * i + 100 * j + 50 * k
            if(Y == X):
                count +=1
print(count)