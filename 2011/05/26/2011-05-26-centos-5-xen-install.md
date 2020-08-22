---
title: CentOS 5.6上でXenを使って仮想環境を作るための基本設定
author: hylom
type: post
date: 2011-05-26T10:43:11+00:00
url: /2011/05/26/centos-5-xen-install/
categories:
  - Docs
tags:
  - centos
  - linux
  - virtualization
  - xen

---
　先日MSDNを契約、テスト用に自由にOSを使えるようになったので、テスト用のCore i7マシンにXenを導入して仮想マシン上でテスト環境を作ろう、という話。いままではテスト環境が必要になったら実環境上にインストール→不要になったら削除、を繰り返していたんだけど、仮想環境を使えばスナップショットも取れるし便利だろう、ということで。

　ベースの環境はCentOS 5.6。CentOS 5.6上にXen環境を構築する解説はネット上にたくさんあるわけですが、その多くがGUIを使ったセットアップ方法を解説していて、コンソールベースのCentOS環境でインストールする方法の解説は少なかったので以下に手順をメモしておきます。

　まず、仮想化関連パッケージを導入。

<pre># yum groupinstall Virtualization
# yum install kernel-xen
</pre>

　Xenを動かすには専用カーネルが必要なので、/boot/grub/menu.lstを確認してXen対応カーネル（2.6.xx-xxx.x.x.el5xen）でブートされるように設定してリブート。また、xendおよびxendomainsサービスを起動するように設定しておく。

<pre># /sbin/chkconfig xend on
# /sbin/chkconfig xendomains on
# /sbin/service xend start
# /sbin/sercice xendomains start
</pre>

　仮想マシンの作成とOSインストールは「virt-install」コマンドで行える。Fedora 15をインストールするなら下記のような感じに。

<pre># /usr/sbin/virt-install --nographics --prompt
Would you like a fully virtualized guest (yes or no)? This will allow you to run unmodified operating systems. no
 What is the name of your virtual machine? fedora
 How much RAM should be allocated (in megabytes)? 1024
 What would you like to use as the disk (file path)? /var/lib/xen/images/fedora.img
 How large would you like the disk (/var/lib/xen/images/fedora.img) to be (in gigabytes)? 10
 What is the install URL? http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/releases/15/Fedora/i386/os/
　：
　：
インストールを開始しています...
ファイル .treeinfo を読出中...                             |  906 B     00:00
ファイル vmlinuz-PAE を読出中...                           | 3.7 MB     00:00     TA
ファイル initrd-PAE.img を読出中...                        |  94 MB     00:40     TA
ストレージファイルを作成中...                         |  10 GB     00:00
ドメインを作成中...                                        |    0 B     00:04
Connected to domain fedora
エスケープ文字は  ^] です
[    0.000000] Reserving virtual address space above 0xf5800000
[    0.000000] Initializing cgroup subsys cpuset
　：
　：
</pre>

　コンソール上で仮想環境上のコンソールが表示され、インストールを行える。

<div id="attachment_1392" style="width: 410px" class="wp-caption aligncenter">
  <a href="/img/blog/2011/05/xen_f15_inst.png"><img src="/img/blog/2011/05/xen_f15_inst-400x278.png" alt="コンソール上でFedoraのインストーラを操作する" title="コンソール上でFedoraのインストーラを操作する" width="400" height="278" class="size-medium wp-image-1392" srcset="/img/blog/2011/05/xen_f15_inst-400x278.png 400w, /img/blog/2011/05/xen_f15_inst.png 757w" sizes="(max-width: 400px) 100vw, 400px" /></a>
  
  <p class="wp-caption-text">
    コンソール上でFedoraのインストーラを操作する
  </p>
</div>

　インストール完了語は、Ctrl-]でコンソールを抜けられる。稼働中の仮想マシンは「xm list」コマンドで確認可能。

<pre># /usr/sbin/xm list
Name                                      ID Mem(MiB) VCPUs State   Time(s)
Domain-0                                   0     2012     8 r-----    780.4
fedora                                     2     1024     1 -b----      9.9
</pre>

　仮想マシンのコンソールに接続するには、「xm console ＜仮想マシン名＞」を実行すればよい。コンソール接続の終了は先と同様Crtl-]。

<pre># /usr/sbin/xm console fedora
</pre>
