---
slug: read-ecmascript2015-specification-part6
title: ECMAScript 2015の仕様書を読む（その6）
tags: [ ecmascript,javascript ]
date: 2016-04-05T00:40:37+09:00
lastmod: 2016-04-05T00:40:37+09:00
publishDate: 2016-04-05T00:40:37+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を読んでいます。エラー処理および言語仕様の拡張についての第16章、標準組み込み（ビルトイン）オブジェクトについての第17章、グローバルオブジェクトについての第18章。


## 第16章


　エラー処理についてと言語仕様の拡張について。「early error」という種別のエラーが検出されたら、その時点でスクリプトの評価を止めてそれを通知する。また、モジュール内でのearly errorが検出されたら、その時点でモジュールの評価は中止されモジュールは初期化されない。evalキーワードでスクリプトが実行された際にearly errorが発生した場合、その評価をその時点で終了される。

　このearly errorの発生条件は仕様書内に細かく記載されているが、いわゆる文法エラーがこれに相当する。なお、ECMAScriptの処理系はSyntax ErrorおよびReferenceError以外のエラーについては詳細にそれをレポートするべきである。

　言語仕様の拡張については、16.1で拡張してはいけない仕様についてが説明されている。こちらについては一般的にコードを書く際には知識は不要なので割愛。

## 第17章


　ECMAScriptの標準ビルトインオブジェクトについて。

・標準ビルトインオブジェクトの多くは関数オブジェクト
・関数オブジェクトのうち、一部はnew演算子付きで実行することが想定されているコンストラクタ
・ビルトイン関数には必要な引数よりも少ない引数を与えることができる。その場合、足りない引数にはundefinedが渡される
・必要な引数よりも多い引数を与えることもできる。通常それは関数の実行時に評価はされるが、その後は無視される。ただし、このとき実装側でTypeError例外を投げることも許可されている
・ビルトイン関数オブジェクトはlengthプロパティを持つ。このプロパティには、その関数に与える最大の名前付き引数の数が格納されている

## 第18章


　グローバルオブジェクトについて。グローバルオブジェクトは、コード実行が開始される前に作成される。これらオブジェクトをnew演算子で作成することはできないし、関数として実行することもできない。ECMAScript 2015ではいくつかのグローバルオブジェクトが規定されているほか、処理系によって独自のグローバルオブジェクトを用意することも許されている。

　ECMAScript 2015で定義されているグローバルオブジェクトは次の通り。まず値を示すオブジェクトが3つ。

・Infinity
・NaN
・undefined

　いくつかの関数オブジェクト。

・eval(x)
・isFinite(number)
・isNaN(number)
・parseFloat(string)
・parseInt(string, radix)
・decodeURI(encodedURI)
・decodeURIComponent(encodedURIComponent)
・encodeURI(uri)
・encodeURIComponent(uriComponent)

　いくつかのグローバルオブジェクトのコンストラクタ。

・Array()
・ArrayBuffer()
・Boolean()
・DataView()
・Date()
・Error()
・EvalError()
・Float32Array()
・Float64Array()
・Function()
・Int8Array
・Int16Array
・Int32Array
・Map()
・Number()
・Object()
・Proxy()
・Promise()
・RangeError()
・ReferenceError()
・RegExp()
・Set()
・String()
・Symbol()
・SyntaxError()
・TypeRrror()
・Uint8Array()
・Uint8ClampedArray()
・Uint16Array()
・Uint32Array()
・URIError()
・WeakMap()
・WeakSet()

　そのほかのグローバルオブジェクト。

・JSON
・Math
・Reflect

　各オブジェクトについての詳細は後の章で説明されている。

