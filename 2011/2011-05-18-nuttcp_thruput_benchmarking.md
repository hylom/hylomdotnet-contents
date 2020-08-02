---
title: nuttcpでネットワークスループットを測る
author: hylom
type: post
date: 2011-05-18T09:40:48+00:00
url: /2011/05/18/nuttcp_thruput_benchmarking/
categories:
  - Docs

---
　ネットワークのスループットを測るツールには色々ある。SourceForge.JP Magazineの翻訳記事（[ネットワークのベンチマーク・ツールを試す &#8211; nepim、LMbench、nuttcp][1]）でいくつか紹介されているのだが、その中でも自分が比較的よく使っているのが[nuttcp][2]だ。ということで簡易的な使い方メモ。

#### インストール

　ソースコードからビルドしても良いが、[nuttcpのダウンロードサイト][3]にはRPMパッケージもあるので、こちらを利用するのが楽である。

#### ベンチマークの実行

　nuttcpはクライアント/サーバー型のベンチマークツールである。つまり、帯域測定をしたいネットワークの片側でサーバーを動かし、もう片側でクライアントを実行してベンチマークを行う。

　サーバー側では「-S」オプション付きでnuttcpを実行しておく。

\# nuttcp -S

　クライアント側では、サーバーのIPアドレス付きでnuttcpを実行する。上り速度を測定するには「-B」を、下り速度を測定するには「-D」オプションを使う。「-i＜数字＞」オプションを付けると、数字で指定した間隔で途中経過を表示する。「-v」や「-vv」で経過や結果の詳細表示。

　次の例はクライアントからサーバーへの上り速度を測定する場合。

<pre>$ nuttcp -B -i1 183.181.28.64
    7.1875 MB /   1.00 sec =   60.2683 Mbps     0 retrans
    7.1875 MB /   1.00 sec =   60.2960 Mbps     0 retrans
    7.6875 MB /   1.00 sec =   64.4898 Mbps     0 retrans
    7.7500 MB /   1.00 sec =   65.0148 Mbps     0 retrans
    8.0000 MB /   1.00 sec =   67.1111 Mbps     0 retrans
    8.1250 MB /   1.00 sec =   68.0925 Mbps     0 retrans
    7.8750 MB /   1.00 sec =   66.0627 Mbps     0 retrans
    7.6875 MB /   1.00 sec =   64.4892 Mbps     0 retrans
    7.5000 MB /   1.00 sec =   62.9117 Mbps     0 retrans
    8.1875 MB /   1.00 sec =   68.6899 Mbps     0 retrans

   77.6250 MB /  10.07 sec =   64.6675 Mbps 0 %TX 6 %RX 0 retrans 9.35 msRTT
</pre>

　下り速度の測定は次のような感じ。

<pre>$ nuttcp -D -i1 183.181.28.64
    6.1250 MB /   1.00 sec =   51.3391 Mbps     0 retrans
    7.5625 MB /   1.00 sec =   63.4470 Mbps     0 retrans
    7.3750 MB /   1.00 sec =   61.8740 Mbps     0 retrans
    7.3125 MB /   1.00 sec =   61.3443 Mbps     0 retrans
    6.9375 MB /   1.00 sec =   58.1962 Mbps     0 retrans
    7.1875 MB /   1.00 sec =   60.2891 Mbps     0 retrans
    7.3750 MB /   1.00 sec =   61.8149 Mbps     0 retrans
    7.7500 MB /   1.00 sec =   65.0144 Mbps     0 retrans
    7.5625 MB /   1.00 sec =   63.4413 Mbps     0 retrans
    7.5625 MB /   1.00 sec =   63.4363 Mbps     0 retrans

   73.2500 MB /  10.07 sec =   60.9941 Mbps 0 %TX 5 %RX 0 retrans 9.11 msRTT
</pre>

 [1]: http://sourceforge.jp/magazine/08/08/22/0159234
 [2]: http://www.wcisd.hpc.mil/nuttcp/Nuttcp-HOWTO.html
 [3]: http://www.lcp.nrl.navy.mil/nuttcp/
