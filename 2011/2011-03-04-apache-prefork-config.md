---
title: Apacheチューニング：プロセス設定を変更
author: hylom
type: post
date: 2011-03-04T11:00:48+00:00
url: /2011/03/04/apache-prefork-config/
categories:
  - Docs
tags:
  - apache
  - httpd
  - tuning

---
　hylom.netがだいぶ遅くなっていたのでちょっとチューニングした。原因としてはメモリ不足、DBが遅い、I/Oが遅い、ネットワークが遅いなどがあるが、さくらVPSのコントロールパネルを見た限りではCPUやネットワーク、I/Oには余裕がある感じだったので、メモリ不足ではないかと検討をつける。ということで、各プロセスのメモリ使用状況をチェック。

<pre># ps aux --sort -rss| lv

USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
apache   28879  0.1  6.6 269404 33728 ?        S    Mar01   9:40 /usr/sbin/httpd
apache   28966  0.1  6.5 269072 33484 ?        S    Mar01   9:54 /usr/sbin/httpd
apache   30532  0.1  6.5 272696 33412 ?        S    Mar02   4:48 /usr/sbin/httpd
apache   30542  0.1  6.2 274072 31680 ?        S    Mar02   4:41 /usr/sbin/httpd
apache   29002  0.1  6.0 274684 30804 ?        S    Mar01   9:31 /usr/sbin/httpd
apache   28868  0.2  5.9 273812 30556 ?        S    Mar01  10:30 /usr/sbin/httpd
apache   28750  0.2  5.8 274168 29964 ?        S    Mar01  10:56 /usr/sbin/httpd
apache   30543  0.1  5.7 274040 29212 ?        S    Mar02   4:23 /usr/sbin/httpd
apache   30529  0.1  5.2 273992 26952 ?        S    Mar02   4:33 /usr/sbin/httpd
apache   28580  0.2  4.8 274152 24852 ?        S    Mar01  10:36 /usr/sbin/httpd
apache   27032  0.1  4.3 273148 22224 ?        S    Mar01   6:06 /usr/sbin/httpd
apache    8773  0.1  3.9 268900 19944 ?        S    Mar03   2:44 /usr/sbin/httpd
apache   27108  0.1  3.7 274016 19224 ?        S    Mar01   6:03 /usr/sbin/httpd
apache   30530  0.1  3.3 273152 17020 ?        S    Mar02   4:45 /usr/sbin/httpd
apache   18789  0.1  2.7 269340 14000 ?        S    Mar01   5:38 /usr/sbin/httpd
apache   28998  0.1  2.6 274204 13616 ?        S    Mar01   9:11 /usr/sbin/httpd
apache    8767  0.1  2.1 273544 10756 ?        S    Mar03   2:53 /usr/sbin/httpd
apache   28976  0.1  1.9 273572  9740 ?        S    Mar01   9:32 /usr/sbin/httpd
apache   28877  0.2  1.4 274668  7308 ?        S    Mar01  10:14 /usr/sbin/httpd
apache   30506  0.1  1.1 273528  5688 ?        S    Mar02   4:12 /usr/sbin/httpd
　：
　：
</pre>

　見て分かるように、httpdのプロセスが多数走っており、メモリを食いつぶしていることが分かる。そこで、httpdで使用するプロセス数を調整することで対処を図る。

<pre>&lt;IfModule prefork.c&gt;
StartServers       8
MinSpareServers    5
# MaxSpareServers   20
MaxSpareServers   16
#ServerLimit      256
ServerLimit      32
#MaxClients       256
MaxClients       32
MaxRequestsPerChild  4000
&lt;/IfModule&gt;
</pre>

　MaxSpareServersとMaxClientsを減らしてとりあえず様子見。

　なお、@ITの「[httpd.confによるWebサーバの最適化][1]」という記事などを参考にした。

 [1]: http://www.atmarkit.co.jp/flinux/rensai/apache2_03/apache03a.html