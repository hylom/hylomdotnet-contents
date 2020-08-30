---
slug: read-ecmascript2015-specification-part7
title: ECMAScript 2015の仕様書を読む（その7）
tag: [ ecmascript, javascript ]
date: 2016-04-13T01:26:05+09:00
lastmod: 2016-04-14T00:05:09+09:00
publishDate: 2016-04-13T01:26:05+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を読んでいます。今回は基本オブジェクト（Fundamental Objects）についての第19章のうち、Objectオブジェクトについて。

## 第19章第1節


　ECMAScript 2015では基本オブジェクトとしてObject、Function、Boolean、Symbol、Errorの5つのオブジェクトが用意されている。どのオブジェクトも関数オブジェクトであり、コンストラクタとして呼び出すことができる。第1節では、Objectオブジェクトについて説明されている。

　Objectオブジェクトをnewキーワードを付けずに関数として呼び出すと、その引数をオブジェクト化したものを返す。たとえば数値を引数に与えた場合、その数値をNumberオブジェクトにしたものを返す。引数がnullやundefinedだった場合は新たに空のオブジェクトを作成して返す。また、newキーワード付きで呼び出すと、その引数で指定したオブジェクトのコンストラクタにその引数を与えて実行した結果を返す。たとえば、「new Object("hoge")」は「new String("hoge")」と同じ結果となる。

　Objectオブジェクトは次のメソッド/プロパティを持つ。

```
Object.assign(target, ...sources)	sourcesオブジェクトのenumerableなプロパティを、その添え字をキー、値を値としてtargetオブジェクトにコピーする。戻り値はtargetオブジェクト
Object.create (O[, Properties])	Oオブジェクトを元に新しいオブジェクトを作成する
Object.defineProperties(O, Properties)	Oオブジェクトにプロパティを追加する。そのプロパティがすでに定義されていた場合は指定されたものに更新する。Propertiesはキーとして対象のプロパティ、値としてそのプロパティの情報（ディスクリプタ）を格納したオブジェクトを持つオブジェクト
Object.defineProperty(O, P, Attributes)	OオブジェクトにPプロパティを追加する。Attributesはそのプロパティの情報を格納したオブジェクト（ディスクリプタ）
Object.freeze(O)	Oオブジェクトをフリーズする。フリーズされた（frozen）オブジェクトは変更ができなくなる
Object.getOwnPropertyDescriptor(O, P)	OオブジェクトのPプロパティのディスクリプタを返す
Object.getOwnPropertyNames(O)	Oオブジェクトのプロパティ名一覧を含む配列を返す
Object.getOwnProertySymbols(O)	Oオブジェクトのシンボル一覧を含む配列を返す
Object.getPrototypeOf(O)	Oオブジェクトのプロトタイプを返す
Object.is(value1, value2)	value1とvalue2が同じ値であればtrueを返す
Object.isExtensible(O)	Oオブジェクトが拡張可能であればtrueを返す
Object.isFrozen(O)	Oオブジェクトがフリーズされていればtrueを返す
Object.isSealed(O)	Oオブジェクトがsealed状態であればtrueを返す
Object.keys(O)	Oオブジェクトのプロパティ名一覧を含む配列を返す
Object.preventExtensions(O)	Oオブジェクトの拡張を禁止する。拡張が禁止されたオブジェクトには、新たなプロパティを追加できなくなる
Oject.prototype	オブジェクトのプロトタイプを格納するプロパティ
Object.seal(O)	Oオブジェクトをsealed状態にする。sealed状態のオブジェクトに対しては新たなプロパティを追加できず、またプロパティの設定を変更できなくなる
Object.setProtptypeOf(O, proto)	Oオブジェクトのプロトタイプをprotoオブジェクトに変更する
```

　オブジェクトのプロパティには「データプロパティ（Data Property）」と「アクセサプロパティ（Accessor Proerty）」がある。Dataプロパティは「Value」「Writable」「Enumerable」「Configurable」という属性を持つ。また、アクセサプロパティは「Get」「Set」「Enumerable」「Configurable」という属性を持つ（6.1.7.1）。これら属性を設定/変更するのがdefinePropertiesやdefineProperty。各属性の説明は下記の通り。

```
Value	そのプロパティに設定された値
Writable	プロパティへの値の書き込みが可能かどうか（Boolean）
Enumerable	そのプロパティがfor-inループでの列挙対象となるか（Boolean）
Configurable	そのプロパティの削除や属性変更が可能かどうか（Boolean）
Get	プロパティに対応するgetter関数
Set	プロパティに対応するsetter関数
```

　これらを以下のような形で格納したオブジェクトはプロパティディスクリプタと呼ばれる。

```
{
  value: 値,
  writable: (true|false),
  enumerable: (true|false),
  ...
}
```

　オブジェクトには拡張の不可や「frozen」や「sealed」といった「Ingegrity Level」を設定できる。まず拡張の不可だが、拡張が不可である場合オブジェクトに新しいプロパティを追加できなくなる（削除は可能）。また、sealed状態のオブジェクトは拡張不可となり、さらに各プロパティの属性が変更不可能になる（プロパティのconfigurable属性がfakseになる）。データプロパティの値を変更することは可能。いっぽうfrozen状態のオブジェクトは拡張不可で各プロパティの属性は変更できなくなる点はsealedと同じだが、さらにデータプロパティの値変更も不可となる（プロパティのwritable属性がfalseになる）。ただし、setter/getterについては実行可能。

　また、Object.prototypeオブジェクトは次のメソッド/プロパティを持つ。

```
Object.prototype.constructor	オブジェクトのコンストラクタ。デフォルトはObjectに相当する内部オブジェクト
Object.prototype.hasOwnProperty(V)	Vプロパティを持っていればtrue
Object.prototype.isPrototypeOf(V)	Vオブジェクトのプロトタイプがオブジェクトのプロトタイプと一致すればtrueを返す
Object.prototype.propertyIsEnumerable(V)	Vプロパティが列挙可能であればtrueを返す
Object.prototype.toLocaleString([reserved1[ , reserved2]])	オブジェクトのtoStringメソッドを実行しその結果を返す。現状Array、Number、Date、Typed Arraysのみが固有のtoLocaleStringを持つ
Object.prototype.toString()	オブジェクトが持つ情報を文字列に変換して返す
Object.prototype.valueOf()	オブジェクトのプリミティブ値を返す
```

