---
slug: read-ecmascript2015-specification-part19
title: ECMAScript 2015の仕様書を読む（その19）
tags: [ ecmascript,javascript ]
date: 2016-05-23T22:01:25+09:00
lastmod: 2016-05-23T22:02:02+09:00
publishDate: 2016-05-23T22:01:25+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はArrayBufferおよびDataView、JSONオブジェクトについて規定する第24章。

## 第24章1節


　ArrayBufferオブジェクトについて。ArrayBufferは、処理系内部に確保された、任意の値を格納できるメモリバッファをラップするオブジェクトとなる。このオブジェクトは内部的にはデータを格納するメモリバッファと、そのバッファの長さを保持する。

　ArrayBufferコンストラクタはサブクラス化可能にデザインされている。その場合、サブクラスのコンストラクタ内ではsuperキーワードを使ってWeakMapコンストラクタを呼び出してインスタンスの初期化を行う必要がある。

　ArrayBufferをnewキーワード付きで関数として実行すると、ArrayBufferのインスタンスを生成できる。この際、引数にはバッファの長さを指定できる。newキーワード無しで実行するとTypeErrorとなる。

　ArrayBufferオブジェクトは下記のメソッド/プロパティを持つ。

```
ArrayBuffer.isView(arg)	argがViewedArrayBufferであればtrueを返す
ArrayBuffer.prototype	内部オブジェクト
ArrayBuffer[@@species]	getter。
```

　また、ArrayBuffer.prototypeは次のメソッド/プロパティを持つ。

```
ArrayBuffer.prototype.byteLength	getter。対応するバッファのバイト数を返す
ArrayBuffer.prototype.constructor	コンストラクタ
ArrayBuffer.prototype.slice(start, end)	対応するバッファのstartバイトからendバイトを新たに作成したArrayBufferにコピーして返す
ArrayBuffer.prototype[@@toStringTag]	"ArrayBuffer"
```

## 第24章2節


　DataViewオブジェクトについて。DataViewオブジェクトは対応するArrayBufferに格納されたデータにアクセスするためのメソッドを提供する。データへのアクセスはすべてNumber形式で行い、またコンストラクタで指定したbyteOffsetおよびbyteLengthの範囲を超える範囲へはアクセスできない。　

　ArrayBufferコンストラクタはサブクラス化可能にデザインされている。その場合、サブクラスのコンストラクタ内ではsuperキーワードを使ってWeakMapコンストラクタを呼び出してインスタンスの初期化を行う必要がある。

　DataViewオブジェクトをnewキーワード付きで関数として実行すると、DataViewオブジェクトのインスタンスを生成できる。引数はDataView(buffer [, byteOffset [, byteLength]])の最大3つ。bufferは対応付けるArrayBuffer（もしくはその派生オブジェクト）。byteOffset、ByteLengthはそれぞれバッファを参照する際のオフセットと、最大長さ。

　DataViewオブジェクトはprototypeプロパティのみを持つ。また、DataView.prototypeは次のメソッド/プロパティを持つ。

```
DataView.prototype.buffer	getter。対応付けられたArrayBufferを返す
DataView.prototype.byteLength	getter。参照できる最大バイト数を返す
DataView.prototype.byteOffset	getter。バッファを参照する際のオフセットを返す
DataView.prototype.constructor	コンストラクタ
DataView.prototype.getFloat32(byteOffset [, littleEndian])	対応付けられたバッファのbyteOffsetバイト目からのデータをFloat32として扱い、それをNumber形式に変換してデータを取り出す。littleEndianがtrueならリトルエンディアン、falseならビッグエンディアンで取り出す。以下、取り出す形式が異なるのみで同じ処理を行う
DataView.prototype.getFloat64(byteOffset [, littleEndian])	
DataView.prototype.getInt8(byteOffset)	
DataView.prototype.getInt16(byteOffset [, littleEndian])	
DataView.prototype.getInt32(byteOffset [, littleEndian])	
DataView.prototype.getUint8(byteOffset)	
DataView.prototype.getUint16(byteOffset [, littleEndian])	
DataView.prototype.getUint32(byteOffset [, littleEndian])	
DataView.prototype.setFloat32(byteOffset, value [, littleEndian])	対応付けられたバッファのbyteOffsetバイト目以降に、valueをFloat32として扱ってバイナリ化したものを書き込む。littleEndianがtrueならリトルエンディアン、falseならビッグエンディアンで取り出す。以下、取り出す形式が異なるのみで同じ処理を行う
DataView.prototype.setFloat64(byteOffset, value [, littleEndian])	
DataView.prototype.setInt8(byteOffset, value)	
DataView.prototype.setInt16(byteOffset, value [, littleEndian])	
DataView.prototype.setInt32(byteOffset, value [, littleEndian])	
DataView.prototype.setUint8(byteOffset, value)	
DataView.prototype.setUint16(byteOffset, value [, littleEndian])	
DataView.prototype.setUint32(byteOffset, value [, littleEndian])	
DataView.prototype[@@toStringTag]	"DataView"
```

## 第24章3節


　JSONオブジェクトについて。JSON形式で記述されたテキストベースのデータをオブジェクト化するもの。

　JSONオブジェクトはコンストラクタを持たないため、newキーワード付きでは実行できず、また関数として実行することもできない。

　JSONオブジェクトは次のメソッドを持つ。

```
JSON.parse(text [, reviver])	textをJSON文字列としてパースしECMAScriptオブジェクト/値を生成する。関数オブジェクトであるreviverが与えられた場合、この関数に対しthisとしてプロパティを含むオブジェクトを、引数にプロパティ名と値を与えて実行してこの値を変換できる
JSON.stringify(value, [, replacer [, space]])	valueをJSON文字列に変換する。関数オブジェクトであるreplacerが与えられた場合、引数にプロパティ名と値を与えて実行してその値を変換できる。spaceがtrueだった場合、変換結果を整形する。
JSON[@@toStringTag]	"JSON"
```

