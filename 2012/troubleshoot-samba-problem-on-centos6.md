---
slug: troubleshoot-samba-problem-on-centos6
title: CentOS 6のSambaでファイル共有時に問題が発生したら
tags: [ linux,centos,samba ]
date: 2012-09-12T16:05:34+09:00
lastmod: 2012-09-12T16:05:34+09:00
publishDate: 2012-09-12T16:05:34+09:00
---

<P>　CentOS 6のSambaでファイル共有がうまく行かない場合、SELinuxによって各種アクセスがブロックされている可能性がある。詳細はsamba_selinuxドキュメントに記載されている。</p>

<pre>
$ man samba_selinux
</pre>

<p>　とりあえず、smbclientでログインには成功するのにホームディレクトリにアクセスできない、という場合、次のコマンドで解決できた。</p>

<pre>
# setsebool -P samba_enable_home_dirs 1
</pre>
