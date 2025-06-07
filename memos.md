# 備忘録

## 入力

基本は input()でどうにかできる。

## 数え上げる系

```Python
s = input()
count = s.count('A') # sの中のAをcountする。
```

## 配列の種類

```Python
set() # 集合(順序なし、重複なし)
list() # 配列(順序有り、重複あり)

```

## 配列の要素の追加・削除

```Python
S.append(A)  #Sの後ろにA(stringなら'')
S = S[:-7] #Sの後ろから7つを削除
S.pop(3) #SのS[3]を削除
```

## 配列の全要素に対して行う操作

```Python
a = [x * 2 for x in a] #内包表記。シンプル。
map(f , a) #配列a全部に関数fを作用させる。(戻り値はmap型なのでlistやsetで回収)

```

## string 系

```Python
i = 1234321
digits = [int(num) for num in str(i)]  # iを文字に変換して各桁を独立させ、配列のように扱える。numにstring型で数字を格納し、int型に直してdigitsに代入。
```

## 処理早くするシリーズ

累積和(積)

```Python
sum = 0
a = [] # a は1 ~ 10000までの数字の配列
for i in range(10000):
    a.append(i + 1)

# 前からj,j+1,j+2 0<j<9998
sum = a[0] + a[1] + a[2]
for j in range(1,len(a)):


```

## 部分数列

````

## 配列の操作
```Python
max(A)  # 配列Aの最大値を取得
A.count(n)  # 配列Aの中の要素nの出現回数をカウント
```

## 数値の操作

```Python
(a + b) % L  # 剰余演算。Lで割った余りを取得
```

## ループ処理

```Python
for n in range(1, len(d)):  # 1から配列の長さ-1までループ
for n in range(1, A_max+1):  # 1からA_maxまでループ
```

## NumPyの操作
```Python
import numpy as np
np.zeros((6,6))  # 6x6のゼロ行列を作成
A[i,j] = (i,j)  # 行列の要素に値を代入
```

## 配列のスライス操作
```Python
A = P[i:j+i]  # 配列Pのi番目からj+i-1番目までの要素を取得
```

## 条件分岐
```Python
if A[k]<A[k+1] and A[k+1]>A[k+2]:  # 複数の条件をandで結合
elif A[k]>A[k+1] and A[k+1]<A[k+2]:  # else ifの条件分岐
```
````
