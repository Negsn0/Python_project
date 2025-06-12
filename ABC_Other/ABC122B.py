S = list(input())

count = 0
tmp = 0
for i in range(len(S)):
    if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
        tmp += 1
        if tmp > count:
            count = tmp
    else:
        tmp = 0

print(count)