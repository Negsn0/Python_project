N = int(input())
arr = list(map(int, input().split()))

sum_A = 0
sum_B = 0

sort_arr = sorted(arr,reverse = True)

for i in range(N):
    if i % 2 == 0:
        sum_A += sort_arr[i]
    else:
        sum_B += sort_arr[i]

print(sum_A - sum_B)