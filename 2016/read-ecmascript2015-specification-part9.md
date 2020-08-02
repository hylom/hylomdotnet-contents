---
slug: read-ecmascript2015-specification-part9
title: ECMAScript 2015の仕様書を読む（その9）
tags: [ ecmascript,javascript ]
date: 2016-04-15T01:06:06+09:00
lastmod: 2016-04-19T23:37:05+09:00
publishDate: 2016-04-15T01:06:06+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を読んでいます。今回は基本オブジェクト（Fundamental Objects）についての第19章のうち、Boolean、Symbol、Errorオブジェクトについて。

## 第19章第3節


　Booleanオブジェクトおよびそのメソッド、プロパティについて説明されている。

　Booleanオブジェクトは関数として実行すると、引数として与えたオブジェクトの真偽値に対応したtrueもしくはfalseを返す。また、newキーワード付きで実行するとその真偽値に対応したBooleanオブジェクトを返す。

　Booleanオブジェクトはprototypeプロパティのみを持つ。初期値は内部オブジェクトとなる。このプロパティの書き換えや属性変更は行えない。また、Boolean.prototypeは下記のプロパティ/メソッドを持つ。

```
Boolean.prototype.constructor	コンストラクタ。初期値は内部オブジェクト
Boolean.prototype.toString()	格納されている値に応じて"true"もしくは"false"を返す
Boolean.prototype.valueOf()	格納されている値に応じてtrue/falseを返す
```

## 第19章第4節


　Symbolオブジェクトおよびそのメソッド、プロパティについて説明されている。SymbolはECMAScript2015で新たに導入された基本オブジェクトで、オブジェクトのプロパティを参照するためのキーとして使用することが想定されている。

　Symbolオブジェクトをそのまま関数として実行すると、ユニークなSymbolオブジェクトを作成して返す。このとき、作成されたオブジェクトの[[Description]]内部スロットに引数として与えたオブジェクトを文字列に変換したものが格納される。また、newキーワード付きで実行するとTypeError例外を発生させる。

　Symbolオブジェクトは下記のプロパティ/メソッドを持つ。

```
Symbol.for(key)	GlobalSymbolRegistryを検索し、keyに対応するSybolがあればそれを返す。無ければ、新たなSymbolを作成し、GlobalSymboその[[key]]内部スロットおよび[[symbol]]内部スロットにkeyを文字列に変換したものを設定する。GlobalSymbolRegistryにkeyをキーとしてこのSymbolを登録し、このSymbolを返す
Symbol.hasInstance	@@hasInstanceシンボルが格納されている
Symbol.isConcatSpreadable	@@isConcatSpreadableシンボルが格納されている
Symbol.iterator	@@iteratorシンボルが格納されている
Symbol.keyFor(sym)	GlobalSymbolRegistryを検索し、symシンボルに対応するkeyがあればそれを返す。なければundefinedを返す
Symbol.match	@@matchシンボルが格納されている
Symbol.prototype	初期値では内部オブジェクトが格納されている
Symbol.replace	@@replaceシンボルが格納されている
Symbol.search	@@searchシンボルが格納されている
Symbol.spicies	@@spiciesシンボルが格納されている
Symbol.split	@@splitシンボルが格納されている
Symbol.toPrimitive	@@toPrimitiveシンボルが格納されている
Symbol.toStringTag	@@toStringTagシンボルが格納されている
Symbol.unscopables	@@unscopablesシンボルが格納されている
```

　なお、GlobalSymbolRegistryはグローバルな内部変数。

　Symbol.prototypeは下記のプロパティ/メソッドを持つ。

```
Symbol.prototype.constructor	コンストラクタ。初期値は内部オブジェクト
Symbol.prototype.toString()	"Symbol ([[Description]])"という文字列を返す
Symbol.prototype.valueOf()	そのシンボル自体を返す。オブジェクトがSymbolオブジェクトで内場合、[[SymbolData]]内部スロットの値を返す
Symbol.prototype[@@toPrimitive](hint)	Symbolオブジェクトをプリミティブ値に変換したものを返す。hintは"default"もしくは"number"、"string"
Symbol.prototype[@@toStringTag]	初期値は"Symbol"
```

　[[SymbolData]]内部スロットは、そのSymbolオブジェクトの内容を示す値が格納されているもの。

## 第19章第5節


　Errorオブジェクトおよびそのメソッド、プロパティについて説明されている。Errorオブジェクトは例外が発生した際にランタイムによって生成されるほか、ユーザー定義例外の基本オブジェクトとしても使われる。

　Errorオブジェクトをそのまま関数として実行すると、新たなErrorオブジェクトを生成して返す。このとき、引数に与えたオブジェクトを文字列化してmeessageプロパティの値に設定する。また、newキーワード付きで実行した場合も同じ挙動を行う。

　なお、Errorオブジェクトのコンストラクタはそのサブクラスを作れるように設計されている。その場合、コンストラクタ内ではsuperキーワードを使ってErrorオブジェクトを作成・初期化することが推奨されている。

　Errorオブジェクトは下記のプロパティ/メソッドを持つ。

```
Error.prototype	初期値では内部オブジェクトが格納されている
```

　Error.prototypeは下記のプロパティ/メソッドを持つ。

```
Error.prototype.constructor	コンストラクタ。初期値は内部オブジェクト
Error.prototype.message	初期値は空の文字列
Error.prototype.name	初期値は"Error"
Error.prototype.toString()	"<name>: <message>"という文字列を返す
```

　なお、ECMAScript2015ではネイティブエラーオブジェクトとして下記が用意されている。

```
EvalError
RangeError
ReferenceError
SyntaxError
TypeError
URIError
```

　これらのオブジェクトもサブクラス化が可能となっている。

