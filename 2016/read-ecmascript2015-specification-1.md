---
slug: read-ecmascript2015-specification-1
title: ECMAScript 2015の仕様書を読む（その1）
tags: [ ecmascript,javascript ]
date: 2016-03-07T23:49:23+09:00
lastmod: 2016-03-07T23:49:23+09:00
publishDate: 2016-03-07T23:49:23+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を最近読み始めたので、従来のECMAScript 3/5との差異を中心に各章の要点を軽くまとめていく。

　今回は第1章〜第9章まで。ここではECMAScript処理系の内部実装について説明されており、ECMAScriptを使うだけであれば理解は不要。CでNode.js向けモジュールを実装する場合などは知っておくと良いかもしれない。

## 第1章


　この文書はECMAScript 2015について定義されているということが書いてある。

## 第2章


　ECMAScript実装が必要とする要件等が書いてある。

## 第3章


　関連文書について言及。ECMAScript 2015では国際化機能が実装されており、それは別文書（[ECMAScript 2015 Internationalization API Specification](http://www.ecma-international.org/publications/standards/Ecma-402.htm)）でまとめられている

　また、JSONの仕様は[Standard ECMA-404 The JSON Data Interchange Format](http://www.ecma-international.org/publications/standards/Ecma-404.htm)でまとめられている。

## 第4章


　ECMAScriptの概要や歴史が書いてある。オブジェクト指向、プロトタイプベースの敬称といった特徴が説明されている。また、用語についても説明されている。この辺りは以前のECMAScriptから変更はない。

## 第5章


　このドキュメントにおける表記法が説明されている。

## 第6章


　ECMAScriptで利用できるデータ型と値の説明。こちらも以前からの変更はなし。数値型は64ビット倍精度浮動小数点とか、2の53乗-2がNaNに割り当てられているとか、Infinity（無限大）が定義されているとかが書かれている。オブジェクトが内部的に実装しているメソッドとかの話もあるが、これらはECMAScriptコードからは隠蔽されているのでECMAScriptコードを書く用途では特に覚えなくてもOK。

## 第7章


　型変換ルール（ObjectやSymbolはtrueになるとか、Stringは空文字列の場合のみfalseになるとか、文字列を数値に変換するルールとか）やオブジェクト型の判定ルール、2つの値が同一かどうかの比較ルールなどが説明されている。

## 第8章


　ECMAScriptがどうやってコードを実行するのか、という話。

 - ECMAScriptのレキシカル環境は関数宣言やブロックステートメント、TryステートメントとのCatch節などで開始されるよ
 - どのレキシカル環境にも属さない環境はグローバル環境と呼ばれるよ
 - モジュール環境や関数環境といった環境も存在するよ
 - ECMAScriptのコードは評価前に「Realm」（領域）というものに関連付けられるよ
 - 実行コンテキストというものがあるよ
 - ジョブやジョブキューというものがあるよ
 - 一つの実行コンテキストが終了したら、ジョブキューからジョブを1つ取り出してそこから実行コンテキストを作成するよ

## 第9章


　オブジェクトの振る舞いの話。すべてのオブジェクトはPrototypeという内部スロットを持ち、これを使ってオブジェクトの継承を実現している。また、Extensibleという内部スロットもあり、これがfalseの場合Prototypeスロットは変更が禁止される。

　関数オブジェクトは「strict function」と「non-strict function」の2種類が存在しうる。どちらもレキシカル環境を内包するほか、基底オブジェクトなのか派生オブジェクトなのかといった情報や、関数の種類（normal、classConstructor、generator）といった情報を内部的に持っている。

　ECMAScriptにはいくつかのビルトイン関数があるが、これらの関数オブジェクトは特殊なビルトイン関数オブジェクトとして定義されている。これらのオブジェクトは通常の関数オブジェクトとは異なり、一部の内部メソッドなどを持たないなどの違いがある。

　特殊なオブジェクトとして、Exoticオブジェクトというものがある。9.4節ではExoticオブジェクトとしてArrayオブジェクトやStringオブジェクト、Intger Indexedオブジェクト、Module Namespaceオブジェクトについて説明されている。Exoticオブジェクトはオブジェクトとしての特性を持ちつつ、特別な特性も実装されている（たとえばArrayオブジェクトであればlengthプロパティを持っていたり、インデックスでのアクセスが可能であったり）。

　さらに、その一部のみがECMAScriptで実装されているProxyオブジェクトというものも存在する。これは、ほかの言語で実装されたコードをECMAScriptコードから呼び出すために使われる。

