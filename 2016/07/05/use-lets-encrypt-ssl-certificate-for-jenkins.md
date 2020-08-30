---
slug: use-lets-encrypt-ssl-certificate-for-jenkins
title: JenkinsでLet's encryptのSSL証明書を使う
tag: [ jenkins, ci ]
date: 2016-07-05T22:00:58+09:00
lastmod: 2016-07-05T23:24:11+09:00
publishDate: 2016-07-05T22:00:58+09:00
---

　Let's encryptで取得したSSL証明書をJenkinsで使おうとしてハマったので解決法のメモ。

　基本的には[https://issues.jenkins-ci.org/browse/JENKINS-22448](https://issues.jenkins-ci.org/browse/JENKINS-22448)に書いてあるとおり。まず、次のようなconvert.shを作る。

```
#!/bin/bash

HOST=＜ホスト名＞
KEY_PEM=/etc/letsencrypt/live/$HOST/privkey.pem
CERT_PEM=/etc/letsencrypt/live/$HOST/cert.pem
JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
KEYSTORE=/var/lib/jenkins/keystore

# convert ky
openssl rsa -des3 -in $KEY_PEM -out key.encrypted.pem
openssl pkcs12 -inkey key.encrypted.pem -in $CERT_PEM -export -out keys.encrypted.pkcs12
keytool -importkeystore -srckeystore keys.encrypted.pkcs12 -srcstoretype pkcs12 -destkeystore $KEYSTORE
```

　このconvert.shをroot権限で実行すると、/var/lib/jenkins/keystoreというファイルができる。ついでにカレントディレクトリにいくつかの中間ファイルができるが、それは削除してOK。

　次にJenkinsのサーバー設定ファイル（Ubuntuなら/etc/default/jenkins）内の「JENKINS_ARGS」付近を以下のように変更する。

```
HTTPS_KEYSTORE=/var/lib/jenkins/keystore
HTTPS_KEYSTORE_PASSWORD=＜適当なパスワード＞
HTTPS_PORT=8443
HTTPS_OPT="--httpsKeyStore=$HTTPS_KEYSTORE --httpsKeyStorePassword=$HTTPS_KEYSTORE_PASSWORD --httpsPort=$HTTPS_PORT"

JENKINS_ARGS="--webroot=/var/cache/$NAME/war --httpPort=$HTTP_PORT $HTTPS_OPT"
```

　これでJenkinsを再起動すればhttps://＜ホスト名＞:8443/での待ち受けが可能。鍵を更新したら毎回この作業が必要なので適当にcronで回すのがよさそう……なんだけど、途中でパスワードの入力を求められるのでそこら辺を自動化しないといけません。


