---
slug: node-http-request-get-and-timeout
title: Node.jsのhttp.request関数/http.get関数とタイムアウト
tag: [ node, programming, network ]
date: 2013-04-08T01:18:39+09:00
lastmod: 2013-04-16T21:59:13+09:00
publishDate: 2013-04-08T01:18:39+09:00
---

<p>　Node.jsのhttpモジュールには、HTTPクライアント機能も実装されている。http.request関数およびhttp.get関数がそれだ。詳細は<a href="http://nodejs.org/api/http.html">ドキュメント</a>を確認していただきたいが、http.requestは任意のリクエストメソッドを使ってリクエストを送信できるものだ。また、http.getはGETリクエストに限定されるものの、URLを与えるだけで簡単にリクエストを送信できる。</p>

<p>　たとえば以下のコード（http-request.js）は、引数で指定したURLに対しGETリクエストを送信し、取得したコンテンツを表示するものだ。</p>

<div class="code">
<span class="caption">http-request.js</span>
<pre>
#!/usr/local/bin/node
var http = require('http');

// check arguments
if (process.argv.length < 3) {
  process.exit(-1);
}
var targetUrl = process.argv[2]

// send request
var req = http.get(targetUrl, function(res) {
  // output response body
  res.setEncoding('utf8');
  res.on('data', function(str) {
    console.log(str);
  });
});

// error handler
req.on('error', function(err) {
  console.log("Error: " + err.message);
});
</pre></div>

<p>　http.request関数やhttp.get関数はともに戻り値としてhttp.ClientRequest型のrequestオブジェクトを返す。http.request関数の場合、request.endメソッドを実行して明示的にリクエストの送信を完了させる必要があるが、http.get関数の場合はendメソッドは暗黙的に実行されるので不要だ。</p>

<p>　http-request.jsを以下のように実行すると、http://hylom.net/のコンテンツがコンソールに表示される。</p>

<pre class="console">
$ node http-request.js http://hylom.net/
</pre>

<p>　さて、http.get関数やhttp.request関数を使ってリクエストを送信する場合、デフォルトではタイムアウト時間が設定されない。つまり、サーバーへの接続が成功した後、サーバー側がレスポンスの送信を完了しない限りクライアント側の処理は終了しない。</p>

<p>　たとえば、次のslowserver.jsはローカルホストの4000番ポートで待ち受けをし、リクエストを受信してから5分（300秒）後にレスポンスを返すというものだ。</p>

<div class="code">
<span class="caption">slowserver.js</span>
<pre>
#!/usr/local/bin/node
var http = require('http');

server = http.createServer();
server.on('request', function(req, res) {
  setTimeout(function() {
    res.setHeader('Content-Type', 'text/plain');
    res.writeHead(200);
    res.write('200 - OK.');
    res.end();
  }, 300 * 1000);
});

server.listen(4000, function() {
  console.log('start listening on port 4000...');
});
</pre>
</div>

<p>　このサーバーを実行し、先ほどのhttp-request.jsを使ってアクセスすると、実行後5分をすぎたあたりでレスポンスが表示される。</p>

<pre class="console">
$ node slowserver.js &
start listening on port 4000...

$ node http-request.js http://localhost:4000/
200 - OK.
$ fg
node slowserver.js
^C
</pre>

<p>　さて、タイムアウトが設定されていないということは、サーバー側がレスポンスを返さない、もしくは接続を破棄しない限り、クライアント側は永遠にレスポンスを待ち続けることになる。クライアント側でタイムアウト時間を設定するには、http.get関数やhttp.request関数の戻り値として返されるhttp.ClientRequestクラスのsetTimeoutメソッドを利用する。</p>

<pre class="definition">
request.setTimeout(timeout, [callback])
</pre>

<p>　timeout引数にはタイムアウト時間を指定する。単位はミリ秒だ。接続後、ここで指定された時間が経過するとrequestオブジェクトに'timeout'イベントが発生する。callback引数はtimeoutイベント発生時に一度だけ実行されるコールバック関数を指定する。なお、'timeout'イベントハンドラは引数を取らない。</p>

<p>　ここで注意したいのが、timeoutイベントが発生した場合でも接続は継続されたままになっている点だ。次のコードは、先のhttp-request.jsにrequest.setTimeoutメソッドを使ってタイムアウトを設定したものだ。</p>

<div class="code">
<span class="caption">http-request.js（改造版その1）</span>
<pre>
#!/usr/local/bin/node

var http = require('http');

// check arguments
if (process.argv.length < 3) {
  process.exit(-1);
}
var targetUrl = process.argv[2]

var req = http.get(targetUrl, function(res) {
  console.log('get response')
  res.setEncoding('utf8');
  res.on('data', function(str) {
    console.log(str);
  });
});
req.setTimeout(1000);

req.on('timeout', function() {
  console.log('request timed out');
  req.abort()
});

req.on('error', function(err) {
  console.log("Error: " + err.code + ", " + err.message);
});
</pre></div>

<p>　これを実行すると、次のようにtimeoutイベントは発生しているものの、イベント発生後も引き続きレスポンスを待ち続けていることが分かる。</p>

<pre class="console">
request timed out
200 - OK.
</pre>

<p>　timeoutイベント発生時に接続を破棄したい場合、イベントハンドラ内でrequest.abortメソッドなどを使用して明示的に接続を破棄する操作を行えばよい。</p>

<pre class="code">
req.on('timeout', function() {
  console.log('request timed out');
  req.abort()
});
</pre>

<p>　このように修正した上で先ほどのhttp-request.jsを実行すると、次のようにタイムアウト発生時に接続が破棄され、errorイベントが発生する。</p>

<pre class="console">
$ node http-request.js http://localhost:4000/
request timed out
Error: ECONNRESET, socket hang up
</pre>

