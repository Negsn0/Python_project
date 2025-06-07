A,B = map(int, input().split())
count = 0
p = 1
while True:
    if p >= B:
        print(count)
        exit()
    
    p += A - 1
    count += 1