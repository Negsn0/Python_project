A, B, C = map(int, input().split())
count = 0

if A == B == C and A % 2 == 0:
    print(-1)
    exit()

while True:
    if A % 2 or B % 2 or C % 2:
        print(count)
        break
    a, b, c = A, B, C
    A = (b + c) // 2
    B = (a + c) // 2
    C = (a + b) // 2
    if (A, B, C) == (a, b, c):
        print(-1)
        break
    count += 1
