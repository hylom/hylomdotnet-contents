---
slug: iodrive-with-ubuntu-1804
title: Ubuntu 18.04でioDriveを使う
tag: [ ubntu, linux ]
date: 2019-01-29T17:31:54+09:00
lastmod: 2019-05-17T22:24:57+09:00
publishDate: 2019-01-29T17:31:54+09:00
---

　一昔前にフラッシュメモリベースのデータセンター向けストレージ「ioDrive」が[一瞬話題になった](https://knowledge.sakura.ad.jp/1724/)が、このioDriveはUbuntu 18.04を公式にはサポートしていない。うっかり使っているサーバーをUbuntu 16.04から18.04にアップデートしてしまいトラブったのだが、自前でドライバをビルドすることでとりあえず動くようにはなる。当然サポート範囲外だが、手順をメモしておく。

　まず、Ubuntu 18.04にアップデートして再起動した時点でioDriveをマウントできなくなり、/etc/fstabで起動時にioDriveをマウントするよう設定している場合復旧モードで起動する羽目になる。そのため、まずはここで/etc/fstabを編集し、ioDriveに関する宇の記述をコメントアウトする。自分の環境ではioDriveは/dev/fioa1として認識されていたので、この記述をコメントアウト。

```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda1 during installation
UUID=29279b34-d2fd-4a10-b3ac-378884b6f579 /               ext4    relatime,errors=remount-ro 0       1
# swap was on /dev/sda5 during installation
UUID=ff4e823a-c074-41bf-aa7c-5e63bd8c3f6a none            swap    sw              0       0
#/dev/fioa1 /fioa1 ext4 auto,rw,relatime,stripe=8,data=ordered 0 0
```

　続いて[Western Digitalのサポートサイト](https://portal.wdc.com/Support/s/)の「Downloads」リンク経由で最新のドライバを入手する（要アカウント登録）。ダウンロードページで「ioDrive」－「Linux_ubuntu-16.04」－「Current Version」（今回使用したのは「3.2.16」）を選択して「Software Source」からソースtarball（今回は「iomemory-vsl_3.2.16.1731-1.0.tar.gz」）をダウンロードする。なお、このページはCORS関連の問題でChromeではまともに動作しないようだ（Firefoxではダウンロードできた）。

　ダウンロードしたアーカイブを適当なディレクトリに展開する。

```
$ tar xvzf iomemory-vsl_3.2.16.1731-1.0.tar.gz
$ cd iomemory-vsl-3.2.16.1731/
```

　このソースtarballにはroot/usr/src/iomemory-vsl-3.2.16/kfio/以下にコンパイル済みオブジェクトファイル（いわゆるバイナリblob）が含まれており、このオブジェクトファイルをコンパイル時にリンクして使用するようになっている。このオブジェクトファイルは異なるコンパイラでビルドしたと思われる複数のものが用意されており、ファイル名の「cc??」の部分がコンパイラのバージョンに対応するようだ。今回使用したiomemory-vsl_3.2.16.1731-1.0.tar.gzでは次のようにGCC 4.1/4.3/4.4/4.8/4.9/5.3/5.4/6.3用のバイナリが入っていた。

```
$ /root/usr/src/iomemory-vsl-3.2.16/kfio/
x86_64_cc41_libkfio.o_shipped  x86_64_cc44_libkfio.o_shipped  x86_64_cc49_libkfio.o_shipped  x86_64_cc54_libkfio.o_shipped
x86_64_cc43_libkfio.o_shipped  x86_64_cc48_libkfio.o_shipped  x86_64_cc53_libkfio.o_shipped  x86_64_cc63_libkfio.o_shipped
```

　Ubuntu 18.04のデフォルトのGCCはバージョン7.3だが、これに対応するバージョンのバイナリはない。ただ幸いなことにUbuntu 18.04ではGCC 4.8がパッケージで提供されているので、これを利用する。

```
# apt-get install gcc-4.8
```

　また、debhelperとdpkg-devパッケージも必要なのでインストールしておく。

```
# apt-get install debhelper dpkg-dev
```

　GCC 4.8をインストールしたら、次のように「CC=gcc-4.8」を指定して「dpkg-buildpackage」コマンドを実行する。

```
$ CC=gcc-4.8 dpkg-buildpackage -b -us -uc
```

　正常にコンパイルとパッケージ作成が完了すると、親ディレクトリに次のようにファイルが作成される。

```
$ cd ..
$ ls -1
iomemory-vsl-3.2.16.1731
iomemory-vsl-4.15.0-43-generic_3.2.16.1731-1.0_amd64.deb
iomemory-vsl-config-4.15.0-43-generic_3.2.16.1731-1.0_amd64.deb
iomemory-vsl-source_3.2.16.1731-1.0_amd64.deb
iomemory-vsl_3.2.16.1731-1.0.tar.gz
iomemory-vsl_3.2.16.1731-1.0_amd64.buildinfo
iomemory-vsl_3.2.16.1731-1.0_amd64.changes
```

　このうち、「iomemory-vsl-4.15.0-43-generic_3.2.16.1731-1.0_amd64.deb」をインストールすれば良い。そのため、まずすでにインストールされているパッケージをアンインストールする。

```
# dpkg -r iomemory-vsl-source iomemory-vsl-config-3.13.0-77-generic  iomemory-vsl-3.13.0-77-generic libvsl
```

　続いて新たに作成したパッケージをインストールする。

```
# dpkg -i iomemory-vsl-4.15.0-43-generic_3.2.16.1731-1.0_amd64.deb
```

　最後にmodprobeコマンドで「iomemory-vsl」モジュールをロードすればioDriveが利用可能になる。fstabファイルでコメントアウトした部分を元に戻し、問題なくマウントできればOK。

```
# modprobe iomemory-vsl
# vi /etc/fstab
# mount /fioa1
```

