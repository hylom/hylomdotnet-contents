---
slug: read-ecmascript2015-specification-part20
title: ECMAScript 2015の仕様書を読む（その20）
tags: [ ecmascript,javascript ]
date: 2016-05-26T23:40:32+09:00
lastmod: 2016-05-30T23:37:46+09:00
publishDate: 2016-05-26T23:40:32+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はイテレータやジェネレータ、Promise関連のオブジェクトに関する第25章。

## 第25章1節


　イテレーションについて。iterate可能なオブジェクトは、@@iteratorプロパティでそのオブジェクトに対応するiteratorを取得できる。iteratorはnextメソッドを持ち、このメソッドを実行するとIteratorResultオブジェクトを返す。このオブジェクトは次のメソッドを持つ。これらはすべてIteratorResultオブジェクトを返す。

```
next
```

　また、オプションで次のプロパティを持つ。これらはすべてIteratorResultオブジェクトを返す。

```
return
throw
```

　returnは、それ以上nextメソッドを呼び出さないことをiteratorに通知する際に実行される。また、throwはiteratorに何らかのエラーが発生したことを通知するために使われる。throwは引数にexceptionオブジェクトなどのエラー内容を格納するオブジェクトを与えることができる。

　IteratorResultオブジェクトは次のプロパティを持つ。

```
done	iterateが完了するとtrue
value	対応する値を格納する
```

## 第25章2節


　GeneratorFunctionについて。GeneratorFunctionはFunctionオブジェクトの派生オブジェクトであり、Functionオブジェクトのコンストラクタから派生した独自のコンストラクタと、Iteratorのプロトタイプから派生した独自のprototypeを持つ。GeneratorFunctionはグローバルオブジェクトではないが、下記のコードを用いて取得できる。

```
Object.getPrototypeOf(function*(){}).constructor
```

　GeneratorFunctionは関数として実行できる。newキーワードを付けても付けなくても同じ挙動を行う。サブクラス化も可能だが、その際はコンストラクタ内でsuperキーワードを使ってGeneratorFunctionオブジェクトを生成する必要がある。また、GeneratorFunctionオブジェクトはfunction*キーワードで生成できる。

　GeneratorFunctionは次のような形式で実行できる。

```
GeneratorFunction(p1, p2, ..., pn, body)
```

　bodyは実行コード、p1〜pnはそれに与える引数の識別子である。これらは通常は文字列として与えられる。

また、lengthおよびprototypeというプロパティを持つ。lengthの値は1である。GeneratorFunction.prototypeは次のプロパティを持つ。

```
GeneratorFunction.prototype.constructor	内部オブジェクト
GeneratorFunction.prototype.prototype	内部オブジェクト
GeneratorFunction.prototype[@@toStringTag]	"GeneratorFunction"
```

　また、GeneratorFunctionインスタンスはlengthおよびname、prototypeプロパティを持つ。

## 第25章3節


　ジェネレータオブジェクトについて。このオブジェクトはジェネレータ関数のインスタンスであり、IteratorとIterableインターフェイスの両方の性質を持つ。このオブジェクトはジェネレータオブジェクトのprototypeではなく、インスタンスを作成したジェネレータ関数のprototypeを引き継ぐ。つまり、GeneratorオブジェクトのprototypeオブジェクトはGeneratorFunction.prototypeである。

　Generator.prototypeは次のプロパティ/メソッドを持つ。

```
Generator.prototype.constructor コンストラクタ
Generator.prototype.next(value)	ジェネレータ関数の状態をvalueにする
Generator.prototype.return(value)	valueを返して処理を終了させる
Generator.prototype.throw(exception)	ジェネレータ関数で例外を発生させる
Generator.prototype[@@toStringTag]	"Generator"
```

　ジェネレータ関数内では、yieldキーワードの戻り値を使っているケースがある。この場合、次にジェネレータ関数が呼び出された場合にその戻り値が関数内で続く処理に渡されるわけだが、nextメソッドを利用することでその値を変更できる。

## 第25章4節


　Promiseオブジェクトについて。Promiseオブジェクトは遅延・非同期処理を行うためのオブジェクト。内部的に「Resolve」と「Reject」の2つの関数オブジェクトを保持し、またfulfilled、rejected、pendingの3つのステータスのどれか1つを持つ。

　内部で非同期処理を行っている場合など、それが終了する時点では結果が分からない関数でPromiseオブジェクトを返り値として使用することが想定されている。このオブジェクトは処理が完了するとfulfilledもしくはrejectedのステータスとなり、ステータスを監視することで並列処理が完了したのか、またその結果がどうなったのかを知ることができる。

　Promiseオブジェクトは関数としては実行できない。newキーワード付きでコンストラクタとしての実行のみが許可される。Promiseオブジェクトのコンストラクタはサブクラス化可能であるが、その場合はsuperキーワードを使ってコンストラクタ内でPromiseオブジェクトを生成する必要がある。

　PromiseのコンストラクタはPromise(executor)という形で呼び出される。executorは関数オブジェクトであり、遅延・非同期処理が完了した際に呼び出される。また、resolveとrejectという2つの引数を持つ。いずれも関数オブジェクトで、executor関数内で処理が成功したのか、それとも失敗したのかを通知するために呼び出すことができる。また、executor関数の終了（returnの実行）は遅延・非同期処理の完了を意味するのでは無く、その処理が受け付けられたというのを示すだけである。

　引数として与えられるresolve関数は、1つの引数を取る。executor関数内で対応するPromiseオブジェクトの解決を行いたい際にこの関数が呼び出され、引数には遅延・非同期処理が進められる際に得られた値が渡される。

　引数として与えられるreject関数も1つの引数を取る。executor関数内で対応するPromiseオブジェクトがrejectされ、成功しないことが分かった際にこの関数が呼び出される。引数にはrejectされたことを示す値（一般的にはErrorオブジェクト）が渡される。

　Promiseオブジェクトは次のメソッド/プロパティを持つ。

```
Promise.all(iterable)	与えられたPromiseのすべてが成功した際に成功となる新たなPromiseオブジェクトを返す
Promise.prototype	内部オブジェクト
Promise.race(iterable)	与えられたPromiseのうち、最初に完了したPromiseと同じ結果を返す新たなPromiseオブジェクトを返す
Promise.reject(r)	与えられた引数によって失敗状態となる新たなPromiseオブジェクトを返す
Promise.resolve(x)	与えられた引数によって成功状態となる新たなPromiseオブジェクトを返す
Promise[@@species]	getter
```

　また、Promise.prototypeは下記のメソッド/プロパティを持つ。

```
Promise.prototype.catch(onRejected)	Promiseが失敗したときに実行されるコールバック関数を設定する
Promise.prototype.constructor	コンストラクタ
Promise.then(onFulfilled, onRejected)	成功した際および失敗した際に実行されるコールバック関数を設定する
Promise.prototype[@@toStringTag]	"Promise"
```
