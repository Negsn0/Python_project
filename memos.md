# AtCoder 備忘録

## 1. 基本的な入出力

```Python
# 入力
input()  # 基本的な入力
N = int(input())  # 数値の入力
A = list(map(int, input().split()))  # スペース区切りの数値配列の入力
```

## 2. 配列操作

### 配列の種類と基本操作

```Python
# 配列の種類
list()  # 配列(順序有り、重複あり)
set()   # 集合(順序なし、重複なし)

# 要素の追加・削除
S.append(A)     # Sの後ろにAを追加(stringなら'')
S = S[:-7]      # Sの後ろから7つを削除
S.pop(3)        # SのS[3]を削除

# 配列の操作
max(A)          # 配列Aの最大値を取得
A.count(n)      # 配列Aの中の要素nの出現回数をカウント
A = P[i:j+i]    # 配列Pのi番目からj+i-1番目までの要素を取得

# 配列の変換と処理
a = [x * 2 for x in a]  # 内包表記：配列の各要素を2倍に
map(f, a)  # 配列a全部に関数fを作用させる(戻り値はmap型なのでlistやsetで回収)
```

## 3. 文字列と数値操作

### 文字列操作

```Python
# 文字列のカウント
s = input()
count = s.count('A')  # sの中の文字Aをカウント

# 数値から文字列への変換
i = 1234321
digits = [int(num) for num in str(i)]  # 数値を文字列に変換し、各桁を配列に格納
```

### 数値演算

```Python
# 基本的な演算
(a + b) % L  # 剰余演算。Lで割った余りを取得
s = int(N/1.08)  # 除算して小数点以下を切り捨て

# 累積計算
count = countA + countB  # 複数のカウンターの合計

# 最小値の探索
result_comp = 100000000000000000  # 十分大きな初期値
if result_comp > result:
    result_comp = result  # より小さい値で更新

# 二乗和の計算
sum([(x - P)**2 for x in X])  # 配列の各要素とPの差の二乗和
```

## 4. 制御構造

### ループ処理

```Python
# for文
for n in range(1, len(d)):     # 1から配列の長さ-1までループ
for n in range(1, A_max+1):    # 1からA_maxまでループ

# while文
while True:
    if 条件:
        print(結果)
        exit()  # プログラムを終了
```

### 条件分岐

```Python
# 条件分岐
if A[k]<A[k+1] and A[k+1]>A[k+2]:    # 複数の条件をandで結合
elif A[k]>A[k+1] and A[k+1]<A[k+2]:  # else ifの条件分岐

# インクリメントとデクリメント
count += 1  # カウントを1増やす
p += A - 1  # pに(A-1)を加算
```

## 5. ライブラリ操作

### NumPy

```Python
import numpy as np
np.zeros((6,6))  # 6x6のゼロ行列を作成
A[i,j] = (i,j)   # 行列の要素に値を代入
```

## 6. アルゴリズム

### 累積和

```Python
sum = 0
a = []  # a は1 ~ 10000までの数字の配列
for i in range(10000):
    a.append(i + 1)

# 前からj,j+1,j+2 0<j<9998
sum = a[0] + a[1] + a[2]
for j in range(1,len(a)):
    # 累積和の計算
```

0 1 2
3 4 5
6 7 8