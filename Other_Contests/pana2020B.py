##解けなかった

H, W = map(int, input().split())

if H % 2 == 0:
    count = (W * H // 2)
elif H % 2 == 1:
    if W % 2 == 0:
        count = H * W // 2
    elif W % 2 == 1:
        count = ((W + 1) // 2) * ((H + 1) // 2) + ((W - 1) // 2) * ((H - 1) // 2)
####ここの部分、つまり横一列or縦一列の場合は斜めに動けないからこれの分の場合分けが必要。
if W == 1 or H == 1:
    count = 1
print(count)