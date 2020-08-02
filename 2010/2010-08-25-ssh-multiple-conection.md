---
title: あまり知られてない（ような気がする）sshの多重接続
author: hylom
type: post
date: 2010-08-24T17:02:08+00:00
url: /2010/08/25/ssh-multiple-conection/
categories:
  - Docs

---
　[OpenSSH 5.6/5.6p1リリース][1]の記事をチェックしているとき、リリースノートの「多重（multiplex）接続」ってなんじゃこれ、と思い調べてみたんですが、なかなかに有用なのでちょいとまとめてみました。というか、元ネタはこちらの[SSH: Tips And Tricks You Need][2]という記事です。

　多重接続というのは、1本のSSHコネクションで複数のセッションを同時に張るという感じのもの。たとえば、OS Xでターミナルを複数開き、それぞれのターミナルウィンドウで1つのサーバーに対しsshコマンドで接続を行った場合、通常はサーバー側では複数のsshdが起動し、それぞれのsshクライアントと通信を行います。いっぽう、多重接続を利用すると1つのsshdが複数のsshと通信する形となり、サーバー側のリソースをより効率的に利用できる、というわけ。

　設定は簡単で、クライアント側の.sshディレクトリに設定ファイルと一時ディレクトリを用意するだけ。

<pre>$ cd ~/.ssh
$ mkdir connections
$ chmod 700 connections/
$ vim config
</pre>

　~/.ssh/configの内容は下記のとおり。

<pre class="code">Host *
ControlMaster auto
ControlPath ~/.ssh/connections/%r_%h_%p
</pre>

　あとは、通常通りsshでサーバーに接続するだけ。これだけで、体感できるほど2つめ以降の接続が高速化されます。下記は5つのSSHセッションを張った状態で、6つめのセッションを張ろうとした際の実行速度ベンチマーク。

<pre>多重化なし：
$ time ssh hylom.******.com uptime
 08:13:53 up 22 days, 10:18,  6 users,  load average: 0.00, 0.00, 0.00

real	0m2.123s
user	0m0.015s
sys	0m0.010s
</pre>

<pre>多重化あり：
Last login: Tue Aug 24 17:15:34 on ttys006
$ time ssh hylom.******.com uptime
 08:18:53 up 22 days, 10:23,  6 users,  load average: 0.00, 0.00, 0.00

real	0m0.278s
user	0m0.006s
sys	0m0.007s
</pre>

　多重化により、だいたい7.6倍くらい速くなっています。ちなみに、この状態で「ps ux」を実行してみるとこんな感じに。

<pre>$ ps ux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
hylom    17182  0.2  0.2   8292  1580 ?        S    08:21   0:00 sshd: hylom@pts
hylom    17183  0.0  0.2   2968  1584 pts/0    Ss+  08:21   0:00 -sh
hylom    17188  0.0  0.2   2968  1584 pts/1    Ss+  08:21   0:00 -sh
hylom    17193  0.0  0.2   2968  1584 pts/2    Ss+  08:21   0:00 -sh
hylom    17198  0.0  0.2   2968  1588 pts/3    Ss+  08:21   0:00 -sh
hylom    17203  0.0  0.2   2968  1580 pts/4    Ss+  08:21   0:00 -sh
hylom    17208  1.0  0.3   3484  1856 pts/5    Ss   08:21   0:00 -sh
hylom    17213  0.0  0.1   2432   908 pts/5    R+   08:21   0:00 ps ux
</pre>

　sshdは1つだけで、接続毎にシェルだけが起動されるようになっていることが確認できます。

 [1]: http://sourceforge.jp/magazine/10/08/24/0758204
 [2]: http://symkat.com/35/ssh-tips-and-tricks-you-need/