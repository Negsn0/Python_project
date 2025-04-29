N,Y= map(int, input().split())

for x in range(N + 1):
    if 10000 * x > Y:
        break
    for y in range(N + 1 - x):
        if 10000 * x + 5000 * y> Y:
            break
        z = N - x - y
        tot = 10000 * x + 5000 * y + 1000 * z
        if Y == tot:
            print(x,y,z)
            exit()

print("-1 -1 -1")

