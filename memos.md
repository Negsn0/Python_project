# AtCoder 備忘録

## 1. 基本的な入出力とデータ型

### 入力処理

```Python
# 基本的な入力
input()  # 文字列入力
N = int(input())  # 数値入力
A = list(map(int, input().split()))  # スペース区切りの数値配列入力
```

### データ型の変換

```Python
# 文字列と数値の変換
i = 1234321
digits = [int(num) for num in str(i)]  # 数値を文字列に変換し、各桁を配列に格納
ab = int(a+b)  # 文字列を結合して数値に変換
```

## 2. 配列と文字列操作

### 配列の種類と基本操作

```Python
# 配列の種類
list()  # 配列(順序有り、重複あり)
set()   # 集合(順序なし、重複なし)

# 要素の追加・削除
S.append(A)     # Sの後ろにAを追加(stringなら'')
S = S[:-7]      # Sの後ろから7つを削除
S.pop(3)        # SのS[3]を削除
A += list(map(int, input().split()))  # 配列に要素を追加

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

### 文字列操作

```Python
# 文字列のカウント
s = input()
count = s.count('A')  # sの中の文字Aをカウント
```

## 3. 数値計算と最適化

### 基本的な演算

```Python
# 四則演算
(a + b) % L  # 剰余演算。Lで割った余りを取得
s = int(N/1.08)  # 除算して小数点以下を切り捨て
ab//2  # 整数除算（小数点以下切り捨て）

# 累乗計算
2 ** i  # 2のi乗
2 ** (i-1)  # 2の(i-1)乗
```

### 累積計算と最適化

```Python
# 累積計算
total += 2 * X[i]  # 値を2倍して加算
total += 2 * (K - X[i])  # 差の2倍を加算
count = countA + countB  # 複数のカウンターの合計

# 最小値の探索
result_comp = 100000000000000000  # 十分大きな初期値
if result_comp > result:
    result_comp = result  # より小さい値で更新

# 最大値の更新
if dis < A[i+1] - A[i]:
    dis = A[i+1] - A[i]  # より大きい値で更新
```

### 行列と多次元配列

```Python
# 行列の作成
A = [list(map(int, input().split())) for i in range(N)]  # N行の行列を入力

# 行列の要素アクセスと演算
A[j][k]  # j行k列の要素にアクセス
s += A[j][k]*B[k]  # 行列の要素同士の積和
```

## 4. 制御構造

### 条件分岐

```Python
# 基本的な条件分岐
if A[k]<A[k+1] and A[k+1]>A[k+2]:    # 複数の条件をandで結合
elif A[k]>A[k+1] and A[k+1]<A[k+2]:  # else ifの条件分岐

# 偶奇判定
if H % 2 == 0:  # 偶数判定
    # 処理
elif H % 2 == 1:  # 奇数判定
    # 処理

# 複合条件
if W == 1 or H == 1:  # どちらかの条件が満たされる場合
    # 処理

# 要素の検索
if k in A:  # 配列内に要素が存在するか確認
    B.append(A.index(k))  # 要素のインデックスを取得

# 条件の全一致確認
if all(cond in B for cond in conditions[i]):  # 全ての条件が満たされるか確認
```

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

### インクリメントとデクリメント

```Python
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

### 平方根の判定

```Python
if i * i == ab:  # 完全平方数の判定
```

### 複数変数の同時更新

```Python
# 変数の同時更新
A1 = (B + C) / 2
B1 = (A + C) / 2
C1 = (A + B) / 2
A = A1
B = B1
C = C1
```

## 7. 配列の並び替えとインデックス操作

### 配列の並び替え

```Python
# 配列のソート
d.sort()  # 配列を昇順にソート

# 中央値の計算
mid = N // 2  # 配列の中央インデックス
Knum = d[N//2] - d[N//2 - 1]  # 中央値の差
```

### インデックス操作

```Python
# インデックスの取得と変換
B.append(A.index(i+1)+1)  # 値のインデックスを取得して1を加算

# 配列の展開出力
print(*B)  # 配列の要素をスペース区切りで出力
```

## 8. 最適化と収束

### 絶対値と最小値

```Python
# 絶対値の計算
temp = abs(minimum - K)  # 2つの値の差の絶対値

# 最小値の更新
if temp < minimum:
    minimum = temp  # より小さい値で更新
```

### 剰余と最適化

```Python
# 剰余の計算と最適化
r = N % K  # NをKで割った余り
print(min(r, abs(r - K)))  # 余りと(K-余り)の小さい方を出力
```

## 9. 特殊なアルゴリズムと実装

### コラッツ予想の実装

```Python
# 数値の偶奇判定と変換
if temp % 2 == 0:
    temp = temp // 2  # 偶数なら2で割る
else:
    temp = 3 * temp + 1  # 奇数なら3倍して1を足す

# 集合を使用した重複チェック
a = set()
a.add(temp)
if temp1 == len(a):  # 重複が発生したかチェック
```

### 文字列の連続カウント

```Python
# 文字の条件判定とカウント
if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
    tmp += 1
    if tmp > count:
        count = tmp  # 最大値を更新
else:
    tmp = 0  # カウントをリセット
```

### 累乗計算と配列操作

```Python
# 累乗計算による値の更新
v[0] = (0.5**(N-1))*v[0]  # 0.5の(N-1)乗を掛ける
v[i] = (0.5**(N-i))*v[i]  # 0.5の(N-i)乗を掛ける
```

### 2 次元配列の操作

```Python
# 2次元配列の定義とアクセス
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l[2][2])  # 3行3列目の要素にアクセス
```

## to do

- dict の勉強
