---
slug: read-ecmascript2015-specification-part10
title: ECMAScript 2015の仕様書を読む（その10）
tags: [ ecmascript,javascript ]
date: 2016-04-20T00:17:00+09:00
lastmod: 2016-04-20T00:19:55+09:00
publishDate: 2016-04-20T00:17:00+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はNumber、Math、Dateオブジェクトについて解説する第20章のうち、Numberオブジェクトについて。

## 第20章第1節


　Numberオブジェクトについて。Numberオブジェクトは基本型であるNumberに対応するオブジェクト。サブクラスを作って拡張可能となっている。サブクラスを作る場合、コンストラクタ内でsuperキーワードを使ってNumberオブジェクトのコンストラクタを実行することが推奨されている。

　Numberオブジェクトを関数として実行すると、引数を数値化したものを返す。引数が与えられなかった場合は0を返す。また、newキーワード付きで実行されると引数を数値化したものを値として格納する新たなNumberオブジェクトを作成して返す。なお、このコンストラクタは内部オブジェクトを参照している。

　Numberオブジェクトが持つプロパティやメソッドは下記の通り。

```
Number.EPSILON	「1と1より大きい最小の数の差」を示す定数
Number.isFinite(number)	numberがNaN、Infinity、-Infinity以外の数であればtrueを返す
Number.isInteger(number)	numberが整数であればtrueを返す
Number.isNaN(number)	numberがNaNであればtrueを返す
Number.isSafeInteger(number)	numberが整数で、かつその絶対値がNumber.MAX_SAFE_INTEGER以下であればtrueを返す
Number.MAX_SAFE_INTEGER	2の53乗-1。Number型では整数はこの数+1までしか表現できない
Number.MAX_VALUE	Number形で扱える最大の数。約1.7976931348623157×10の308乗
Number.MIN_SAFE_INTEGER	-(2の53乗-1)。Number型では整数はこの数-1までしか表現できない
Number.MIN_VALUE	Number形で扱える最小の数。約5×10の-324乗
Number.NaN	NaN	
Number.NEGATIVE_INFINITY	-Infinity
Number.paseFloat(string)	parseFloat(string)と同等
Number.parseInt(string, radix)	parseFloat(string, radix)と同等
Number.POSITIVE_INFINITY	Infinity
Number.prototype	初期値は内部オブジェクト
```

　なお、Number.isNaNはisNaNとは異なり、引数としてNaNが与えられた場合のみtrueを返す。

```
> isNaN("fo")
true
> Number.isNaN("fo")
false
```

　また、Number.MAX_SAFE_INTEGER+1を超える整数、もしくはNumber.MIN_SAFE_INTEGER-1よりも小さい整数は次の例のように演算結果が保証されない。

```
> Number.MAX_SAFE_INTEGER 
9007199254740991
> Number.MAX_SAFE_INTEGER + 1
9007199254740992
> Number.MAX_SAFE_INTEGER + 2
9007199254740992
> Number.MAX_SAFE_INTEGER + 3
9007199254740994
```

　Number.prototypeの持つプロパティ/メソッドは下記になる。

```
Number.prototype.constructor	コンストラクタ。初期値は内部オブジェクト
Number.prototype.toExponential(fractionDigits)	指数表記した文字列に変換して返す。このとき、小数点以下はfractionDigitsで指定した桁数となる
Number.prototype.toFixed(fractionDigits)	固定小数点表記した文字列に変換して返す。このとき、小数点以下はfractionDigitsで指定した桁数となる
Number.prototype.toLocaleString([reserved1 [, reserved2]])	ECMA-402規格で定義されたローカリゼーションされた文字列を返す
Number.prototype.toPrecision(precision)	precisionで指定した桁数の文字列に変換して返す
Number.prototype.toString([radix])	文字列に変換して返す。radixが指定された場合、radix進数表記で返す
Number.prototype.valueOf()	値を返す
```

　なお、数値型はNumberオブジェクトでありNnumber.prototypeを継承する。
