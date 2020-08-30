---
slug: use-lets-encrypt-with-fedora-25-and-httpd
title: Fedora 25のhttpd（Apache HTTP Server）でLet's Encryptを使う
tag: [ fedora, linux ]
date: 2017-02-10T20:22:39+09:00
lastmod: 2017-02-10T20:22:39+09:00
publishDate: 2017-02-10T20:22:39+09:00
---

　Fedora 25では、httpdをインストールするとデフォルトで自己署名証明書を作成してSSLを有効にする設定になっている模様。そのため、certbotコマンドでLet's Encryptで証明書を取得しようとすると失敗するようだ。

```
# dnf install certbot
# certbot --apche
（...ここで設定を入力する）
Failed authorization procedure. test.hylom.net (tls-sni-01): urn:acme:error:connection :: The server could not connect to the client to verify the domain :: Failed to connect to ＜IPアドレス＞:443 for TLS-SNI-01 challenge
```

　対策としては、まず/etc/httpd/conf.d/ssl.confをssl.conf.orgなどにリネーム後にhttpdを再起動してSSLをいったん無効にした後、certbotコマンドを実行すれば良い。


