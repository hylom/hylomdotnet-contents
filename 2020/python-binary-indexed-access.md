---
slug: python-binary-indexed-access
title: 「Pythonではバイナリファイルを操作したい時にバイナリ列をリストに変換して操作した後にまたバイナリ列に戻さなければならない」というのは不正確
tags: [ python, programming ]
date: 2020-05-23T15:31:09+09:00
lastmod: 2020-05-23T15:47:23+09:00
publishDate: 2020-05-23T15:31:09+09:00
---

　「Pythonでバイナリファイルを操作したい場合にファイルから読み出したバイナリ列をリストに変換しないとデータを自由に編集できないし、書き出し時に再度バイナリ列に変換しなければならないのでPythonは嫌い」という話を見かけたのですが、それは不正確だし適切な処理ではないです。

　そこではこの処理について、次のように記述されていました（適当に抜粋・改変しています）。

```
f = open("somefile.bin", "rb")
bin = f.read()
f.close()

data = []
for b in bin:
    data.append(b)

# ここでインデックスを使ったdata配列の操作を行う
# ：
# ：

f = open("output.bin", "wb")
f.write(bytearray(data))
f.close()
```

　このコードでは、データをbinという変数に読み込んだ後、dataというlistに入れて処理し、最後にそのlistをbytearray型に変換してからファイルに書き出しています。確かにこう書いてしまうと、配列への変換が冗長です。そもそもなぜこういった処理が必要になるかというと、open()でバイナリ形式での読み出し（"rb"フラグ）を指定した場合、読み出されたデータは[bytes](https://docs.python.org/ja/3/library/stdtypes.html#bytes)型のオブジェクトとして返されます。

```
$ python3
Python 3.7.5 (v3.7.5:5c02a39a0b, Oct 14 2019, 18:49:57) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> with open('testdata.bin', 'rb') as f:
...     bin_data = f.read()
... 
>>>
>>> type(bin_data)
 <class 'bytes'>
```

　bytes型では、インデックスを使ってその値を取得することができます。

```
>>> bin_data[48]
48
```

　一方で、bytes型はimmutableなオブジェクトなので、値を変更することはできません。

```
>>> bin_data[48] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
```

　しかし、実はPythonには[bytearray](https://docs.python.org/ja/3/library/stdtypes.html#bytearray)というバイト列を扱うmutableな型もありまして、これを使えばbytes型と同様にインデックスを使った指定でデータを書き換えることができます。

```
>>> ba = bytearray(bin_data)
>>>
>>> type(ba)
 <class 'bytearray'>
>>>
>>> ba[48]
48
>>>
>>> ba[48] = 0x10
>>>
>>> ba[48]
16
```

　さらにこのbytearray型のオブジェクトは、write()メソッドの引数として指定することで直接ファイルに書き出せます。

```
>>> with open('output.bin', 'wb') as f:
...     f.write(ba)
... 
256
```

　ということで、先に挙げられていた「不満のあるコード」は次のように書き換えられます。

```
with open("somefile.bin", "rb") as f:
    data = bytearray(f.read())

# ここでインデックスを使ったdata配列の操作を行う
# ：
# ：

with open("output.bin", "wb") as f:
    f.write(data)
```

　このコードでも、ファイルから直接bytearray型のオブジェクトに読み込ませている訳ではない（bytes型オブジェクトを中継している）ため、結局バイナリ列をリストに変換しているじゃないか、と言われたらまあそうなんですが、それをバイナリ列に戻さなくても書き込みはできます、という話でした。

