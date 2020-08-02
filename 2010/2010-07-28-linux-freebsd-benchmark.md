---
title: LinuxとFreeBSDのベンチマーク比較
author: hylom
type: post
date: 2010-07-27T17:10:30+00:00
url: /2010/07/28/linux-freebsd-benchmark/
categories:
  - News
tags:
  - benchmark
  - freebsd
  - linux

---
　やや旧聞となるが、PhoronixがLinuxとFreeBSDのベンチマーク比較を行っている（[Debian Linux Benchmarked Against Debian GNU/kFreeBSD &#038; FreeBSD][1]）。比較対象はDebian kFreeBSD 7.3、Debian kFreeBSD 8.0、Debian GNU/Linux（カーネル2.6.32）、FreeBSD 7.3、FreeBSD 8.0。

　「Debian kFreeBSD」はカーネルとしてFreeBSD、ユーザーランドとしてDebianを採用したものだ。Debian GNU/LinuxとDebian kFreeBSDはカーネルだけが異なり、またDebian kFreeBSDとFreeBSDはユーザーランドだけが異なる。これらを比較することで、ユーザーランドもしくはカーネルだけの性能比較が行える（と期待できる）点で興味深いベンチマークである。

　ベンチマーク結果であるが、gzipでの圧縮やGnuPGでの暗号化、MAFFT（分子生物学向けの核酸・アミノ酸アライメント作成ツール）、GraphicsMagickによる画像のリサイズ処理、Himeno BenchmarkについてはDebian kFreeBSDやDebian GNU/Linuxが高パフォーマンス、という結果だった。いっぽう、C-Rayでの3DグラフィックレンダリングについてはFreeBSD 7.3/8.0が高速な傾向が見られている。

　また、Debian GNU/LinuxがFreeBSDやDebian kFreeBSDよりも高速だったのはdCrawによるRAW画像の現像処理、Sudokut（数独演算アプリ）、SQLiteのインサート処理。

　このようにベンチマークごとに結果はばらばらであり、DebianのユーザーランドとFreeBSDのユーザーランドのどちらが高速か、またLinuxカーネルとFreeBSDのカーネルのどちらが高速かは単純には言えないという、なんともモヤモヤとした結論となっている。このベンチマークでは実行マシンとしてThinkPad R52とThinkPad T61を使用しているが、マシンによって結果が違うのも微妙なところだ。

ただし、マルチスレッドによるI/O処理ベンチマークについては、特にランダムWriteについてはLinuxカーネルのほうがパフォーマンスを発揮する傾向があるようだ。

 [1]: http://www.phoronix.com/scan.php?page=article&#038;item=debian_kfreebsd_h210
