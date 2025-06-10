## 解けなかった

A, B, C = map(int, input().split())
count = 0
if A == B and A == C and A%2==0:
    print(-1)
    exit()
if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
    print(0)
    exit()
while True :
    A1 = (B + C) / 2
    B1 = (A + C) / 2
    C1 = (A + B) / 2
    A = A1
    B = B1
    C = C1
    count += 1
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        print(count)
        exit()