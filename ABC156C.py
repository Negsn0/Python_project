N = int(input())
X = list(map(int, input().split()))

result_comp = 100000000000000000

for P in range(100):
    result = sum([(x - P)**2 for x in X])
    if result_comp > result:
        result_comp = result

print(result_comp)