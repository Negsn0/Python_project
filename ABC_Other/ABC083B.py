N,A,B=input().split() # int処理せずにいれるのは効率が悪い
tot = 0
A = int(A)
B = int(B)
for i in range(int(N) + 1):
    digits = [int(num) for num in str(i)]
    sum_d = sum(digits)
    if A <= sum_d <= B:
        tot += i
print(tot)