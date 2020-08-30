---
slug: read-ecmascript2015-specification-part5
title: ECMAScript 2015の仕様書を読む（その5）
tag: [ ecmascript.javascript ]
date: 2016-03-27T21:35:37+09:00
lastmod: 2016-03-27T21:35:37+09:00
publishDate: 2016-03-27T21:35:37+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を読んでいます。今回はモジュールの説明がある第15章。新機能であるモジュールのexport/importについて説明されている。

## 第15章


　スクリプトとモジュールについて。ESMAScript 2015では新たにモジュールという概念が投入されている。モジュールではexportやimport文を使ってモジュール外からアクセスできる要素を指定できる。

　import文では、ほかのモジュール内のメソッドやプロパティを現在のモジュール内で参照できるよう読み込むことができる。まず、下記のようにすると指定したモジュールがインポートされる。

```
import モジュール名
```

　また、次のようにしてモジュール内の指定した要素のみをインポートできる。

```
import 要素 from　モジュール名
import * as 名前 from　モジュール名
import {} from モジュール名
import {インポートする要素1 [, 要素2 [,...]]} from　モジュール名
 from　モジュール名
```

　要素の後に「as 名前」を続けることでインポートする要素を参照するための名前を指定できる。

　export文では、モジュールで公開する要素を指定できる。

```
export * from モジュール名;
export {要素1 [, 要素2, [,...]} from モジュール名;
export {要素1 名前[, 要素2, [,...]} from モジュール名;
export {要素1 [, 要素2, [,...]};
export 変数
export 宣言
export default 各種宣言
```

　要素の後に「as 名前」を続けることでエクスポートする要素を参照するための名前を指定できる。

　それぞれの挙動の違いは、15.2.1.16で説明されているが、次のような解釈になる。

```
import v from "mod";
```

　→modモジュールのdefaultオブジェクトをvという名前で参照可能にする

```
import * as ns from "mod";
```

　→modモジュールのオブジェクトをnsオブジェクト経由で参照可能にする

```
import {x} from "mod";
```

　→modモジュールのxオブジェクトをxという名前で参照可能にする

```
import {x as v} from "mod";
```

　→modモジュールのxオブジェクトをvという名前で参照可能にする

```
import "mod";
```

　→modモジュールを読み込むがいずれのオブジェクトも参照可能とはしない

```
export var v;
```

　→モジュールのvオブジェクトをvという名前で参照可能にする

```
export default function f() {};
```

　→モジュールの関数fをdefaultという名前で参照可能にする

```
export default function () {};
export default 42;
```

　→指定した関数や値をdefaultという名前で参照可能にする

```
export {x};
```

　→xオブジェクトをxという名前で参照可能にする

```
export {v as x};
```

　→vオブジェクトをxという名前で参照可能にする

```
export {x} from "mod";
```

　→指定したモジュールのxオブジェクトをxという名前で参照可能にする

```
export {v as x} from "mod";
```

　→指定したモジュールのvオブジェクトをxという名前で参照可能にする

```
export * from "mod";
```

　→指定したモジュールのすべてのオブジェクトを参照可能にする

