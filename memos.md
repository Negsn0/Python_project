# AtCoder 備忘録

## 1. 基本的な入出力

```Python
# 入力
input()  # 基本的な入力
N = int(input())  # 数値の入力
A = list(map(int, input().split()))  # スペース区切りの数値配列の入力
```

## 2. 配列操作

### 配列の種類

```Python
list()  # 配列(順序有り、重複あり)
set()   # 集合(順序なし、重複なし)
```

### 配列の基本操作

```Python
# 要素の追加・削除
S.append(A)     # Sの後ろにAを追加(stringなら'')
S = S[:-7]      # Sの後ろから7つを削除
S.pop(3)        # SのS[3]を削除

# 配列の操作
max(A)          # 配列Aの最大値を取得
A.count(n)      # 配列Aの中の要素nの出現回数をカウント
A = P[i:j+i]    # 配列Pのi番目からj+i-1番目までの要素を取得
```

### 配列の変換と処理

```Python
# 内包表記
a = [x * 2 for x in a]  # 配列の各要素を2倍に

# map関数
map(f, a)  # 配列a全部に関数fを作用させる(戻り値はmap型なのでlistやsetで回収)
```

## 3. 文字列操作

```Python
# 文字列のカウント
s = input()
count = s.count('A')  # sの中の文字Aをカウント

# 数値から文字列への変換
i = 1234321
digits = [int(num) for num in str(i)]  # 数値を文字列に変換し、各桁を配列に格納
```

## 4. 数値演算

```Python
(a + b) % L  # 剰余演算。Lで割った余りを取得
```

## 5. ループ処理

```Python
for n in range(1, len(d)):     # 1から配列の長さ-1までループ
for n in range(1, A_max+1):    # 1からA_maxまでループ
```

## 6. 条件分岐

```Python
if A[k]<A[k+1] and A[k+1]>A[k+2]:    # 複数の条件をandで結合
elif A[k]>A[k+1] and A[k+1]<A[k+2]:  # else ifの条件分岐
```

## 7. NumPy 操作

```Python
import numpy as np
np.zeros((6,6))  # 6x6のゼロ行列を作成
A[i,j] = (i,j)   # 行列の要素に値を代入
```

## 8. アルゴリズム

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
