# 備忘録

## 入力

基本はinput()でどうにかできる。

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

## string系
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