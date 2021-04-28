# python高速化

pythonの高速化、その他tips

## 入出力

- 高速化

readlineは改行コードを含むので、[:-1]で消す必要あり

```
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
```

- 複数入力

```
a,b,c = input()[:-1].split()  #3個の文字列の入力を受け取る
str_list = list(input()[:-1].split())  # n個の文字列がリストに格納される
a,b,c = map(int, input()[:-1].split())  # 3個の数字の入力を受け取る
```

- ２次元

**文字**
```
n = int(input())  # nは入力回数
str_list = [list(input().split()) for _ in range(n)]
print(str_list)
```

**数字**

```
n = int(input())  # nは入力回数
num_list = [list(map(int, input().split())) for _ in range(n)]
print(num_list)
```




## データ格納

- 末尾

append

- 先頭への要素の追加・削除

deque

- 注意する処理

in, min, max : O(n)

- set, Dict

ハッシュテーブル:O(1)

- list

Listへの不必要な書き込みは実行が遅くなる原因

**indexが必要な場合**

```
for i, ai in enumerate(a):
    ai
```

**indexがいらない**

```
for ai in a:
    ai
```
- sort

**高速**

```
from operator import itemgetter
a.sort(key=itemgetter(1))
```

**多次元配列,高速**

1つ目の要素でソート、同じ場合は2つ目, itemgetterで両方指定しないと、指定しなかったほうの順序が保証できない

```
from operator import itemgetter
list = [[10,4],[3,6],[4,6],[5,0],[4,9],[2,0]]
list.sort(key=itemgetter(0,1))
print (list)
```


2つ目の要素でソート、同じ場合は１つ目

```
from operator import itemgetter
list = [[10,4],[3,6],[4,6],[5,0],[4,9],[2,0]]
list.sort(key=itemgetter(1,0))
print (list)
```

```
sorted(a, key=lambda x:(x[1],x[2]), reverse=True)#降順
```

第1キーは昇順、第2キーは降順

```
list = sorted(a, key=lambda x:(x[0],-x[1]))
```

**柔軟なソート**

```
a = ['e', 'B', 'd', 'C', 'a']
print(sorted(a))                            # 普通にソートすると大文字，小文字それぞれでソートされます．
print(sorted(a, key=lambda x: x.upper()))   # 比較時に大文字に変換してソートするので，結果大文字・小文字あわせてソートされます．
```

- 変数

**local変数を利用した高速化**


pythonではグローバル変数にアクセスするよりもローカル変数にアクセスする方が早い

- 再帰関数の上限

上限確認

```
import sys
print(sys.getrecursionlimit())
>>1000 (local環境)
```

上限操作

```
import sys
sys.setrecursionlimit(10**6)
```




## 参考URL

https://medium.com/finatext/lets-do-competitive-programming-with-python-9c8b834769f6

https://docs.python.org/ja/3.6/library/collections.html#collections.defaultdict

https://qiita.com/fantm21/items/6df776d99356ef6d14d4