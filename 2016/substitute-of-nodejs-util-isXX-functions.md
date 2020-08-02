---
slug: substitute-of-nodejs-util-isXX-functions
title: Node.js 4.xで廃止となったutil.is系メソッドの代替案
tags: [ javascript,nodejs ]
date: 2016-02-15T18:13:43+09:00
lastmod: 2016-02-16T01:17:59+09:00
publishDate: 2016-02-15T18:13:43+09:00
---

<P>
Node.jsの最新長期サポート版（LTS）であるv4.3.0では、それまで利用できたutil.isArray()やutil.isRegExp()、util.isDate()などのメソッドがDeprecated（廃止予定）扱いとなっています（<A href="https://nodejs.org/dist/latest-v4.x/docs/api/util.html">v4.x系のドキュメント</a>、<A href="https://nodejs.org/docs/latest-v0.12.x/api/util.html">v0.12.x系のドキュメント</a>）。
</p><p>
ドキュメントには理由が説明されておらず、代替案も掲載されていないのですが、<a href="http://stackoverflow.com/questions/32515413/why-have-many-util-is-functions-been-deprecated-in-node-js-v4-0-0">StackOverflowでの情報</a>によると、「後方互換性がなくなるために修正したくないから」だそうです。例としてutil.isObject()に関数オブジェクトを与えると戻り値はfalseになりますが、JavaScript（ECMAScript）の言語仕様上は関数オブジェクトもオブジェクトであり、これは不適切な実装であることが挙げられています。
</p><p>
isArrayとかisStringとかはあっても良いのでは……と思いますが、まあほかのコードで代替可能なのでコアからは削除する、というのは理解できます。ということで代替案ですが、下記のように<A href="https://developer.mozilla.org/ja/docs/JavaScript/Reference/Operators/instanceof">isinstanceof</a>演算子で代替できます。
</p>

<pre>
$ node
> [] instanceof Array
true
> [] instanceof Object
true
> [] instanceof String
false
</pre>

<p>
なお面倒臭いことに、instanceof演算子はプリミティブ型（文字列や数値型など、オブジェクトではないもの）に対してはすべてfalseを返します。そのため、プリミティブ型に対してはtypeof演算子の戻り値を使用して判断する必要があります。
</p>

<pre>
> typeof a
'string'
> typeof []
'object'
> typeof 10.1
'number'
> typeof /ABC/
'object'
</pre>


