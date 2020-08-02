---
slug: use-logger-connect-middleware
title: Connectミドルウェア「logger」でExpressアプリケーションのアクセスログ/エラーログを記録する 
tags: [ express,connect,programming,node.js ]
date: 2013-03-25T02:03:46+09:00
lastmod: 2013-03-25T02:40:02+09:00
publishDate: 2013-03-25T02:03:46+09:00
---

<p>　Expressでは、Connectミドルウェア「<a href="http://www.senchalabs.org/connect/logger.html">logger</a>」を使うことで詳細なアクセスログやエラーログを記録することができる。Expressコマンドで生成したスケルトンコードでは、以下のようにloggerミドルウェアを利用するように設定されている。</p>

<pre>
app.configure(function(){
  ：
  ：
  app.use(express.logger('dev'));
  ：
  ：
}</pre>

<p>　このように第一引数に'dev'引数を与えて生成されたloggerミドルウェアを使用すると、標準出力にカラー付きでアクセスログが出力される。これは開発用という目的なので、実サービスの運用には適していない。そこで、Apacheのデフォルト設定で使われる形式のアクセスログおよびエラーログをファイルに出力するよう設定していく。</p>

<p>　なお、下記ではExpress 3.1.0およびこれが依存しているConnect 2.7.2ベースを使用している。</p>

<h4>logger型オブジェクトを生成する</h4>

<p>　loggerミドルウェアオブジェクトのファクトリ関数は、以下のような引数を取る。</p>

<pre>
logger([options])
</pre>

<p>　options引数にはオプション情報を格納したオブジェクト、文字列、関数オブジェクトを与えることができる。省略された場合は空のオブジェクト（{}）が与えられたものと見なされる。また、文字列もしくは関数オブジェクトが与えられた場合、次のようなオブジェクトが与えられたものと見なされる。</p>

<pre>
{format: ＜与えられた文字列もしくは関数オブジェクト＞}
</pre>

<p>　options引数に与えられたオブジェクトのうち、<strong>表1</strong>のプロパティが挙動に影響を与える。</p>

<table>
<caption>表1 options引数で有効なプロパティ</caption>
<tr><th>プロパティ名</th><th>説明</th><th>デフォルト値</th></tr>
<tr><td>immediate</td><td>非falseの値を指定すると、リクエストを受信した時点でログ出力を実行する。false、もしくはundefinedの場合、レスポンスの送信が完了した時点（responseオブジェクトのendイベントハンドラが呼び出されるタイミング）でログ出力を実行する</td><td>undefined</td></tr>
<tr><td>format</td><td>出力フォーマットを指定する。表2のどれかに該当する文字列が指定された場合、それに対応する定義済みフォーマットが使用される。それ以外の文字列が指定された場合、その文字列をフォーマット文字列として使用する</td><td>'default'</td></tr>
<tr><td>stream</td><td>ログを出力するストリームを指定する</td><td>process.stdout</td></tr>
<tr><td>buffer</td><td>バッファを利用する場合、非falseの値を指定する。数値が指定された場合、フラッシュする間隔をミリ秒で指定する</td><td>undefined</td></tr>
</table>

<p>　また、options.formatプロパティでは出力形式を指定できるが、ここでは<strong>表2</strong>の定義済みフォーマット値が利用できる。「tiny」と「dev」はほぼ同じ内容を出力するが、devはコンソール出力時に見やすいよう色付き表示のためのエスケープシーケンス付きで出力される点が異なる。</p>

<table>
<caption>表2 使用できる定義済みフォーマット</caption>
<tr><th>定義済みフォーマット名</th><th>フォーマット文字列</th></tr>
<tr><td>default</td><td>:remote-addr - - [:date] ":method :url HTTP/:http-version" :status :res[content-length] ":referrer" ":user-agent"</td></tr>
<tr><td>short</td><td>:remote-addr - :method :url HTTP/:http-version :status :res[content-length] - :response-time ms</td></tr>
<tr><td>tiny</td><td>:method :url :status :res[content-length] - :response-time ms</td></tr>
<tr><td>dev</td><td>:method :url :status :response-time ms - :res[content-length]</td></tr>
</table>

<p>　なお、フォーマット文字列では<strong>表3</strong>のトークンが利用できる。これらは出力時に適切な値に変換される。</p>

<table>
<caption>表3 フォーマット文字列で使用できるトークン</caption>
<tr><th>トークン名</th><th>変換後の文字列</th></tr>
<tr><td>:url</td><td>req.originalUrl || req.url</td></tr>
<tr><td>:method</td><td>req.method</td></tr>
<tr><td>:response-time</td><td>new Date - req._startTime</td></tr>
<tr><td>:date</td><td>new Date().toUTCString()</td></tr>
<tr><td>:status</td><td>res.statusCode</td></tr>
<tr><td>:referrer</td><td>req.headers['referer'] || req.headers['referrer']</td></tr>
<tr><td>:remote-addr</td><td>req.ipもしくはsock.socket.remoteAddress、sock.remoteAddress</td></tr>
<tr><td>:http-version</td><td>req.httpVersionMajor + '.' + req.httpVersionMinor</td></tr>
<tr><td>:user-agent</td><td>req.headers['user-agent']</td></tr>
<tr><td>:req[＜リクエストヘッダ名＞]</td><td>指定したリクエストヘッダの値</td></tr>
<tr><td>:res[＜レスポンスヘッダ名＞]</td><td>指定したレスポンスヘッダの値</td></tr>
</table>

<p>　定義済みフォーマットで所望の出力が得られない場合、<strong>表3</strong>のフォーマット文字列を使って独自のフォーマットを定義することも可能だ。さらに、options.formatプロパティに独自のログ整形処理を実装した関数オブジェクトを与えることもできる。この場合、この関数オブジェクトはログを出力するタイミングで(exports, req, res)という引数が与えられて実行される。exports引数にはloggerモジュールが、req引数にはリクエストオブジェクトが、res引数にはレスポンスオブジェクトが与えられ、この関数の戻り値がログとして指定されたストリームに出力される。</p>

<h4>Apacheのデフォルト設定で使われる形式のログを出力する</h4>

<p>　以下はApacheのデフォルト設定で出力されるログの例だ。</p>

<pre>
192.168.0.1 - - [24/Mar/2013:06:07:06 +0900] "GET /feed/ HTTP/1.1" 304 - "-" "hogehoge user-agent"
</pre>

<p>　このとき、各フィールドには次のような情報が格納されている。なお、定義されていない/取得できない値に対応するフィールドには「-」が出力される。</p>

<pre>
＜リモートホスト名＞ ＜identd（mod_ident）が提供するリモートログ名＞ ＜リモートユーザー名＞ ＜アクセス日時＞ "＜HTTPリクエストヘッダ＞" ＜ステータスコード＞ ＜転送バイト数＞ "＜Refererリクエストヘッダの値＞" "＜User-Agentリクエストヘッダの値＞"
</pre>

<p>　これと同じ形式のログをloggerミドルウェアを使って出力するには、定義済みフォーマットの「default」を利用すればよい。たとえば/home/foobar/access_logというファイルにログを出力するには、以下のようにする。</p>

<pre>
app.configure(function(){
  ：
  ：
  var logStream = fs.createWriteStream('/home/foobar/access_log', {mode: 'a'});
  app.use(express.logger({
    format: 'default',
    stream: logStream || process.stdout
    }));
  ：
  ：
}</pre>

