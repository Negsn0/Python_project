N, Q = map(int, input().split())
A = [i + 1 for i in range(N)]
#敗北
# for i in range(Q):
#     list_t = list(map(int,input().split()))
#     if list_t[0] == 1 :
#         A[list_t[1] - 1] = list_t[2]
#     elif list_t[0] == 2:
#         print(A[list_t[1] - 1])
#     elif list_t[0] == 3:
#         l1 = list_t[1] % N
#         temp = []
#         for j in range(l1):
#             temp.append(A[j])
#         for j in range(N - l1):
#             A[j] = A[j+l1]
#         A =A[:-l1]
#         A += temp
#         # for j in range(list_t[1]):
#         #     a0 = A[0]
#         #     for k in range(N-1):
#         #         A[k]=A[k+1]
#         #     A[N-1]= a0
head = 0
for i in range(Q):
    list_t = list(map(int,input().split()))
    if list_t[0] == 1:
        A[(list_t[1] + head ) % N - 1 ] = list_t[2]
    elif list_t[0] == 2:
        print(A[(list_t[1] + head ) % N - 1])
    elif list_t[0] == 3:
        head = (head + list_t[1]) % N