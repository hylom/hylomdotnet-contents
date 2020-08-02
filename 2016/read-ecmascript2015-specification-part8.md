---
slug: read-ecmascript2015-specification-part8
title: ECMAScript 2015の仕様書を読む（その8）
tags: [ ecmascript,javascript ]
date: 2016-04-14T00:58:06+09:00
lastmod: 2016-04-14T00:58:06+09:00
publishDate: 2016-04-14T00:58:06+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を読んでいます。今回は基本オブジェクト（Fundamental Objects）についての第19章のうち、Functionオブジェクトについて。

## 第19章第2節


　Functionオブジェクトおよびそのメソッド、プロパティについてが説明されている。

　Functionオブジェクトは関数として呼び出すことで、関数オブジェクトを返す。この場合、常にFunctionオブジェクトのコンストラクタとして関数は実行されるため、newキーワードを付けても付けなくても同じ結果となる。

　Functionオブジェクトを関数として実行する場合、以下のような引数を取る。

```
Function(p1, p2, ..., pn, body)
```

　p1〜pnはその関数に与える仮引数リスト、bodyは関数本体である。戻り値はFunctionオブジェクトとなる。なお、仮引数リストは文字列で与えられる。このとき、1つの引数に複数の仮引数を入れることが可能。たとえば以下の3つは同じものを返す。

```
new Function("a", "b", "c", "return a+b+c")
new Function("a, b, c", "return a+b+c")
new Function("a,b", "c", "return a+b+c")
```

　Functionオブジェクトは以下のプロパティを持つ。

```
Function.length	1を返す
Funtion.prototype	内部オブジェクトが割り当てられている
```

　また、Function.protoypeオブジェクトは内部オブジェクトであるため、関数として実行すると常にundefinedを返す。また、下記のプロパティを持つ。

```
Function.prototype.apply(thisArg, argArray)	thisArgをthis変数に設定し、argArrayを引数として関数を実行する
Function.prototype.bind(thisArg, ...args)	thisArgをthis変数に設定し、argsを引数として呼び出される束縛関数を作成して返す
Function.prototype.call(thisArg, ...args)	thisArgをthis変数に設定し、argを引数として関数を実行する
Function.prototype.constructor	コンストラクタ関数。初期値は内部オブジェクト
Function.prototype.toString()	オブジェクトの内容を示す文字列を返す
Function.prototype[@@hasInstance](V)	v instanceof Fに相当
```

　なお、Functionオブジェクトのインスタンスはlength、name、prototypeというプロパティを持つ。lengthは関数の引数の数、nameは関数名が格納されている。

