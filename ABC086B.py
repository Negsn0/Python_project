a , b = input().split()

ab = int(a+b)

for i in range(1,ab//2):
    if i * i == ab:
        print("Yes")
        exit()
print("No")