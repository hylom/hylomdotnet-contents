---
slug: read-ecmascript2015-specification-part18
title: ECMAScript 2015の仕様書を読む（その18）
tags: [ ecmascript, javascript ]
date: 2016-05-19T02:14:55+09:00
lastmod: 2016-05-19T02:14:55+09:00
publishDate: 2016-05-19T02:14:55+09:00
---


　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はWeakMapについて規定する第23章第3節とWeakSetについて規定する第4節。

## 第23章3節


　WeakMapはキー/値のペアを格納するオブジェクト。Mapとは異なり、キーにはオブジェクトしか使用できない。さらにWeakMapではキーを列挙する手段が提供されていない。WeakMapでは格納するキーに対し弱参照のみを保持する。そのため、キーとして使われたオブジェクトがgarbage collectionで回収された場合、WeakMap内からそのキーおよび対応付けられた値は削除される。

　WeakMapコンストラクタはサブクラス化可能にデザインされている。その場合、サブクラスのコンストラクタ内ではsuperキーワードを使ってWeakMapコンストラクタを呼び出してインスタンスの初期化を行う必要がある。

　WeakMapオブジェクトを関数として実行する場合、newキーワード付きで実行する必要がある。引数にはiterableなオブジェクトを取る。

　WeakMapオブジェクトはprototypeプロパティを持つ。WeakMap.prototypeオブジェクトは下記のメソッド/プロパティを持つ。

```
WeakMap.prototype.constructor	コンストラクタ
WeakMap.prototype.delete(key)	keyに対応するキー/値のペアを削除する
WeakMap.prototype.get(key)	keyに対応する値を返す
WeakMap.prototype.has(key)	keyに対応するキーがあればtrue
WeakMap.prototype.set(key, value)	keyに対応する値をvalueにセットする
WeakMap.prototype[@@toStringTag]	"WeakMap"
```


## 第23章4節


　WeakSetはオブジェクトのセットを格納するオブジェクト。Setとは異なり、オブジェクトしか格納できない。WeakMapと同様、格納されているオブジェクトを列挙する手段は提供されておらず、格納するオブジェクトに対し弱参照のみを保持する。

　WeakSetコンストラクタはサブクラス化可能にデザインされている。その場合、サブクラスのコンストラクタ内ではsuperキーワードを使ってWeakSetコンストラクタを呼び出してインスタンスの初期化を行う必要がある。

　WeakSetオブジェクトを関数として実行する場合、newキーワード付きで実行する必要がある。引数にはiterableなオブジェクトを取る。

　WeakSetオブジェクトはprototypeプロパティを持つ。WeakSet.prototypeオブジェクトは下記のメソッド/プロパティを持つ。

```
WeakSet.prototype.add(value)	valueをセットに追加する
WeakSet.prototype.constructor	コンストラクタ
WeakSet.prototype.delete(value)	valueに対応する値をセットから削除する
WeakSet.prototype.has(value)	valueがセット内にあればtrue
WeakSet.prototype[@@toStringTag]	"WeakSet"
```

