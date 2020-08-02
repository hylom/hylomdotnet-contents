---
title: 64ビット版CentOSで32ビット用プログラムを動かす
author: hylom
type: post
date: 2012-07-26T09:17:02+00:00
url: /2012/07/26/run-32bit-program-on-64bit-centos/
categories:
  - Hacks
tags:
  - centos
  - linux

---
　64ビットのLinux環境で32ビットのプログラムを動かそうとする場合、32ビット版のライブラリが不足していて実行できない場合がある。

<pre>/lib/ld-linux.so.2: bad ELF interpreter: No such file or directory
</pre>

　と出た場合、次のように32ビット版のlibstdc++をインストールすればOK。

<pre>$ sudo yum install libstdc++.i686
</pre>