---
slug: how-to-use-google-openid-auth
title: 独自WebサービスにGoogleアカウントを使った認証を実装する
tags: [ google,openid,develoer ]
date: 2016-02-11T23:42:51+09:00
lastmod: 2016-02-11T23:44:58+09:00
publishDate: 2016-02-11T23:42:51+09:00
---

<p>　結構ハマったので記録に残しておく。Webアプリを想定し、コードはNode.jsでのものの抜粋。</p>

<p>　基本的にはGoogle Developersの<a href='https://developers.google.com/identity/protocols/OpenIDConnect'>OpenID Connect</a>ページに書いてある通りで、OAuth 2.0を使って認証を行える。</p>

<p>　事前準備としては、<A href="https://console.developers.google.com/home/dashboard">Google Developers Console</a>でプロジェクトを作成しておく。認証だけであればAPIはすべて無効でOK。認証情報では使用する「承認済みのリダイレクトURI」を適切に登録しておく。</p>

<p>　コード的には、一般的なOAuth 2.0での認証と同じ。流れ的には次のような感じ。</p>

<h3>1. 適当なランダム文字列を生成する</h3>

<p>　下記のコードではstateToke変数がそれ。今回はランダム文字列と日付と適当な文字列（salt）を組み合わせてsha256ハッシュを取って使用。これは認証が試みられるたびに異なるものを作る必要がある。</p>

<pre>
  var salt = 'hogehoge';
  var hash = crypto.createHash('sha256');
  hash.update(salt + Math.random() + Date())
  var stateToken = hash.digest('hex');
</pre>

<h3>2. 認証URLを作成</h3>

<P>　クライアントIDとランダム文字列とリダイレクトURLをパラメータとして指定する。</P>
<pre>
  var authUrl = 'https://accounts.google.com/o/oauth2/v2/auth?'
    + 'response_type=code'
    + '&client_id=' + config.googleToken.clientID
    + '&redirect_uri=' + ＜リダイレクトURL＞
    + '&scope=profile%20email'
    + '&state=' + stateToken;
</pre>

<h3>3. ランダム文字列をセッションストアに保存したうえで認証URLにリダイレクトする</h3>

<p>　この辺はフレームワークによって異なるのでコードは割愛。リダイレクトURLがDevelopers Consoleで指定したものと異なるとエラーになるので注意。</p>

<h3>4. リダイレクトURL経由でトークンを取得</h3>

   認証に成功すると、Googleの認証ページから指定したリダイレクトURLにリダイレクトされる。このとき、URLには「?state=＜token＞&code=＜code＞」というパラメータが付加されるので、URLをパースして取得。

<pre>
  var params = url.parse(req.url, true);
  var code = params.query.code;
  var state = params.query.state;
</pre>

<p>　ここで、stateには最初に作成したランダム文字列が入るので、セッションストアに保存されていた値と比較する、同じクライアントでアクセスしていれば一致するはず。一致しなければ認証失敗を返す。</p>

<pre>
  if (state !== session.stateToken) {
      // 認証に失敗。エラーを返すコードを書く
</pre>

<h3>5. 取得したcodeを使ってアクセストークンを取得する</h3>

<P>　ここは面倒臭いのでモジュールの利用を推奨。リダイレクトURLは最初に指定したものと同じものを指定する。</P>

<pre>
  var oauth2 = new oauth.OAuth2(
    config.googleToken.clientID, //cliendId
    config.googleToken.clientSecret, //clientSecret
    'https://accounts.google.com/o/', //baseSite
    null, //authorizePath
    'oauth2/token', //accessTokenPath
    null  //customHeaders
  );
  var param = {
    grant_type: 'authorization_code',
    redirect_uri: ＜リダイレクトURL＞
  };
  oauth2.getOAuthAccessToken(code, param, tokenCallback);
</pre>

<h3>6. 受け取ったトークンを検証する</h3>
<p>　無事認証に成功するとアクセストークンとリフレッシュトークン、認証用データが入ったオブジェクトがコールバック関数に渡される（下記のtoken、refresh、resultsがそれ）。</p>

<pre>
var jwtToken = require('./jwt-token');

  function tokenCallback(err, token, refresh, results) {
    if (err) {
      callback(err, null);
      return;
    }

    jwtToken.verify(results.id_token, function (err, token) {
      if (err || !token) {
        callback(err, null);
        return;
      }
      callback(null, token);
    });
  };
</pre>

<p>　ここで、ユーザー情報はresultsオブジェクトのid_tokenプロパティにJSON Web Tokens（JWT）という形式で署名済みの形で格納されているので、それをデコードして検証しなければならない。</p>

<p>　JWTを扱うモジュールとしてjwt-simpleモジュールがあるので、今回はこれを使用。また、<A href="https://www.googleapis.com/oauth2/v1/certs">検証に使う公開鍵</a>はそれなりの頻度で変更されるとのことなので、検証のたびにダウンロードして使用する。この処理をラップしたモジュール（jwt-token.js）が下記。</p>

<pre>
var jwt = require('jwt-simple');
var https = require('https');

var certsUrl = 'https://www.googleapis.com/oauth2/v1/certs';

function decodeBase64(strings) {
  var buf = new Buffer(strings, 'base64');
  return buf.toString('utf8');
}

function verifyJwtToken(token, callback) {
  var segments = token.split('.');
  var envelope = JSON.parse(decodeBase64(segments[0]));
  var payload = JSON.parse(decodeBase64(segments[1]));

  var data = '';
  var req = https.get(certsUrl, function (res) {
    res.on('data', function (chunk) {
      data += chunk;
    });
    res.on('end', function () {
      var certs = JSON.parse(data);
      var key = certs[envelope.kid];
      var result = jwt.decode(token, key);
      callback(null, result);
    });
  });

  req.on('error', function (err) {
    callback(err);
  });
}  

exports.verify = verifyJwtToken;
</pre>

<p>　トークンをデコードすると、中にemailというプロパティがあるのでそこからユーザーのメールアドレスを取得できるので、これを自分のサービス側に登録されているメールアドレスと比較してユーザーと対応付けるなり、新たにユーザーを作るなりOpenID関連の情報を使って認証するなりすればOK。</p>

