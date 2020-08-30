---
title: CentOS 6の初期設定メモ1
author: hylom
type: post
date: 2012-07-24T09:25:48+00:00
url: /2012/07/24/centos-initial-setup/
category:
  - 未分類
tag:
  - centos
  - hack
  - linux

---
　CentOS 6の初期設定メモその1。ユーザーを作成してSSHの設定を行うまで。

#### ユーザーの作成

<pre># groupadd hylom
# useradd -d /home/hylom -g hylom -m hylom
# chsh -s /bin/bash hylom
# passwd hylom
</pre>

#### sudoの設定

　sudoersファイルを編集する。

<pre># yum install sudo
# visudo
</pre>

　sudoersファイルに次のようにhylomを追加。

<pre>## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL
hylom   ALL=(ALL)       ALL
</pre>

#### SSH関連の設定

　SSH公開鍵を作成する。

<pre># su hylom
$ ssh-keygen
$ cd ~/.ssh
$ vi authorized_keys 
$ chmod 600 authorized_keys
</pre>

　authorized_keysにはログインに使用する公開鍵をコピー＆ペーストしておく。

　SSHサーバーの設定。

<pre># vi /etc/ssh/sshd_config
</pre>

　sshd_configファイルでPermitRootLoginをnoに、PasswordAuthenticationをnoに設定し、rootでのログインを禁止＆認証に公開鍵必須とする。

<pre>#PermitRootLogin yes
PermitRootLogin no
</pre>

<pre>#PasswordAuthentication yes
PasswordAuthentication no
</pre>

#### ホスト名の設定

<pre># vi /etc/sysconfig/network
# hostname &lt;hostname&gt;
</pre>
