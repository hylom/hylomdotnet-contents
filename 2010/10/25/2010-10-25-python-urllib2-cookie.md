---
title: 要ログインのサイトにPythonのurllib2でアクセスする
author: hylom
type: post
date: 2010-10-24T15:55:22+00:00
url: /2010/10/25/python-urllib2-cookie/
category:
  - Docs
tag:
  - programming
  - python
  - www

---
　ログインが必要なWebサイトに対してスクリプトでページを取得/送信したい場合、まずログイン用のURLに対しログイン情報をPOSTしてCookieを取得する、という作業を行うのが一般的だ。しかし、Pythonのurllib2を利用すると簡単にPOSTは行えるのだが、なぜかCookieを取得できない、という問題が発生することがある。

　これはurllib2のurlopen()でURLを開き、帰ってきたオブジェクトのinfo()メソッド経由でSet-Cookieヘッダを取得しようとする場合に発生する。たとえばCMSを使用しているWebサイトで、管理用ページ以外に（正当な）Cookieを持たずにアクセスするとCookieなしでアクセスできるトップページ等にリダイレクトされる、というケース。多くのCMSではログインに成功すると管理ページトップにリダイレクトされるのだが、urllib2のデフォルト設定ではCookie処理を行ってくれない＆リダイレクトを自動的に処理してくれるため、「ログイン成功→（Cookieを返すがurllib2はCookieを保存せず）→管理ページトップにリダイレクト→Cookieがないので公開ページのトップにリダイレクト→Cookieは受け取れず」という事態になってしまうことがある。

　この場合、urllib2.HTTPCookieProcessorを使ってCookie処理を行えばよいのだが、なぜかurllib2のドキュメントにはこのクラスの解説が無い。例にも上がっていない。ということで途方にくれるわけだが、実はCookieを扱うcookielibのほうに使い方の例が載っていたりする。

<pre class="code">import cookielib
# ： 
# （このへんでurlやencoded_data、headersを準備）
# ：
req = urllib2.Request(url, encoded_data, headers)
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp = opener.open(req)
</pre>

　取得したCookieはCookieJarオブジェクトに保存されるので、必要に応じて適宜取り出せばOK。かわりにFileCookieJarオブジェクトを使えばファイルへのsave/loadも可能。
