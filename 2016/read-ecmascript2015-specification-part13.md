---
slug: read-ecmascript2015-specification-part13
title: ECMAScript 2015の仕様書を読む（その13）
tags: [ ecmascript, javascript ]
date: 2016-05-11T00:42:56+09:00
lastmod: 2016-05-11T00:43:15+09:00
publishDate: 2016-05-11T00:42:56+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はテキスト処理関連について規定する第21章のうち、Stringオブジェクトについて。

## 第21章1節


　Stringオブジェクトのコンストラクタは内部オブジェクトが割り当てられているが、サブクラス化可能になっており、Stringオブジェクトのサブクラスはコンストラクタ内でsuperキーワードを使ってStringコンストラクタを実行しインスタンスを作成しなければならない。

　なお、Stringオブジェクトを関数として実行すると引数を文字列に変換したものを返す。また、newキーワード付きで関数として実行すると、引数を値として格納したStringオブジェクトを返す。

　Stringオブジェクトは次のプロパティ/メソッドを持つ。

```
String.fromCharCode(...codeUnits)	codeUnitsに相当する文字コードを含む文字列を返す。codeUnitsはUnicodeで指定。
String.fromCodePoint(...codePoints)	codePointsに相当する文字コードを含む文字列を返す
String.prototype	内部オブジェクトを指す。変更不可
String.raw(template, ...substitutions)	テンプレートオブジェクトに対し与えられた引数を使って展開を行う。通常はタグ付けされたテンプレート処理のために利用される
```

　また、String.prototypeオブジェクトは次のプロパティ/メソッドを持つ。

```
String.prototype.charAt(pos)	posの位置にある文字を返す
String.prototype.charCodeAt(pos)	posの位置にある文字の文字コードを返す
String.prototype.codePointAt(pos)	posの位置にある文字のコードポイントを返す
String.prototype.concat(...args)	argsを連結した文字列を返す
String.prototype.constructor	コンストラクタ。内部オブジェクト
String.prototype.endsWith(searchString [, endPosition])	文字列がsearchStringで終わっていればtrueを返す。endPositionを指定した場合、文字列がその長さであるかのように処理を行う
String.prototype.(includes)sesarchString [, position])	文字列がsearchStringを含んでいればtrueを返す。positionが指定された場合、その位置から検索を開始する
String.prototype.indexOf(searchString [, position])	文字列中でsearchStringが最初に出現する位置を返す。positionが指定された場合、その位置から検索を開始する
String.prototype.lastIndexOf(searchString [, position])	文字列中でsearchStringが最後に出現する位置を返す。positionが指定された場合、その位置から検索を開始する
String.prototype.localeCompare(tha [, reserved1 [, reserved2]])	ECMA-402で規定されているlocaleCompare処理を行う。
String.prototype.match(regexp)	regexpを使ってマッチ処理を行う
String.prototype.normalize([form])	文字列を正規化したものを返す。formは"NFC"、"NFD"、"NFKC"、"NFKD"が指定可能
String.prototype.repeat(count)	文字列をcount回繰り返したものを返す
String.prototype.replace(searchValue, replaceValue)	serachValueをreplaceValueに置き換える。replaceValueには$$、$&、$`、$'、$n、$nnなどが指定可能
String.prototype.search(regexp)	文字列中でregexpにマッチした位置を返す
String.prototype.slice(start, end)	startの位置からendの位置までの部分文字列を返す。endが負の場合、文字列のlengthにendを足したものがendとして使われる
String.prototype.split(separator, limit)	separatorで文字列を分割する
String.prototype.startsWith(searchString [, position])	文字列がsearchStringで始まっているならtrueを返す。positionが指定されていた場合、その場所から検索を開始する
String.prototype.substring(start, end)	startの位置からendの位置までの部分文字列を返す。endがstartより小さい場合、endとstartは入れ替えられる
String.prototype.toLocaleLowerCase([reseved1 [, reserved2]])	ECMA-402で規定されているtoLocaseLowerCase処理を行う。
String.prototype.toLocaleUpperCase([reseved1 [, reserved2]])	ECMA-402で規定されているtoLocaseUpperCase処理を行う。
String.prototype.toLowerCase()	小文字に変換した文字列を返す
String.prototype.toString()	変換した文字列を返す
String.prototype.toUpperCase()	大文字に変換した文字列を返す
String.prototype.trim()	前後のホワイトスペースをものを返す
String.prototype.valueOf()	変換した文字列を返す
String.prototype[@@iterator]()	文字列のコードポイントを走査するためのiteratorを返す
```

　また、Stringインスタンスはその文字列の長さを格納するlengthプロパティを持つ。

　Stringはiteratorを使った走査にも対応している。このiteratorは、文字列をインデックス順に返す。

