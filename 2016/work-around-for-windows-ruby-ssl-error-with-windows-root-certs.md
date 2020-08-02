---
slug: work-around-for-windows-ruby-ssl-error-with-windows-root-certs
title: Windows環境でのRubyのSSLエラー対策（Windowsが管理するルート証明書を使う）
tags: [ windows,ruby ]
date: 2016-12-09T19:24:38+09:00
lastmod: 2016-12-09T19:25:45+09:00
publishDate: 2016-12-09T19:24:38+09:00
---

　Windows環境でRubyを使う際、以下のようなエラーが出る場合がある。これはSSLアクセスに利用できる適切なルート証明書がないために発生する。

```
C:/Ruby23-x64/lib/ruby/2.3.0/net/http.rb:933:in `connect_nonblock': SSL_connect
returned=1 errno=0 state=error: certificate verify failed (OpenSSL::SSL::SSLErro
r)
```
　対策としてはルート証明書を用意すれば良いのだが、ネットから安易にダウンロードしたくないという場合、「certmgr」というツールでWindowsが管理するルート証明書をエクスポートし、opensslコマンドでRubyが扱える形に変換して利用すれば良い。

　まずスタートメニューの「プログラムとファイルの検索」に「certmgr.msc」と入力してEnterキーを押す。certmgrが起動するので、左ペイン内の「信頼されたルート証明機関」－「証明書」を選択する。

　すると証明書一覧が表示されるので、右ペインをクリックし、Ctrl-A等を入力してすべての証明書を選択する。続いて右クリックしてコンテキストメニューの「すべてのタスク」－「エクスポート」メニューを選択する。「証明書のエクスポート ウィザード」が開くので、指示に従って進める。「エクスポートファイルの形式」では「PKCS #12」を選択し、「すべての拡張プロパティをエクスポートする」にチェックを入れておく。エクスポートされたファイルは.pfxという拡張子が付く。

　続いてこのファイルを引数に指定して次のようにopensslコマンドを実行する。Windowsにはデフォルトではopensslコマンドが含まれていないので、別途インストールするか、適当なLinuxマシンにエクスポートした.pfxファイルをコピーして実行しよう。

```
$ openssl pkcs12 -in ＜エクスポートしたファイル（.pfx）＞ -out ＜適当なファイル名.pem＞ -nodes
```

　これでRubyで扱える.pemファイルが出力される（参考：[@ITの「*.pfxファイルからPEM形式で証明書や秘密鍵を取り出す」](http://www.atmarkit.co.jp/ait/articles/1602/05/news039_2.html)）。

　このファイルを適当な場所に保存し、SSL_CERT_FILE環境変数にそのパスを指定する。たとえばC:\Users\hylom\windows.pemとして保存した場合、以下のようになる。

```
$ set SSL_CERT_FILE=C:\Users\hylom\windows.pem
```

