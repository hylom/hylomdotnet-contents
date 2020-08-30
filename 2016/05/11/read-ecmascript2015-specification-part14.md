---
slug: read-ecmascript2015-specification-part14
title: ECMAScript 2015の仕様書を読む（その14）
tag: [ ecmascript, javascript ]
date: 2016-05-11T23:13:51+09:00
lastmod: 2016-05-13T01:40:45+09:00
publishDate: 2016-05-11T23:13:51+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はテキスト処理関連について規定する第21章のうち、RegExpオブジェクトについて。

## 第21章2節


　RegExpオブジェクトは正規表現およびそれに関するフラグを格納するオブジェクト。Perl 5の正規表現をベースにしている。ECMAScriptで使える正規表現については詳しくまとめると大変なので省略。また、Perlとは異なり使える文字クラスは\d（数字）、\D（数字以外）、\s（ホワイトスペース）、\S（ホワイトスペース以外）、\w（アルファベットおよび数字、アンダースコア）、\W（アルファベットおよび数字、アンダースコア以外）の6つのみ。また、コントロールシーケンスは\t（HT）、\n（LF）、\v（VT）、\f（FF）、\r（CR）が定義されている。

　RegExpオブジェクトは(pattern, flags)という引数を取る。patternは正規表現リテラルもしくは文字列、flagsがフラグ。

　利用できるフラグはg（global）、i（ignoreCase）、m（multiline）、u（unicode）、y（sticky）。

　RegExpオブジェクトはRegExp[@@species]というアクセサを持つ。通常派生オブジェクトを作る際にこれを使用する。サブクラスを作る際にこの挙動を書き換えることも可能。

　RegExp.prototypeプロパティは下記のプロパティ/メソッドを持つ。

```
RegExp.prototype.constructor    コンストラクタ。初期値は内部オブジェクト
RegExp.prototype.exec(string)	stringに対しマッチを行う
RegExp.prototype.flags	アクセサ。設定されているフラグを返す
RegExp.prototype.global	アクセサ。gフラグが設定されていればtrue
RegExp.prototype.ignoreCase	アクセサ。iフラグが設定されていればtrue
RegExp.prototype[@@match](string)	String.prototype.matchメソッド内で内部的に呼び出されるマッチ関数
RegExp.prototype.multiline	アクセサ。mフラグが設定されていればtrue
RegExp.prototype[@@replace](string, replaceValue)	String.prototype.replaceメソッド内で内部的に呼び出される置換関数
RegExp.prototype[@@search](string)	String.prototype.searchメソッド内で内部的に呼び出されるマッチ関数
RegExp.prototype.source	アクセサ。正規表現を返す
RegExp.prototype[@@split](string, limit)	String.prototype.splitメソッド内で内部的に呼び出されるマッチ関数
RegExp.prototype.sticky	アクセサ。yフラグが設定されていればtrue
RegExp.prototype.test(S)	Sに対しマッチを行い、マッチしたらtrueを返す
RegExp.prototype.toString()	正規表現を文字列として返す
RegExp.prototype.unicode	アクセサ。uフラグが設定されていればtrue
```

 　RegExpオブジェクトはlastIndexプロパティを持つ。これは、次のマッチ処理の際にどの位置からマッチ処理を行うべきかを格納する。
