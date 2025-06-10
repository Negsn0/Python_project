##TLEコーナー
N , K = map(int, input().split())

minimum = N

while True:
    temp = abs(minimum - K)
    if temp < minimum:
        minimum = temp
    else:
        print(minimum)
        exit()

## GPTコーナー
### N , Kがあったときに, 収束地点をZとしたら、NからZまで移動するときの回数が繰り返し回数で、あまりを考えるとよい。
N, K = map(int, input().split())

if K == 0:
    print(N)
else:
    r = N % K
    print(min(r, abs(r - K)))
