---
title: CentOS 5を延命させる
author: hylom
type: post
date: 2012-04-17T05:14:56+00:00
url: /2012/04/17/centos-5-with-epel/
categories:
  - Hacks
tags:
  - centos
  - linux
  - programming

---
　CentOS 5を使っていると、含まれているソフトウェアのバージョンが古かったり、そもぞもリポジトリにそのソフトウェアがなかったりして困ることがある。さっさとCentOS 6にアップデートすればいい話なのだが、面倒くさいとか、そもそもフルバックアップしないと行けないとか色々と大変だったりするので（CentOS 5からCentOS 6へのアップデートは再インストールが推奨されている）、なんとかまだCentOS 5をこのまま使いたい、そんな時に役立つのがEPEL。

　[EPEL][1]は「Extra Packages for Enterprise Linux」の略で、Fedora Projectが運営しているRed Hat Enterprise Linuxおよびその互換OS向けのパッケージリポジトリ。同種のものにrpmforgeがあるわけですが、Fedora Projectが運営しているということでEPELのほうがやや信頼感が（個人的には）高いということでこちらを使うことに。

　導入方法は簡単。以下を実行するだけ。

<pre>$ sudo rpm -Uvh http://ftp.jaist.ac.jp/pub/Linux/Fedora/epel/5/i386/epel-release-5-4.noarch.rpm
</pre>

　これでgitとかpython26とかをyumでインストールできるようになります。

 [1]: http://fedoraproject.org/wiki/EPEL/FAQ
