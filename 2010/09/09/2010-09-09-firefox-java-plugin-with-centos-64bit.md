---
title: x86_64版CentOS 5.5で64ビット版FirefoxでJavaプラグインを使う
author: hylom
type: post
date: 2010-09-09T09:45:41+00:00
url: /2010/09/09/firefox-java-plugin-with-centos-64bit/
category:
  - Docs
tag:
  - centos
  - linux
  - tips
  - web

---
　x86_64版CentOS 5.5のFirefoxでのJavaプラグイン導入に軽くハマったのでメモ。

　x86_64版のCentOS 5でFirefoxにJavaプラグインを導入したい場合、ググると「32ビット版Firefox＋32ビット版Javaランタイムを使え」という話がぼちぼちとヒットするわけですが、とりあえずJavaプラグインだけを使いたい場合は64ビット版でも可能なようです。ていうか自分の場合、32ビット版を導入しようとしたらうまくいきませんでした……。

　ということで、手順。まず64ビット版Firefoxをインストール。

<pre>$ sudo yum install firefox  # 64ビット版Firefoxをインストール
</pre>

　続いて[java.comのダウンロードページ][1]から「Linux x64 RPM」をダウンロード。

<div style="width: 510px" class="wp-caption aligncenter">
  <img alt="「Linux x86 RPM」をダウンロードする" src="/img/blog/100909/dl_jre.png" title="「Linux x86 RPM」をダウンロードする" width="500" height="238" />
  
  <p class="wp-caption-text">
    「Linux x86 RPM」をダウンロードする
  </p>
</div>

　RPMと書いてあるが、ダウンロードしたファイルはRPMではなくインストーラなので、root権限で実行してインストール。自動的にRPMがインストールされる。

<pre>$ chmod +x jre-6u21-linux-x64-rpm.bin
$ sudo ./jre-6u21-linux-x64-rpm.bin
</pre>

　続いて設定。インストールしたjreを利用するようalternativesコマンドで指定。

<pre>$ sudo /usr/sbin/alternatives --install /usr/bin/java java /usr/java/jre1.6.0_21/bin/java 2
$ sudo /usr/sbin/alternatives --config java
</pre>

　最後にmozilla用プラグインフォルダにプラグインのシンボリックリンクを張って完了。

<pre>$ cd /usr/lib64/mozilla/plugins/
$ sudo ln -sf usr/java/jre1.6.0_21/lib/amd64/libnpjp2.so .
</pre>

　あとはFirefoxでabout:pluginsを開きプラグインが正しくインストールされているか確認したり、java.comにアクセスして動作を確認するなり適当にどうぞ。

 [1]: http://www.java.com/en/download/manual.jsp
