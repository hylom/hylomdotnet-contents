---
slug: read-ecmascript2015-specification-part11
title: ECMAScript 2015の仕様書を読む（その11）
tag: [ ecmascript, javascript ]
date: 2016-04-21T23:59:27+09:00
lastmod: 2016-04-21T23:59:38+09:00
publishDate: 2016-04-21T23:59:27+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はNumber、Math、Dateオブジェクトについて解説する第20章のうち、Mathオブジェクトについて。

## 第20章第2節


　Mathオブジェクトについて。Mathオブジェクトは関数オブジェクトではないため、関数としてもnewキーワード付きでも実行できない。

　Mathオブジェクトは多数のプロパティ/メソッドを持つ。まず、数値演算で使われる次のような定数が定義されている。これらはすべて書き込み禁止で列挙もされない。また、Math[@@toStringTag]のみConofigurableである。

```
Math.E	ネイピア数（e、exp(1)）
Math.LN10	log(10)
Math.LN2	log(2)
Math.LOG10E	log10(e)
Math.LOG2E	log2(e)
Math.PI	円周率
Math.SQRT1_2	√(1/2)
Math.Math.SQRT2	√2
Math[@@toStringTag]	"Math"という文字列
```

　また、次のような数学関数をメソッドとして持つ。

```
Math.abs(x)	絶対値
Math.acos(x)	アークコサイン
Math.acosh(x)	逆双曲線コサイン
Math.asin(x)	アークサイン
Math.asinh(x)	逆双曲線サイン
Math.atan(x)    アークタンジェント
Math.atanh(x)   逆双曲線タンジェント
Math.atan2(x, y)	atan(y/x)
Math.cbrt(x)	立方根
Math.ceil(x)    x以上の最小の整数
Math.clz32(x)	xを2進数表示し、その戦闘から続く0の桁数
Math.cos(x)	コサイン
Math.cosh(x)	双曲線コサイン
Math.exp(x)	eのx乗
Math.expm1(x)	eのx乗 - 1
Math.floor(x)	x以下の最小の整数
Math.fround(x)	xに最も近い32ビット浮動小数点数を返す
Math.hypot(value1, value2, value3, ...values)	引数で与えた値の2乗和平方根を返す
Math.imul(x, y)	xとyを整数に変換したものの積を返す
Math.log(x)	eを底とするxの対数
Math.log1p(x)	log(x) + 1
Math.log10(x)	10を底とするxの対数
Math.log2(x)	2を底とする2の対数
Math.max(value1, value2, value3, ...values)	引数の中で最大の数を返す。引数が与えられなかった場合は-Infinityを、NaNが含まれていた場合はNaNを返す
Math.min(value1, value2, value3, ...values)	引数の中で最小の数を返す。引数が与えられなかった場合は-Infinityを、NaNが含まれていた場合はNaNを返す
Math.pow(x, y)	xのy乗を返す
Math.random()	0以上1以下の乱数を返す
Math.round(x)	xに最も近い整数を返す（xの小数点1桁目を四捨五入する）
Math.sign(x)	xが0より大きければ1、0なら0、0より小さければ-1を返す
Math.sin(x)	サイン
Math.sinh(x)	双曲線サイン
Math.sqrt(x)	平方根
Math.tan(x)	タンジェント
Math.tanh(x)	双曲線タンジェント
Math.trunc(x)	xの整数部分を返す
```

