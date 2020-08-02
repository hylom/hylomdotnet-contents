---
slug: nodejs-web-application-startguide
title: Node.jsでWebAppの開発に必要なN個のこと 
tags: [ node.js ]
date: 2013-09-11T00:43:00+09:00
lastmod: 2013-09-11T00:44:57+09:00
publishDate: 2013-09-11T00:43:00+09:00
---

<p>　※元ネタは「<a href="http://d.hatena.ne.jp/gfx/20130909/1378741015">PerlでWebAppの開発に必要なN個のこと</a>」</p>

<p>　あるプログラミング言語で実際にWebAppを開発できるようになるまで、何が必要だろうか。言語仕様の習得は終えているとしよう。おそらく、最低限以下のような知識が必要だと思われる。とりあえずNode.jsについて知っていることを書いた。</p>


<h3>パッケージマネージャ</h3>

<p>　ライブラリの管理には、Node.jsに同梱されている<a href="https://npmjs.org">npm</a>を利用する。Node.js向けに公開されているパッケージのほぼすべてはnpm経由で入手が可能だ。</p>

<p>　npmでは通常アプリケーション個別のディレクトリにパッケージがインストールされ、システム全体でのパッケージの共有は行わないため、バージョン管理は容易である（オプションでシステム全体で共有するようにパッケージをインストールすることも可能）。</p>

<h3>アプリケーションサーバー</h3>

<p>　Node.jsには標準でhttpモジュール/httpsモジュールというHTTP/HTTPSサーバーが組み込まれている。別途Webサーバーを用意する必要は無い。</p>

<h3>リクエストパラメータの処理</h3>

<p>　自前で実装するのであれば、標準で含まれているurlモジュールやquerystringモジュールを使ってパースができる。フォームの処理を行うなら、<A href="https://github.com/felixge/node-formidable">Formidableモジュール</a>などを使うと簡単だ。</p>

<h3>ルーティング</h3>

<p>　単体のルーティングモジュールとしては、今のところNode.jsで決定的なものはない。http/httpsモジュールではリクエストを受け取るとイベントハンドラにリクエストされたパスやパラメータを含んだオブジェクトを渡すので、それらを見てif文などで自前でルーティング処理を実装してもたいした手間ではない。もちろん、npmにはいくつかのルーティング用モジュールが登録されている。</p>

<h3>データベース</h3>

<p>　統一的なインターフェイスはないが、主要なデータベースに対するモジュールは一通り用意されている。たとえばMySQLであれば<a href="https://github.com/felixge/node-mysql">node-mysql</a>など。</p>

<h3>ビューのレンダリング</h3>

<p>　JavaScriptコードをHTML内に埋め込むタイプであれば<a href="http://embeddedjs.com">EJS</a>が広く使われている。そのほか、<a href="http://twitter.github.io/hogan.js/">Hogan.js</a>や<a href="http://jade-lang.com">jade</a>などお好みで。JSONを生成したいのであれば、JSON.stringfy()で可能。</p>

<h3>HTTPクライアント</h3>

<p>　Node.js標準のhttpモジュールに含まれている。</p>

<h3>テストフレームワーク</h3>

<p>　<a href="http://vowsjs.org">Vows</a>とか<a href="http://visionmedia.github.io/mocha/">mocha</a>とかが有名。</p>

<h3>WAF（Web Application Framework）</h3>

<p>　有名なのは<a href="http://expressjs.com">express</a>。ルーティングやリクエストのパースを容易にする機能が多数提供される。また、ルーティングを自前でやりたいというのであればexpressのベースとなっている<a href="http://www.senchalabs.org/connect/">Connect</a>もチェックすると良い。また最近では<a href="http://sailsjs.org/">Sails.js</a>というWAFが注目されているようだ。</p>

