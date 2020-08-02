---
slug: firewalld-change-interface-permanent-can-not-affect-on-centos-7
title: CentOS 7で「firewalld --permanent --change-interface」コマンドが動作しない問題の解決法
tags: [ centos7,firewalld ]
date: 2016-07-12T19:57:27+09:00
lastmod: 2016-07-12T20:01:48+09:00
publishDate: 2016-07-12T19:57:27+09:00
---

　CentOS 7のfirewalldで特定のネットワークインターフェイスを特定のゾーンに関連付けるには、「firewall-cmd --zone=＜ゾーン＞ --change-interface=＜インターフェイス＞」コマンドを使えとmanページに書いてある。このコマンド自体は正常に働くのだが、設定を永続的に保存するための「--permanent」オプションがうまく動かない。具体的には、firewalldを再起動すると設定が消えてしまう。

　実は、CentOSの元になっているRed Hatの「[Bug Fix Advisory firewalld bug fix and enhancement update](https://rhn.redhat.com/errata/RHBA-2015-0520.html)（2015年3月5日付け）を見ると、「The "--permanent --add-interface" option is supposed to be used only for interfaces that are not managed by the NetworkManager utility」と書いてある。つまり、nmtuiなどのツール経由で設定された、NetworkManager下で管理されているネットワークインターフェイスについては、--add-interfaceや--change-interfaceオプション利用時に--permanentオプションを指定しても効果が無いようだ。

　対処策としては、NetworkManager側でネットワークインターフェイスとゾーンの対応付けを行えば良い。ただし、nmtuiコマンドではゾーンの設定項目が無いため、nmcliコマンドでの設定が必要となる。

　まず、「nmcli c」コマンドで認識されているネットワークコネクションを確認する。

```
# nmcli c
名前                UUID                                  タイプ          デバイス
Wired connection 1  d2ee88e7-2e1c-4168-a1ad-8bd5b6ac4db3  802-3-ethernet  eth1
System eth0         5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  802-3-ethernet  eth0
```

　ネットワークコネクションの詳細設定は「nmcli c show ＜コネクション名＞」で確認できる。

```
# nmcli c show "Wired connection 1"
connection.id:                          Wired connection 1
connection.uuid:                        d2ee88e7-2e1c-4168-a1ad-8bd5b6ac4db3
connection.interface-name:              --
connection.type:                        802-3-ethernet
connection.autoconnect:                 yes
connection.autoconnect-priority:        0
connection.timestamp:                   1468320004
connection.read-only:                   no
connection.permissions:
connection.zone:                        --
connection.master:                      --
connection.slave-type:                  --
connection.autoconnect-slaves:          -1 (default)
connection.secondaries:
connection.gateway-ping-timeout:        0
connection.metered:                     不明
802-3-ethernet.port:                    --
802-3-ethernet.speed:                   0
802-3-ethernet.duplex:                  --
802-3-ethernet.auto-negotiate:          yes
802-3-ethernet.mac-address:             9C:A3:BA:28:8B:E2
802-3-ethernet.cloned-mac-address:      --
802-3-ethernet.mac-address-blacklist:
802-3-ethernet.mtu:                     自動
802-3-ethernet.s390-subchannels:
802-3-ethernet.s390-nettype:            --
802-3-ethernet.s390-options:
802-3-ethernet.wake-on-lan:             1 (default)
802-3-ethernet.wake-on-lan-password:    --
ipv4.method:                            manual
ipv4.dns:
ipv4.dns-search:
ipv4.addresses:                         192.168.1.10/24
ipv4.gateway:                           --
ipv4.routes:
ipv4.route-metric:                      -1
ipv4.ignore-auto-routes:                no
ipv4.ignore-auto-dns:                   no
ipv4.dhcp-client-id:                    --
ipv4.dhcp-send-hostname:                yes
ipv4.dhcp-hostname:                     --
ipv4.never-default:                     yes
ipv4.may-fail:                          yes
ipv6.method:                            auto
ipv6.dns:
ipv6.dns-search:
ipv6.addresses:
ipv6.gateway:                           --
ipv6.routes:
ipv6.route-metric:                      -1
ipv6.ignore-auto-routes:                no
ipv6.ignore-auto-dns:                   no
ipv6.never-default:                     no
ipv6.may-fail:                          yes
ipv6.ip6-privacy:                       -1 (不明)
ipv6.dhcp-send-hostname:                yes
ipv6.dhcp-hostname:                     --
GENERAL.名前:                           Wired connection 1
GENERAL.UUID:                           d2ee88e7-2e1c-4168-a1ad-8bd5b6ac4db3
GENERAL.デバイス:                       eth1
GENERAL.状態:                           アクティベート済み
GENERAL.デフォルト:                     いいえ
GENERAL.デフォルト6:                    いいえ
GENERAL.VPN:                            いいえ
GENERAL.ゾーン:                         --
GENERAL.DBUS パス:                      /org/freedesktop/NetworkManager/ActiveConnection/679
GENERAL.CON パス:                       /org/freedesktop/NetworkManager/Settings/1
GENERAL.スペックオブジェクト:           /
GENERAL.マスターパス:                   --
IP4.アドレス[1]:                        192.168.1.10/24
IP4.ゲートウェイ:
IP6.アドレス[1]:                        fe80::9ea3:baff:fe28:8be2/64
IP6.ゲートウェイ:
```

　ここで、「connection.zone」というのがゾーン設定になる。デフォルトではゾーンが指定されていないが、これを変更するには「nmcli c mod ＜コネクション名＞ ＜設定対象＞ ＜設定する値＞」コマンドを実行する。たとえば、eth1を「internal」ゾーンに指定する場合は次のようになる

```
# nmcli c mod "Wired connection 1" connection.zone internal
```

　これでfirewalldを再起動すると、eth1がinternalゾーンに割り当てられるようになる。

```
# systemctl restart firewalld
# firewall-cmd --get-active-zones
internal
  interfaces: eth1
public
  interfaces: eth0
```

