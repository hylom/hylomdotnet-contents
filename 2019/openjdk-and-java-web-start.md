---
slug: openjdk-and-java-web-start
title: openJDKでJava Web Startを使う
tags: [ java ]
date: 2019-05-17T20:16:33+09:00
lastmod: 2019-05-17T20:17:23+09:00
publishDate: 2019-05-17T20:16:33+09:00
---

　ブラウザから直接Javaアプリを起動する「Java Web Start」という技術があります。この技術はすでに終息されることが発表されているのですが、まだ使っているサービスがあります。しかし、[OpenJDKサイト](https://openjdk.java.net/)で配布されているopenJDKではこの技術のサポートが含まれておらず、これらをインストールしてもJava Web Startは利用できない状況です。

　もしopenJDKでJava Web Startを利用したい場合、有志による[ojdkbuild](https://github.com/ojdkbuild/ojdkbuild/releases)というプロジェクトが配布しているopenJDK 1.8.0系にはJava Web Startサポートが含まれています。

　このプロジェクトで配布されているバイナリのうち、WindowsのZIP版にはJava Web Startサポートが含まれていないそうなので（[issue](https://github.com/ojdkbuild/ojdkbuild/issues/48)）、msiインストーラ版をダウンロードしてインストールすると、C:\Program Files\Java\jdk1.8.0_25\bin以下に「javaws.exe」というバイナリがインストールされます。Java Web Startで使用する.jnlpファイルを指定してこれを実行することで、Javaアプリ起動できます（なお、Chromeだとなぜか.jnlpという拡張子が消える場合があるようなので注意）。

```
> javaws ＜対象の.jnlpファイル＞
```

　また、うまく起動できないといった不具合が出た場合は「-verbose」オプションを付けると各種メッセージが表示されるようになります。

