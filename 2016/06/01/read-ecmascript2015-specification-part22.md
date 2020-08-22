---
slug: read-ecmascript2015-specification-part22
title: ECMAScript 2015の仕様書を読む（その22）
tags: [ ecmascript, javascript ]
date: 2016-06-01T01:27:24+09:00
lastmod: 2016-06-01T01:27:43+09:00
publishDate: 2016-06-01T01:27:24+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回は付録について（付録A、D、Eについては詳細な内容は割愛）。

## 付録A


　文法まとめ。本編で説明されている文法がここでまとめられている。とりあえずここを見れば記述可能な文法が分かる。

## 付録B


　Webブラウザ向けの追加機能について。本来推奨されないが、Webブラウザ上で実行されるコードの互換性を保つために規定されているもので、Webブラウザ以外のECMAScript実行環境では実装しなくてもよい。また、これらはstrict modeでは利用できない。

　規定されているのは下記。

 - 数値リテラルにおける0で始まる8進数表記（本来であれば8進数表記は0Oで始まる必要がある）
 - 8進数表記を使ったエスケープシーケンス（バックスラッシュに続けて[0-8]もしくは[0-3][0-8]、[0-4][0-8]、[0-3][0-8][0-8]）
 - HTML風コメント（<!--、-->を利用するもの）
 - Unicodeの基本多言語面（BMP）に関連する正規表現パターン
 - グローバルオブジェクトのescape(string)およびunescape(string)プロパティ
 - Object.prototype.__proto__
 - String.prototype.substr(start, length)
 - String.prototypeのanchor、big、blink、bold、fixed、fontcolor、fontsize、italics、link、small、strike、sub、supメソッド
 - Date.prototypeのgetYear、setYear、toGMTStringメソッド
 - RegExp.prototypeのcompileメソッド
 - オブジェクトの初期化時における__proto__プロパティの利用
 - ラベルを使った関数定義
 - ブロックレベルでの関数定義
 - ifステートメント内での関数定義
 - catchブロック内での重複した変数定義

　なお、escapeプロパティは[A-Za-z0-9@*_+-./]をURLエンコードする。

## 付録C


　ECMAScriptにおけるstrict modeについて。strict modeでは非strct modeと下記が異なる。

 - 予約語にimplements、interface、let、private、protected、public、static、yieldが追加されている
 - 付録Cで定義されているWebブラウザ向けの互換性維持のための文法や機能が利用できない
 - 宣言されていない識別子や参照先が存在しないリファレンスがグローバルオブジェクトのプロパティとして生成されない
 - 各種構文でeval、argumentsを左手側に置くことはできない
 - 関数内で引数が格納されるオブジェクト（argumentsオブジェクト）のcallerやcalleeプロパティ
 - argumentsオブジェクトに格納されている値と引数として渡される値は別
 - argumentsオブジェクトは変更不可
 - 「識別子 eval」や「識別子 arguments」はSyntaxErrorとなる
 - eval内ではそれを呼び出した環境の変数や関数のインスタンスを生成できない
 - thisの値がnullやundefinedだった場合、これらがグローバルオブジェクトに置き換えられることはく、またプリミティブ値が対応するラッパーオブジェクトに変換されることはない
 - 値や関数引数、関数名に対するdelete演算子の利用がSyntaxErrorに
 - Configurableでないプロパティに対するdelete演算子の利用がSyntaxErrorに
 - with文は利用できない
 - try〜catch文でcatchを構成する識別子がevalやargumentsだった場合、SyntaxErrorに
 - 関数定義の歳の引数パラメータで同じものを2つ以上使うとSyntaxErrorに
 - 関数のcallerやargumentsプロパティについてこの仕様書で規定されている以外の拡張をすべきではない

## 付録D


　過去のバージョンのECMAScriptから挙動が修正された点について。

## 付録E


　過去のバージョンのECMAScriptとは互換性のない変更について。

