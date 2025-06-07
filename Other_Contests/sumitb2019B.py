N = int(input())

s = int(N/1.08)

if int(s * 1.08) == N:
    print(s)
elif int((s + 1) * 1.08) == N:
    print(s+1)
else:
    print(":(")