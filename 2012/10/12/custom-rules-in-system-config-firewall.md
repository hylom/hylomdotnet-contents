---
slug: custom-rules-in-system-config-firewall
title: CentOS（RHEL） 6のsystem-config-firewallでカスタムルールを使っている場合の注意
tags: [ firewall, centos6, rhel6, configure ]
date: 2012-10-12T18:36:03+09:00
lastmod: 2012-10-12T18:36:03+09:00
publishDate: 2012-10-12T18:36:03+09:00
---

<p>　CentOS 6（というかRHEL 6のクローン）ではFirewallの設定を行うsystem-config-firewallというツールがある。CUIでも使えて簡単に主要プロトコルのファイアウォール設定ができるのだが、このUI上では込み入った設定は行えない。そのため、たとえば特定のIPアドレスからの接続のみを許可したい場合などは、カスタムルールを使って別ファイルにiptablesのオプションを並べる必要がある。</p>

<p>　この場合、カスタムルールを記述したファイルを編集した後は必ずsystem-config-firewallを実行して、（何も設定を変更せずに）OKを選択しないと設定が反映されない模様。なぜ？</p>
