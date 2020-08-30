---
slug: es6-class-vs-function-keyword
title: ECMAScript 2015（ES6）でのクラス定義におけるclassキーワードとfunctionキーワードの違い
tag: [ ecmascript, javascript ]
date: 2016-06-07T00:58:08+09:00
lastmod: 2016-06-07T01:01:53+09:00
publishDate: 2016-06-07T00:58:08+09:00
---

　ECMAScript 2015では、新たにクラスを定義するためのclassキーワードが導入されている。MDNで提供されているドキュメントの「[Classes](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes)」ページでは、「ECMAScript 6 で導入されたクラス構文は、既存のプロトタイプによるオブジェクト指向の糖衣構文です」と記述されている。しかし、厳密にチェックするとclassキーワードで定義したクラスとfunctionキーワードで定義したクラスは（実用上問題ないレベルで）挙動が微妙に異なる。その違いを検証してみよう。なお、検証に使用した環境はNode.js v6.2.1である。

```
$ node -v
v6.2.1
```

## 宣言方法の違い


　functionキーワードを使ってクラスを定義する場合、次のようにコンストラクタとしてクラス名を持つ関数を定義するのが一般的だ。

```
> function VectorFunction(x, y) {
... this.x = x;
... this.y = y;
... }
undefined
```

　いっぽうclassキーワードを利用する場合、次のようにconstructor関数を使ってクラスのコンストラクタを定義する。

```
> class VectorClass {
... constructor(x, y) {
..... this.x = x;
..... this.y = y;
..... }
... }
[Function: VectorClass]
```

　classキーワードを利用した場合でも、作成されるのはあくまでFunctionオブジェクト（＝関数）である。

## newキーワードなしで実行した際の挙動の違い


　これらのクラスのインスタンスを作成するには、この関数をnewキーワード付きで実行する。

```
> v1 = new VectorFunction(3, 4)
VectorFunction { x: 3, y: 4 }
> v2 = new VectorClass(3, 4)
VectorClass { x: 3, y: 4 }
```

　この挙動はどちらの場合も同じだ。しかし、newキーワード無しでクラスを関数として実行した場合、functionキーワードを使って定義したクラスとclassキーワードを使って定義したクラスは挙動が異なる。

　functionキーワードを使って定義したクラスは、newキーワード無しで関数として実行すると意図しない結果を生み出すことがある。なぜなら、newキーワード無しで関数を実行した場合、this変数にglobalオブジェクト（strict modeの場合はundefined）が渡されるからだ。

　たとえば今回のケースでは、非strict modeの場合グローバルオブジェクトのプロパティが勝手に変更されてしまう。

```
> x = 0
0
> y = 0
0
> v1 = VectorFunction(3, 4)
undefined
> x
3
> y
4
```

　いっぽう、classキーワードで定義したクラスはそのまま実行することはできず、TypeErrorが発生する。

```
> v2 = VectorClass(3, 4)
TypeError: Class constructor VectorClass cannot be invoked without 'new'
    at repl:1:6
    at REPLServer.defaultEval (repl.js:272:27)
    at bound (domain.js:280:14)
    at REPLServer.runBound [as eval] (domain.js:293:12)
    at REPLServer.<anonymous> (repl.js:441:10)
    at emitOne (events.js:101:20)
    at REPLServer.emit (events.js:188:7)
    at REPLServer.Interface._onLine (readline.js:224:10)
    at REPLServer.Interface._line (readline.js:566:8)
    at REPLServer.Interface._ttyWrite (readline.js:843:14)
```

　ECMA-262の「14.5.14 Runtime Semantics: ClassDefinitionEvaluation」および「9.2.9 MakeClassConstructor(F)」で説明されているが、classキーワードでクラスを定義した場合、生成されたFunctionオブジェクトの「FunctionKind」内部スロットに「classConstructor」という値がセットされる。この内部スロットはFunctionオブジェクトの種別を格納するもので、「normal」および「classConstructor」、「generator」のいずれかを持つ（「9.2 ECMAScript Function Objects」）。FunctionKind内部スロットの値がclassConstructorの場合、関数を実行する際に実行される「Call」内部メソッドの実行時にTypeError例外が送出される（「9.2.1 [[Call]] ( thisArgument, argumentsList)」）。なお、FunctionKind内部スロットの値がclassConstructorになるのは、classキーワードでクラスを定義した場合のみである。

## 所有するプロパティの違い


　classキーワードで定義したクラスは、functionキーワードで定義したクラスと異なり「caller」および「arguments」プロパティを持たない。

```
> Object.getOwnPropertyNames(VectorFunction)
[ 'length', 'name', 'arguments', 'caller', 'prototype' ]
> Object.getOwnPropertyNames(VectorClass)
[ 'length', 'name', 'prototype' ]
```

　また、classキーワードで定義したクラスのprototypeプロパティはwritableではないが、functionキーワードで定義したクラスのprototypeプロパティはwritableである。

```
> Object.getOwnPropertyDescriptor(VectorFunction, "prototype")
{ value: VectorFunction {},
  writable: true,
  enumerable: false,
  configurable: false }
> Object.getOwnPropertyDescriptor(VectorClass, "prototype")
{ value: VectorClass {},
  writable: false,
  enumerable: false,
  configurable: false }
```

　もちろん、どちらの場合もprototypeオブジェクトにプロパティ/メソッドを追加することは可能だ。

```
> VectorFunction.prototype.norm = function () {
... return Math.sqrt(this.x * this.x + this.y * this.y);
... }
[Function]
> VectorClass.prototype.norm = function () {
... return Math.sqrt(this.x * this.x + this.y * this.y);
... }
[Function]
```

　このようにして定義したメソッドは、どちらも同じように実行することが可能だ。

```
> v1 = new VectorFunction(3, 4)
VectorFunction { x: 3, y: 4 }
> v1.norm()
5
> v2 = new VectorClass(3, 4)
VectorClass { x: 3, y: 4 }
> v2.norm()
5
```


## functionキーワードを使ったクラス宣言でしかできないこと


　classキーワードを使ってクラスを宣言すると、そのクラス自体を関数として実行することができなくなる。多くの場合でこのこと自体にデメリットはないが、意図的に（newキーワードなしに）クラスを関数として実行したいというケースも考えられる。たとえば次の例は、strict modeではnewキーワード無しにクラスを関数として実行した場合にthis変数がundefinedになることを利用し、newキーワード付きで実行した場合とnewキーワード無しで実行した場合とで異なる処理を行わせるものだ。

```
$ node --use_strict
> function Vector(x, y) {
... if (this === undefined) {
..... return new Vector(x, y);
..... }
... this.x = x;
... this.y = y;
... }
undefined
> Vector(3, 4)
Vector { x: 3, y: 4 }
> new Vector(3, 4)
Vector { x: 3, y: 4 }
```

　このようにして定義したVectorクラスは、newキーワードがあっても無くとも同様にVectorクラスのインスタンスを返す。





