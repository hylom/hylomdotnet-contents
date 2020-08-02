---
slug: systemd-service-control-basics
title: systemdでのサービス制御・超基本編
tags: [ systemd, linux ]
date: 2014-12-19T16:55:35+09:00
lastmod: 2014-12-19T16:56:05+09:00
publishDate: 2014-12-19T16:55:35+09:00
---

<p>　Red Hat Enterprise Linux 7（やCentOS 7など）で導入されたsystemdで、サービスの開始/停止やシステム起動後の自動起動などを設定する手順メモ。</p>

<p>　systemdでは、「systemctl」というコマンドでサービスの制御を行う。サービスを開始/停止するには「start」および「stop」サブコマンドを使用する。また、「status」サブコマンドで稼働状況をチェックできる。</p>

<pre>
systemctl start ＜サービス名＞
systemctl stop ＜サービス名＞
systemctl status ＜サービス名＞
</pre>

<p>　システムの起動時にサービスを自動起動させるには「enable」サブコマンドを、自動起動させないように設定するには「disable」サブコマンドを使う。</p>

<pre>
systemctl enable ＜サービス名＞
systemctl disable ＜サービス名＞
</pre>

<p>　稼働中のサービスの確認は、「list-units」サブコマンドで行える。サブコマンドを省略すると「list-units」サブコマンドが実行されるので、引数無しでsystemctlコマンドを実行しても同じ結果が得られる。</p>

<pre class="bash shell">
# systemctl
UNIT                        LOAD   ACTIVE SUB       DESCRIPTION
proc-sys...t_misc.automount loaded active waiting   Arbitrary Executable File Fo
sys-devi...-sda-sda1.device loaded active plugged   VBOX_HARDDISK
  ：
  ：
</pre>

<p>　このうち、「.service」で終わっているものがサービスとなる。また、「-t service」オプション付きでsystemctlコマンドを実行することでサービスのみを一覧表示できる。</p>

<pre class="shell bash">
$ systemctl -t service
</pre>

<p>　また、「list-units」サブコマンドでは「disabled」に設定されているサービスは表示されない。これらも含めて確認するには、「list-unit-files」サブコマンドを実行する。</p>

<pre class="shell bash">
$ systemctl list-unit-files
</pre>

