n = input()
arr = list(map(int, input().split()))

count = 0

while True:
    if all(x % 2 == 0 for x in arr):
        count +=1
        arr = [x//2 for x in arr]
    else:
        break

print(count)