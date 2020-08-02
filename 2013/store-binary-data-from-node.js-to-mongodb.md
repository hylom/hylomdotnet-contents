---
slug: store-binary-data-from-node.js-to-mongodb
title: Node.jsからMongoDBにバイナリデータを格納する
tags: [ Node.js,MongoDB,programming ]
date: 2013-04-16T02:25:39+09:00
lastmod: 2013-04-16T23:34:48+09:00
publishDate: 2013-04-16T02:25:39+09:00
---

<p>　MongoDBにデータを格納する場合、格納するデータをプロパティとして持つオブジェクトを引数にコレクションのinsertメソッドを実行する。もしバイナリデータをデータベースに格納したい場合、バイナリデータをBuffer型のオブジェクトとして与えればよい。ただし、MongoDBに格納するドキュメント（データを格納する単位。SQLデータベースの1行に相当する）には最大4MBというサイズ制限がある。そのため、格納できるバイナリデータの上限は4MBだ。</p>

<p>　次のサンプルコードは、引数で指定したファイルを読み込んでデータベースに格納するものだ。</p>

<iframe src="/embed/https://gist.github.com/hylom/5383726.js"></iframe>

<p>　データベースに格納するオブジェクトを用意しているのが42行〜45行の部分だ。ここでdataオブジェクトは読み出したデータを格納しているBuffer型のオブジェクトとなっている。</p>

<p>　ちなみに、格納されたデータをmongoシェルで確認すると、BASE64でエンコードされた形で表示される。</p>

<pre class="console">
$ <strong>node store-to-mongodb.js ./test/sample.JPG</strong>
insert succeeded.
 
$ <strong>mongo test01</strong>
> <strong>db.images.find()</strong>
{ "filename" : "sample.JPG", "data" : BinData(0,"/9j/4AAQSkZJRgABAQEAtAC0AAD/4gxYSUNDX1BST0ZJTEUAAQEAAAxITGlubwIQAABtbnRyUkdCIFhZWiAHzgACAAkABgAxAABhY3NwTVNGVAAAAABJRUMgc1JHQgAAAAAAAAAAAAAAAAAA9tYAAQAAAADTLUhQICAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
：
：
</pre>

<p>　逆にデータベースからバイナリデータを読み出した場合、読み出したバイナリデータはmongodb.Binary型のオブジェクトに格納される（<A href="http://mongodb.github.io/node-mongodb-native/api-bson-generated/binary.html">mongoDB Node.js Driverのドキュメント</a>）。このオブジェクトから格納しているデータを取り出すには、readメソッドを使用する。オブジェクトのbufferプロパティを直接参照することでもバイナリデータにアクセスできるのだが、ドキュメントにはこのプロパティが明示されていないので、readメソッドを使用したほうが確実だ。</p>

<pre class="definition">
binary.read(position, length)
</pre>

<p>　ここでposition引数にはデータの読み出しを開始するオフセットを、length引数には読み出すバイト数を指定する。</p>

<p>　次の例は、読み出したデータをファイルに保存するものだ。</p>

<iframe src="/embed/https://gist.github.com/hylom/5383731.js"></iframe>

<p>　データの取り出し処理をしているのは60〜61行の部分だ。まずlengthメソッドでバイナリのサイズを取得してlen変数に格納し、0バイト目からlen変数で指定したサイズまで、つまりバイナリの最初から最後までを取り出してコールバック関数を実行している。</p>
