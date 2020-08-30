---
title: 日本語リファレンスには書いてない話：urllibとurllib2の違いってなんだ
author: hylom
type: post
date: 2010-02-09T15:51:57+00:00
url: /2010/02/10/urllib_and_urllib2_usag/
category:
  - Docs
tag:
  - library
  - python

---
　Pythonでは、HTTPやFTPなどでファイルの送受信をするモジュールとして「[urllib][1]」と「[urllib2][2]」が用意されている。使い方も似ていて、どちらも引数としてURLを与えてurlopen()関数を呼び出すと自動的に対応したプロトコルでURLにアクセスしてデータを読み出せる、というものである。しかし、似たような名前で似たような機能を持つこの2つ、何が違うのかが明確にはドキュメントに記述されていない。そのためどちらを使うべきか迷って、そのたびにGoogleのお世話になるという状況だったのでざっとまとめてみよう。

<!--more-->

　外から見える違いとしては、urlopen()の引数としてurllibはURL文字列のみを受け付けるのに対し、urllib2ではurllib2.Requestクラスを受け取ることができる、という点がある。urllib2.Requestクラスはリクエストを抽象化したクラスで、これを利用することでたとえばHTTPでのデータ送受信の際、任意のHTTPヘッダーを送信させるようなことが可能になる。また、urllibでは使用するproxyを直接引数で指定できるが、urllib2ではRequestオブジェクトで指定することになる。

　ということで、ただHTTPやFTPでデータを取得したいだけならurllibでもurllib2でもどちらでも対して変わらない、HTTPヘッダーをカスタマイズしたいならurllib2を使え、という話になる。あと、urllibにはurlretrive()という関数があったり、quote()/unquote()/urlencode()などの便利そうなユーティリティ関数がある、というくらい。

#### 独自プロトコルを実装したい場合は？

　いっぽう、挙動をカスタマイズしたい、独自プロトコルを実装したい、という場合は話が変わってくる。urllibもurllib2も独自プロトコルへの対応などのカスタマイズが可能なのだが、urllibはFancyURLopenerクラスの派生クラスで実装を行うのに対し、urllib2はBaseHandlerクラスの派生クラスで実装する。

　まず、urllibの場合。ドキュメントに記載されている例だが、たとえばUser-Agentを変更したい場合、下記のようにFancyURLopenerの派生クラスを作り、その初期化時に指定したいUserAgentをversion変数に代入するようにする。そして、この派生クラスのインスタンスをurllib._urlopenerに代入してやる。

<pre>import urllib

class AppURLopener(urllib.FancyURLopener):
    def __init__(self, *args):
        self.version = "App/1.7"
        urllib.FancyURLopener.__init__(self, *args)

urllib._urlopener = AppURLopener()
</pre>

　これにより、以後はurllib.urlopen()などを呼び出した際、urllib._urlopener()で指定したインスタンスを使用してHTTP/FTPなどの処理が行われるようになる。

　ちなみに、FancyURLopenerとURLopenerの関係だが、HTTP/HTTPS/FTPなどの基本的な通信/データ取得処理はURLopener内で実装されており、FancyURLopenerはそれに各種HTTPレスポンスコードへの対応やリトライといった処理を実装したサブクラスとなっている。

　またドキュメントには記述されていないが、URLopenerにはaddheader()というメソッドが用意されており、ヘッダー名をキー、与えるデータを値にした辞書を引数として与えることで、任意のヘッダーを追加できる。

<pre>def addheader(self, *args):
        """Add a header to be used by the HTTP interface only
        e.g. u.addheader('Accept', 'sound/basic')"""
        self.addheaders.append(args)
</pre>

　たとえばURLopenerの\_\_init\_\_()内では、次のようにしてUser-Agentを指定している。

<pre>self.addheaders = [('User-Agent', self.version)]
</pre>

　なおURLopenerでは、urlopen()でHTTP/HTTPSのURLを与え、かつ第2引数が非Noneの場合（つまり、なんらかのデータを与えた場合）は「Content-Type: application/x-www-form-urlencoded」でのPOSTリクエストを利用するようにハードコーディングされている。そのため、ほかの形式でデータをPOSTしたい場合（ファイルを送信するなど）は、独自のURLopenerを作成する必要がある。

#### urllib2で独自プロトコルを使うには？

　いっぽうurllib2で独自のプロトコルを扱いたい場合、まずプロトコルを実装したBaseHandler()派生クラスを用意し、続いてそれを引数として与えてbuild\_opener()を呼び出してURLハンドラを作成、最後にそれをinstall\_opener()引数に与えて登録、という手順となる。下記はドキュメントに記載されている例だ。

<pre>import urllib2
# ベーシック HTTP 認証をサポートする OpenerDirector を作成する...
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib2.build_opener(auth_handler)
# ...urlopen から利用できるよう、グローバルにインストールする
urllib2.install_opener(opener)
urllib2.urlopen('http://www.example.com/login.html')
</pre>

　なお、urllib2の（デフォルトの）HTTP/HTTPSハンドラでも、urlopen()の第2引数が非Noneの場合（つまり、なんらかのデータを与えた場合）は「Content-Type: application/x-www-form-urlencoded」でのPOSTリクエストを利用するようにハードコーディングされている。そのため、ほかの形式でデータをPOSTしたい場合（ファイルを送信するなど）は、やっぱり独自のハンドラを作成する必要がある。

　ちなみに、Python3系ではPython2系のurllibは廃止され、urllib2もurllib.requestという名称に変更されている。ということで、Python3系を見据えるならurllibではなくurllib2を利用するのが望ましいようだ。

 [1]: http://www.python.jp/doc/2.4/lib/module-urllib.html
 [2]: http://www.python.jp/doc/2.4/lib/module-urllib2.html
