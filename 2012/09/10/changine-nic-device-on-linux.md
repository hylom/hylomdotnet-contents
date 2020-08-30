---
slug: changine-nic-device-on-linux
title: NICのデバイス名を変更する
tag: [ linux, configuration, tips ]
date: 2012-09-10T19:38:15+09:00
lastmod: 2012-09-10T19:38:15+09:00
publishDate: 2012-09-10T19:38:15+09:00
---

<p>　CentOSにおいて、複数のNICを搭載しているマシンでNICに対応しているデバイス名を変更したい場合、次のような手順をとれば良い。</p>

<p>　まず、ネットワークを停止させる。</p>

<pre>
# service network stop
</pre>

<p>　次に、NICのモジュールをいったんアンロードする。たとえば「e1000e」モジュールを使っている場合、次のようにする。</p>

<pre>
# rmmod e1000e
</pre>

<p>　udevの設定ファイルを編集する。ネットワークデバイスについてのMACアドレスとデバイス名の対応付けは、「/etc/udev/rules.d/70-persistent-net.rules」というファイルに記述されている。</p>

<p>　このファイルを適当に編集したら、「/etc/sysconfig/network-scripts/ifcfg-eth?」ファイルの「HWADDR」行を削除する。</p>

<p>　以上で設定完了。この状態で次のようにネットワークを再起動させると、デバイスファイル名とNICの対応が変更されているはず。</p>

<pre>
# service network start
</pre>


