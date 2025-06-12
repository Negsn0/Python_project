temp = int(input())
a = set()
a.add(temp)
temp1 = 0
i = 1
while True:
    if temp % 2 == 0:
        temp = temp // 2
    else:
        temp = 3 * temp + 1
    temp1 = len(a)
    a.add(temp)
    i += 1
    if temp1 == len(a):
        print(i)
        exit()
