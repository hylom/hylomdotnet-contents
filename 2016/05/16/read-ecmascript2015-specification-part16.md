---
slug: read-ecmascript2015-specification-part16
title: ECMAScript 2015の仕様書を読む（その16）
tag: [ ecmascript, javascript ]
date: 2016-05-16T22:56:04+09:00
lastmod: 2016-05-16T22:56:04+09:00
publishDate: 2016-05-16T22:56:04+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はTypedArrayなどについて規定する第22章2節。

## 第22章2節



　TypedArrayはバイナリデータを格納するための配列状オブジェクト。格納可能な要素はInt8/Uint8/Uint8C/Int16/Uint16/Int32/Uint32/Float32/Float64のいずれかで、各要素はすべて同じ型である必要がある。各型ごとに異なる次の関数オブジェクトがコンストラクタとして用意されている。

```
Int8Array
Uint8Array
Uint8ClampedArray
Int16Array
Uint16Array
Int32Array
Uint32Array
Float32Array
Float64Array
```

　これらはすべて同じ引数を持ち、また同じprototypeを持つので、以下ではこれらのオブジェクトを%TypedArray%と表記する。

　%TypedArray%は異なる引数を持つ複数の形式で関数として呼び出せる。ただし、これらはすべてnewキーワード付き呼び出す必要がある。newキーワードなしで呼び出すと、TypeErrorを返す。

　コンストラクタに与えられる引数とその際の動作は下記のとおり。

```
%TypedArray%()	空のTypedArrayを返す
%TypedArray%(length)	指定した数の要素を持つTypedArrayを返す。各要素は0に設定される
%TypedArray%(typedArray)	typedArrayと同じ要素を持つTypedArrayを返す
%TypedArray%(object)	objectを元にTypedArrayを作成して返す
%TypedArray%(buffer [, byteOffset [, length]])	bufferのbtyeOffsetからlengthまでの部分を格納したTypedArrayを作成して返す
```

　%TypedArray%は下記のメソッド/プロパティを持つ。

```
%TypedArray%.from(source [, mapfn [, thisArg]])	sourceオブジェクトからTypedArrayを作成して返す。mapfnが指定された場合はこの関数を用いたmap処理が行われたあとに作成されたTypedArrayを返。
%TypedArray%.of(...items)	itemsを要素として持つTypedArrayを作成して返す
%TypedArray%[@@species]	gettter。thisを返す
```

　%TypedArray%.prototypeは下記のメソッド/プロパティを持つ。なお、とくに説明のないものについてはArray.prototypeの同名メソッド/プロパティと同じ処理を行う。

```
%TypedArray%.prototype.buffer	getter。格納するデータをbuffer形式で返す
%TypedArray%.prototype.byteLength	getter。格納するバイト数を返す
%TypedArray%.prototype.byteOffset	getter。byteOffsetを返す
%TypedArray%.prototype.constructor	コンストラクタ
%TypedArray%.prototype.copyWithin(target, start [, end])
%TypedArray%.prototype.entries()
%TypedArray%.prototype.every(callbackfn [, thisArg])
%TypedArray%.prototype.fill(value, [, start [, end]])
%TypedArray%.prototype.filter(callbackfn [, thisArg])
%TypedArray%.prototype.find(predicate [, thisArg])
%TypedArray%.prototype.findIndex(predicate [, thisArg])
%TypedArray%.prototype.forEach(callbackfn [, thisArg])
%TypedArray%.prototype.indexOf(searchElement [, fromIndex])
%TypedArray%.prototype.join(separator)
%TypedArray%.prototype.keys()
%TypedArray%.prototype.lastIndexOf(searchElement [, fromIndex])
%TypedArray%.prototype.length	格納する要素数
%TypedArray%.prototype.map(callbackfn [, thisArg])
%TypedArray%.prototype.reduce(callbackfn, [initialValue])
%TypedArray%.prototype.reduceRight(callbackfn, [initialValue])
%TypedArray%.prototype.set(overloaded [, offset])	第一引数からデータを読み込む。型によって処理が異なる
%TypedArray%.prototype.set(array [, offset])	arrayからデータを読み込む
%TypedArray%.prototype.set(typedArray [, offset])	typedArrayからデータを読み込む
%TypedArray%.prototype.slice(start, end)
%TypedArray%.prototype.some(callbackfn [, thisArg])
%TypedArray%.prototype.sort(comparefn)
%TypedArray%.prototype.subarray([begin [, end]])	部分配列を返す。この部分配列はバッファを共有する
%TypedArray%.prototype.toLocaleString([reserved1 [, reserved2]])
%TypedArray%.prototype.toString()
%TypedArray%.prototype.values()
%TypedArray%.prototype[@@iterator]()
%TypedArray%.prototype.[@@toStringTag]  getter。名前を返す
```

　なお、内部的に基底クラスとしてTypedArrayというものは存在するが、これをECMAScript 2015から直接操作することはできない。

　TypedArray.BYETS_PER_ELEMENTおよびTypedArray.prototype.BYTES_PER_ELEMENTで各要素のバイト数を参照できる。

