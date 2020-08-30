---
slug: express-connect-proxy-middleware
title: Express環境で一部のURLに対するリクエストのみリバースプロクシを使って転送する
tag: [ node.js, programming ]
date: 2013-03-21T01:39:53+09:00
lastmod: 2013-03-21T01:40:38+09:00
publishDate: 2013-03-21T01:39:53+09:00
---

<p>　hylom.netではNode.jsベースのCMS（nodeweblog）で運用されているが、以前はWordPressを使用して運用していた。このようなCMSの切り替えの際、過去コンテンツへのアクセスをどう処理するか、ということを考えなければならない。本来ならば旧システムでデータをエクスポートした上で適切に新システムにインポートするべきだが、今回はテスト的な運用と言うことで、別ポートでApache＋WordPressを起動し、nodeweblog内に存在しないURLに対するリクエストはリバースプロクシを使ってWordPressに転送するという方法で旧コンテンツへのアクセスを可能にしている。</p>

<p>　Node.jsを使ってリバースプロクシを構築する場合、<a href="https://github.com/nodejitsu/node-http-proxy">node-http-proxy</a>といったモジュールを利用する、もしくはリクエストハンドラ内でhttp.request関数を使用する、といった方法があるが、nodeweblogではexpressフレームワークを使っているので、<a href="https://github.com/superjoe30/connect-proxy">connect-proxy</a>というconnectミドルウェアを利用してリバースプロクシを実現してみた。</p>

<p>　connect-proxyは「proxy-middleware」というパッケージ名で提供されており、npmでインストールできる。</p>

<pre>
$ npm install proxy-middleware
</pre>

<p>　たとえば「/api」というパス名で始まるリクエストを「http://example.com/」に転送するには、ミドルウェアの設定を行う部分に以下のようなコードを追加すればよい。</p>

<pre>
var proxy = require('proxy-middleware');
var proxyOptions = url.parse('http://example.com/');
app.use(proxy(proxyOptions));
</pre>

<p>　proxy-middlewareモジュールにはリクエストを転送先のプロトコルやホスト名、パス名などを格納したオブジェクトを与える。ここでは、url.parse関数を使ってこのオブジェクトをURLから生成している。この場合、実際に与えているオブジェクトは以下のようになっている。</p>

<pre>
> url.parse('http://example.com/')
{ protocol: 'http:',
  slashes: true,
  host: 'example.com',
  hostname: 'example.com',
  href: 'http://example.com/',
  pathname: '/',
  path: '/' }
> 
</pre>

<p>　なお、proxy-middlewareは通常HTTPヘッダなどの書き換えは行わず、ホストおよびパスのみを書き換えてリクエストを転送する。HTTPヘッダを書き換えたい場合、proxy-middlewareに与えるオブジェクトのheadersプロパティに書き換え後のヘッダ情報を格納しておけばよい。たとえばHOSTヘッダを「example2.com」に書き換えたい場合、以下のようにすればよい。</p>

<pre>
var proxy = require('proxy-middleware');
var proxyOptions = url.parse('http://example.com/');
proxyOptions.headers = {'host': 'example2.com'};
app.use(proxy(proxyOptions));
</pre>

