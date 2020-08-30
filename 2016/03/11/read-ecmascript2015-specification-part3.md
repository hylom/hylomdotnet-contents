---
slug: read-ecmascript2015-specification-part3
title: ECMAScript 2015の仕様書を読む（その3）
tag: [ ecmascript, javascript ]
date: 2016-03-11T23:09:00+09:00
lastmod: 2016-03-11T23:09:00+09:00
publishDate: 2016-03-11T23:09:00+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を読んでいます。今回は第12章と第13章。ここではひたすら定義が並んでいるので斜め読みして、必要に応じて戻ることにする。

## 第12章


　ECMAScriptの式について。deleteやvoid、typeof、instanceofなどを含む演算子の挙動についても解説されている。新キーワードであるyieldも登場。

　yieldはPythonのyieldと同様の処理を行うもので、関数の実行を中断して戻り値を返すというもの。その関数オブジェクトのnextメソッドを実行することで中断したところから実行を再開できる。

## 第13章


　文と宣言について。新しいキーワードであるletやconst、classなどが登場する。また、新たな構文であるfor〜of文も登場。

　letとconstはvarと同じく変数定義に使うキーワード。letはレキシカルスコープのみで通用する、いわゆる局所変数を定義するのに使い、constは定数として宣言するのに使う。

　また、新たにfor〜of文も登場している。for〜in文と似ているが、プロパティ名ではなくプロパティの値に対して反復処理を行う点が異なる。

