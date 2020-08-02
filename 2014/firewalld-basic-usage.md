---
slug: firewalld-basic-usage
title: firewalldでのファイアウォール制御・超基本編
tags: [ linux, firewalld, システム管理 ]
date: 2014-12-19T17:15:32+09:00
lastmod: 2015-06-14T17:33:39+09:00
publishDate: 2014-12-19T17:15:32+09:00
---

<p>　Red Hat Enterprise Linux 7（やCentOS 7など）では、iptablesなどによるパケット制御をfirewalldで行うようになった。このfirewalldを使って、ファイアウォールの設定を行う手順メモ。</p>

<h3>前提条件</h3>

<ul>
<li>systemctlコマンドでfirewalldを稼動させておく</li>
<li>firewalldの設定は「firewall-cmd」コマンドで行う</li>
</ul>

<h3>zone設定</h3>
<p>　firewalldには「ゾーン」という概念があり、ゾーンごとに有効なポートなどを指定する。デフォルトで用意されているゾーンには「public」や「home」、「trusted」などが用意されている。</p>

<p>　現在有効なゾーンは「firewall-cmd --list-all」コマンドで確認できる。</p>

<pre class="shell bash">
# firewall-cmd --list-all
public (default, active)
  interfaces: enp8s0 virbr0 virbr1
  sources:
  services: dhcpv6-client samba ssh
  ports:
  masquerade: no
  forward-ports:
  icmp-blocks:
  rich rules:
</pre>

<p>　この例では、「enp8s0」および「virbr0」、「virbr1」というインターフェイスが「public」ゾーンに割り当てられている。また、publicゾーンでは「dhcpv6-client」と「samba」、「ssh」というサービスが有効になっている。</p>

<h3>サービスの追加</h3>
<p>　ゾーンに「サービス」を追加することで、そのサービスを追加できる。定義されているサービスは「firewall-cmd --get-services」コマンドで確認できる。</p>

<pre class="shell bash">
# firewall-cmd --get-services
amanda-client bacula bacula-client dhcp dhcpv6 dhcpv6-client dns ftp high-availability http https imaps ipp ipp-client ipsec kerberos kpasswd ldap ldaps libvirt libvirt-tls mdns mountd ms-wbt mysql nfs ntp openvpn pmcd pmproxy pmwebapi pmwebapis pop3s postgresql proxy-dhcp radius rpc-bind samba samba-client smtp ssh telnet tftp tftp-client transmission-client vnc-server wbem-https
</pre>

<p>　特定のゾーンで許可されているサービスは「firewall-cmd --list-service --zone=＜ゾーン名＞」で確認できる。</p>

<pre class="shell bash">
# firewall-cmd --list-service --zone=public
dhcpv6-client samba ssh
</pre>

<p>　ゾーンにサービスを追加するには、「firewall-cmd --add-service=＜サービス名＞ --zone=＜ゾーン名＞」コマンドを使用する。下記は「public」ゾーンに「http」サービスを追加する例。</p>

<pre class="shell bash">
# firewall-cmd --list-service --zone=public
dhcpv6-client mysql samba ssh
# firewall-cmd --add-service=http --zone=public
success
# firewall-cmd --list-service --zone=public
dhcpv6-client http mysql samba ssh
</pre>

<p>　なお、--add-serviceオプションで追加したサービスは、firewalldの再起動後には保持されない。恒久的にサービスを追加するには、「--permanent」オプションを指定する。この場合、即座にはサービスが追加されないので、その後に「firewall-cmf --reload」コマンドを実行してfirewalldの設定をリロードさせると変更が反映される。</p>

<pre class="shell bash">
# firewall-cmd --add-service=http --zone=public --permanent
success
# firewall-cmd --list-service --zone=public
dhcpv6-client samba ssh
# firewall-cmd --reload
</pre>

<p>　また、追加したサービスを削除するには「--remove-service」オプションを使用する。</p>

<pre class="shell bash">
# firewall-cmd --remove-service=dhcpv6-client --zone=public
</pre>

