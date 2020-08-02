---
slug: read-ecmascript2015-specification-part21
title: ECMAScript 2015の仕様書を読む（その21）
tags: [ ecmascript,javascript ]
date: 2016-05-31T00:26:16+09:00
lastmod: 2016-05-31T00:26:16+09:00
publishDate: 2016-05-31T00:26:16+09:00
---


　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はリフレクションやプロキシ、モジュール名前空間に関連するオブジェクトに関する第26章。

## 第26章第1節


　Reflectオブジェクトについて。Reflectオブジェクトは内部オブジェクトとして定義されているオブジェクトで、グローバルオブジェクトのReflectプロパティの初期値になっている。関数オブジェクトではないので直接このオブジェクトを実行することはできないし、newキーワードを使って直接コンストラクタを呼び出すこともできない。

　Reflectオブジェクトは以下のプロパティ/メソッドを持つ。これらはObjectと同名のものもあるが、targetがオブジェクトでない場合必ずTypeErrorを発生させる点が異なる。

```
Reflect.apply(target, thisArgument, argumentsList)	target関数をargumentsListを引数として与えて実行する。このときthisにはthisArgumentが渡される
Reflect.construct(target, argumentsList [, newTarget])	targetを元に新たにオブジェクトを作成する。このときargumentsListを引数としてコンストラクタが実行される。newTargetがあ場合、これをコンストラクタとして使う。
Reflect.defineProperty(target, propertyKey, attributes)	targetにpropertyKeyという名前でプロパティを追加し、値にattributesをセットする
Reflect.deleteProperty(target, propertyKey)	targetのproprtyKeyプロパティを削除する
Reflect.enumerate(target)	targetのenumerableなプロパティに帯するiteratorを返す
Reflect.get(target, proertyKey [, receiver])	tagetのpropertyKeyプロパティを取得する。receiverが指定された場合、これをthisとして使用する
Reflect.getOwnPropertyDescriptor(target, propertyKey)	targetのpropertyKeyのPropertyDescriptorを返す
Reflect.getPrototypeOf(target)	targetのprototypeを返す
Reflect.has(target, propertyKey)	targetがpropertyKeyプロパティを持っていたらtrueを返す
Reflect.isExtensible(target)	targetがextensibleならtrue
Reflect.ownKeys(target)	targetが独自に持つプロパティキーの配列を返す
Reflect.preventExtensions(target)	targetの拡張を禁止する
Reflect.set(target, propertyKey, V [, receiver])	targetのpropertyKeyプロパティにVをセットする。receiverが与えられた場合、これをthisとする。
Reflect.setPrototypeOf(target, proto)	targetのプロトタイプをprotoに設定する
```

## 第26章第2節


　Proxyオブジェクトについて。Proxyオブジェクトは、あるオブジェクトについて、これを変更することなくそのプロパティやメソッドに対する挙動を追加・変更するために使われるオブジェクトである。

　ProxyオブジェクトはグローバルオブジェクトのProxyプロパティの初期値。Proxyコンストラクタは(target, handler)という引数を取り、targetをベースとした新たなproxyオブジェクトを作成する。このオブジェクトのプロパティにアクセスしたり、メソッドを実行しようとするとhandler関数が実行される。なおProxyオブジェクトは通常の関数としての実行は不可で、newキーワード無しで実行するとTypeErrorとなる。

　また、ProxyオブジェクトはProxy.revocable(target, handler)というメソッドを持つ。このメソッドは取り消し可能な（proxyを無効にできる）proxyオブジェクトを返す。このオブジェクトはproxy自体を格納するproxyプロパティおよびproxyを無効にするrevokeメソッドを持つ。

## 第26章第3節


　モジュール名前空間オブジェクト（Module Namespace Object）について。このオブジェクトはimportキーワードを使ってモジュールをロードした際に生成される。@@toStringTagプロパティおよび[@@iterator]()メソッドを持ち、前者は"Module"を返す。後者はモジュールの名前空間に登録されているキーに対するiteratorを返す。

