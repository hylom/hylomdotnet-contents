---
slug: enable-directory-access-when-selinux-enabled
title: SELinux有効下でhttpdから特定のディレクトリへのアクセスを許可する
tags: [ selinux,security ]
date: 2013-06-03T17:30:06+09:00
lastmod: 2013-09-20T19:55:46+09:00
publishDate: 2013-06-03T17:30:06+09:00
---

<p>　SELinuxを有効にしていると、httpdがアクセスできるディレクトリに制限がかかる。それを解除するための手順メモ。</p>

<p>　まず、semanageコマンドでhttpdからのアクセスを許可するディレクトリを登録する。</p>

<pre>
# semanage fcontext -a -t httpd_sys_content_t ＜対象ディレクトリ＞
</pre>

<p>　なお、semanageコマンドがインストールされていない場合はpolicycoreutils-pythonパッケージをインストールすればOK。</p>

<p>　次に、そのディレクトリに対しrestoreconコマンドを実行してラベルを設定させる。</p>

<pre>
# restorecon ＜対象ディレクトリ＞
</pre>

<p>　最後にls -Zコマンドで適切にラベルが設定されているかを確認する。例えば下記の例は/foobarをhttpdからアクセス可能にしたもの。</p>

<pre>
# ls -Zd /foobar
drwxr-xr-x. root root unconfined_u:object_r:httpd_sys_content_t:s0 /foobar
</pre>

<p>　あとは適切にパーミッションを設定すればOK。
