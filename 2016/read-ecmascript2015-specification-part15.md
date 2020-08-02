---
slug: read-ecmascript2015-specification-part15
title: ECMAScript 2015の仕様書を読む（その15）
tags: [ ecmascript,javascript ]
date: 2016-05-13T01:40:34+09:00
lastmod: 2016-05-16T22:55:44+09:00
publishDate: 2016-05-13T01:40:34+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回は配列（Array）などについて規定する第22章第1節。

## 第22章第1節


　Arrayオブジェクトは特別なオブジェクトであり、例外的なプロパティ名を持つ。Arrayオブジェクトを関数として実行すると、新たなArrayオブジェクトを作成して返す。newキーワード付きの場合も同じ処理を行う。また、Arrayコンストラクタは拡張可能で、そのサブクラスはコンストラクタ内でsuperキーワードを使ってArrayコンストラクタを呼び出してオブジェクトを初期化する必要がある。

　Arrayコンストラクタは引数の数によって処理が変わる。引数が無い場合、空の配列を返す。1つの引数を与えた場合、その引数がNumberでかつその値がUint32に変換したものと等しい場合、長さがその値に等しく、かつ各要素がundefinedの配列を作成して返す。そうでない場合、その値を含む長さ1の配列を返す。2つ以上の引数が与えられた場合、それらを格納する配列を返す。

　Arrayオブジェクトは次のプロパティ/メソッドを持つ。

```
Array.from(items [, mapfs [, thisArg]])	mapfs関数にitems引数の各要素を与えて実行した結果を格納した配列を返す。また、thisArgが指定された場合、mapfsを実行時にそれをthisとして使用する。items引数はiterableなものであれば何でも良い
Array.isArray(arg)	argがArrayであればtrueを返す
Array.of(...items)	引数を値として格納した配列を返す
```

　Array.prototypeは内部オブジェクトであり、書き換えは不可能。また、Array[@@species]というアクセサプロパティを持つ。値はundefined。

　Array.prototypeプロパティは下記のプロパティ/メソッドを持つ。なお、thisArg引数はcallbackfnを実行する際にthisとして使用するオブジェクトである。また、startが負の場合、length+startが指定されたものとして処理が行われる。endが指定されなかった場合lengthが、endが負の場合length+endが指定されたものとして処理される。

```
Array.prototype.concat(...arguments)	引数を値として拝謁の末尾に追加する。引数が配列だった場合、その各要素を追加する
Array.prototype.constructor	コンストラクタ
Array.prototype.copyWithin(target, start [, end])	配列内のstartからendまでをtargetの位置から順に格納する
Array.prototype.entries()	[インデックス, 値]をvalue要素に格納するiteratorを返す
Array.prototype.every(callbackfn [, thisArg])	各要素を引数としてcallbackfnを実行し、すべてがtrueならtrueを返す
Array.prototype.fill(value [, start [, end]])	startからendまでの要素をvalueに設定する
Array.prototype.filter(callbackfn [, thisArg])	各要素を引数としてcallbackfnを実行し、trueを返したもののみを含む配列を作成して返す
Array.prototype.find(predicate [, thisArg])	各要素を引数としてpredicateを実行し、trueを返した場合その値を返す。predicateは要素、インデックス、対象の配列という3つの引数が与えられる
Array.prototype.findIndex(predicate [, thisArg])	findと同様の処理を行う。findとは異なり、インデックスを返す
Array.prototype.forEach(callbackfn [, thisArg])	各要素を引数としてcallbackfnを実行する。undefinedを返す
Array.prototype.indexOf(searchElement [, fromIndex])	searchElementと一致する要素のインデックスを返す。fromIndexが指定された場合、その位置から検索を開始する。比較には===演算子が使われる
Array.prototype.join(separator)	各要素を文字列に変換し、separatorを介して連結したものを返す。separatorがundefinedだった場合、","が使われる
Array.prototype.keys()	各キーをvalue要素に格納するiteratorを返す
Array.prototype.lastIndexOf(searchElement [, fromIndex])	searchElementと一致する最後の要素のインデックスを返す。fromIndexが指定された場合、その位置から検索を開始する。比較には===演算子が使われる
Array.prototype.map(callbackfn [, thisArg])	各要素を引数としてcallbackfnを実行し、その結果を含む配列を返す
Array.prototype.pop()	配列の最後の要素を削除してそれを返す
Array.prototype.push(...items)	引数として与えられた値をそれぞれ配列の最後に追加する
Array.prototype.reduce(callbackfn [, initialValue])	各要素を引数としてcallbackfnを実行する。callbackfnには直前に実行されたcallbackfnの戻り値、配列の要素、配列のインデックス、配列の4つの引数が与えられる。initialValueが指定された場合、それが最初に実行されるcallbackfnの第1引数となる。最後に実行されたcallbackfnの戻り値を返す
Array.prototype.reduceRight(callbackfn, [, initialValue])	reduceを逆方向に実行する
Array.prototype.reverse()	配列の要素の順序を逆にする
Array.prototype.shift()	配列の最初の要素を削除して返す
Array.prototype.slice(start, end)	startからendまでの要素を含む配列を返す
Array.prototype.some(callbackfn [, thisArg])	各要素を引数としてcallbackfnを実行し、いずれかがtrueを返したらtrueを返す
Array.prototype.sort(comparefn)	comparefnを比較関数としてソートを実行する
Array.prototype.splice(start, deleteCount, ...items)	startからdeleteCount個の要素を取り除き、そこにitemsで与えた各要素を追加する
Array.prototype.toLocaleString([reserved1 [, reserved2]])	ECMA-402で定義された地域課文字列を返す
Array.prototype.toString()	配列を文字列に変換する
Array.prototype.unshift(...items)	配列の最初に要素を追加しそのlengthを返す
Array.prototype.values()	各要素をvalue要素に格納するiteratorを返す
Array.prototype[@@iterator]()	valuesと同じ
Array.prototype[@@unscopables]	["copyWithin", "entries", "fill", "find", "findIndex", "includes", "keys", "values"]
```

　Arrayインスタンスはlengthプロパティを持つ。また、Arrayオブジェクトのiteratorはnext()のほか、[@@toStringTag]要素を持つ。

