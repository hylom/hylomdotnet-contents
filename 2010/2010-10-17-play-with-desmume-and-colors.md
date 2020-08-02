---
title: DSエミュで（合法的に）遊ぶ
author: hylom
type: post
date: 2010-10-17T09:16:41+00:00
url: /2010/10/17/play-with-desmume-and-colors/
categories:
  - Docs
tags:
  - Emulator
  - NDS
  - Software

---
　最近DeSmuMEなるニンテンドーDSエミュレーターが（一部で）ブームらしい。[Googleトレンドの検索結果][1]を見てもその盛り上がりは明らかで、2010年9月中旬（というか9月18日）に大きな山があることが分かる。この9月18日はポケモン新作の発売日ということで、まぁなんだかなぁ、という感じではあるのだが……。

<div id="attachment_1337" style="width: 410px" class="wp-caption aligncenter">
  <a href="/img/blog/2010/10/trend_ds2.png"><img src="/img/blog/2010/10/trend_ds2-400x301.png" alt="DeSmuMEのトレンド" title="DeSmuMEのトレンド" width="400" height="301" class="size-medium wp-image-1337" srcset="/img/blog/2010/10/trend_ds2-400x301.png 400w, /img/blog/2010/10/trend_ds2.png 598w" sizes="(max-width: 400px) 100vw, 400px" /></a>
  
  <p class="wp-caption-text">
    DeSmuMEのトレンド
  </p>
</div>

　で、ニンテンドーDSエミュレーターというと数年前に触ったときはまだまだ完成度が低く、とても市販のゲームが動かせる状況ではなかったのだが、現在では完成度が上がり、結構色々と動作するらしい。ということで、とりあえず久しぶりに試して見ようと思ったら色々とはまったのでメモ代わりにご紹介。

<!--more-->

#### DeSmuMEほかの入手

　まずはDeSmuMEの入手法だが、[DeSmuMEのダウンロード][2]から入手できる。Windows/Mac OS X/Linux/ソースが公開されているので、適当なものをどうぞ。Windows版の場合、ZIPで圧縮されているだけなので適当に展開すればOKだ。

　続いて動かすアプリの入手。最近では完成度の高いHomebrew（非オフィシャルな開発ツールを使って有志が制作したソフトの総称。ほとんどが無料で公開されている）も増えてきており、とりあえず評価の高いペイントソフト「[Colors!][3]を試して見ることにした。

#### Colors!の設定

　Homebrewソフトは拡張子が「.nds」という形式のファイルで配布されており、通常はこれをDeSmuMEにドラッグ＆ドロップすればソフトを起動できるのだが、Colors!の場合はファイルI/Oに[DLDI][4]という仕組みを使用しており、先にこれの設定を行う必要がある。

　DLDIはDS用のストレージデバイス（マジコンなどと呼ばれているもの）用I/Oドライバのようなもので、使用するストレージデバイスに対応した「パッチ」を.ndsファイルに適用しておく必要がある。DeSmuMEの場合、「[GBA Movie Player (Compact Flash)][5]」を利用せよとのことなので、まずここからmpcf.dldiをダウンロードする。また、パッチを適用するためのツール「[Dlditool-win32-gui][6]」もダウンロードしておく。これはWindows用のGUIツールなので、ほかのOSを使っている場合は適当なものを選んでほしい。

　Dlditool-win32-guiを適当な場所に展開し、「dlditool32.exe」を実行すると「DLDI Patcher v0.32」というウィンドウが表示される。「DLDI File」で先ほどダウンロードしたmpcf.dldiが含まれるフォルダを選択し、「Binaries」でColors!に含まれる「HBMenu.nds」を指定する（ファイルのドラッグ＆ドロップでも指定可能）。最後に「Patch」ボタンをクリックすればパッチ完了となる。

<div id="attachment_1338" style="width: 410px" class="wp-caption aligncenter">
  <a href="/img/blog/2010/10/patch.png"><img src="/img/blog/2010/10/patch-400x371.png" alt="DLDI Patcherでパッチを適用" title="DLDI Patcherでパッチを適用" width="400" height="371" class="size-medium wp-image-1338" srcset="/img/blog/2010/10/patch-400x371.png 400w, /img/blog/2010/10/patch.png 402w" sizes="(max-width: 400px) 100vw, 400px" /></a>
  
  <p class="wp-caption-text">
    DLDI Patcherでパッチを適用
  </p>
</div>

#### ディスクイメージファイルを作る

　さて、本来ならあとはHBMenu.ndsファイルをDeSmuMEで開き、メニューから「colors.nds」を選択すればソフトが起動するはずなのだが、DeSmuMEの問題なのかそれともDLDIの問題なのか、Colors!を起動すると「ストレージに書き込めない」という旨のメッセージが出て操作できなくなってしまう。どうもWindows側のフォルダをそのままストレージとして利用するあたりが問題のようなので、ディスクイメージファイルを作成し、ファイル一式をそこに格納することで対処することにする。

　ディスクイメージの作成・操作だが、残念ながらWindowsで動作する適切なものは発見できなかった。しょうがないのでMac OS X上でディスクイメージを作成＆マウントし、そこでファイルをコピーしたあとでWindows機に転送する、という方法で対処する。

　Mac OS Xでは、「ディスクユーティリティ」を使用して簡単にディスクイメージを作成したり、マウントできる（Linuxでもルート権限があれば比較的容易に作業可能だが今回は割愛）。

<div id="attachment_1339" style="width: 410px" class="wp-caption aligncenter">
  <a href="/img/blog/2010/10/dsm_img.png"><img src="/img/blog/2010/10/dsm_img-400x346.png" alt="Mac OS Xのディスクユーティリティでディスクイメージ作成" title="Mac OS Xのディスクユーティリティでディスクイメージ作成" width="400" height="346" class="size-medium wp-image-1339" srcset="/img/blog/2010/10/dsm_img-400x346.png 400w, /img/blog/2010/10/dsm_img.png 750w" sizes="(max-width: 400px) 100vw, 400px" /></a>
  
  <p class="wp-caption-text">
    Mac OS Xのディスクユーティリティでディスクイメージ作成
  </p>
</div>

　「フォーマット」で「MS-DOS（FAT）」を、「パーティション」で「パーティションマップなし」を選択するのがポイント。容量はお好みでどうぞ。

　ディスクイメージを作成・マウントしたら、Colors!の配布アーカイブに含まれるファイル一式をそこにコピーし、アンマウントしてディスクイメージをWindows側にコピーすれば作業完了。

#### ディスクイメージを使用する設定

　あとはDeSmuMEを起動し、「エミュレーション」メニューの「GBAスロット」を選択して「GBAスロット」ウィンドウを開き、「Compact Flash」を選択して作成したイメージファイルを指定すればOK。

<div id="attachment_1340" style="width: 410px" class="wp-caption aligncenter">
  <a href="/img/blog/2010/10/dsm14.png"><img src="/img/blog/2010/10/dsm14-400x276.png" alt="「GBAスロット」でディスクイメージを指定" title="「GBAスロット」でディスクイメージを指定" width="400" height="276" class="size-medium wp-image-1340" srcset="/img/blog/2010/10/dsm14-400x276.png 400w, /img/blog/2010/10/dsm14.png 490w" sizes="(max-width: 400px) 100vw, 400px" /></a>
  
  <p class="wp-caption-text">
    「GBAスロット」でディスクイメージを指定
  </p>
</div>

　ただし、DeSmuME 0.9.6のWindows版の場合、ここで設定した値が反映されないというバグがあるので、ここでファイルを指定した後いったんDeSmuMEを終了し、DeSmuME.exeと同じディレクトリ内にある「desmume.ini」をテキストエディタで開いて次の個所を修正する必要がある。

<pre>[GBAslot.CFlash]
fileMode=<strong>1</strong>　　<span class="red">←「1」に設定</span>
path=C:\work\desmume\
filename=C:\work\desmume\test.dmg
</pre>

　以上でやっと全作業工程は完了。パッチを適用したHBmenu.ndsをDeSmuMEで開き、メニューから矢印キーで「Colors.nds」を選択してXキーを押せばColors!が起動する。

<div id="attachment_1341" style="width: 282px" class="wp-caption aligncenter">
  <a href="/img/blog/2010/10/dsm12.png"><img src="/img/blog/2010/10/dsm12.png" alt="HBMenuからColors!を起動する" title="HBMenuからColors!を起動する" width="272" height="491" class="size-full wp-image-1341" /></a>
  
  <p class="wp-caption-text">
    HBMenuからColors!を起動する
  </p>
</div>

<div id="attachment_1342" style="width: 282px" class="wp-caption aligncenter">
  <a href="/img/blog/2010/10/dsm13.png"><img src="/img/blog/2010/10/dsm13.png" alt="Colors!をDeSmuMEで実行" title="Colors!をDeSmuMEで実行" width="272" height="491" class="size-full wp-image-1342" /></a>
  
  <p class="wp-caption-text">
    Colors!をDeSmuMEで実行
  </p>
</div>

　ちなみに、実機で動かす場合は自動的にDLDIドライバが選択されるはずなので、パッチ作業は不要らしい（確認していないので本当かどうかは不明）。

 [1]: http://www.google.co.jp/trends?q=Desmume&#038;ctab=0&#038;geo=all&#038;date=ytd&#038;sort=0
 [2]: http://sourceforge.jp/projects/sfnet_desmume/
 [3]: http://colors.collectingsmiles.com/
 [4]: http://dldi.drunkencoders.com/index.php?title=Main_Page
 [5]: http://dldi.drunkencoders.com/index.php?title=GBA_Movie_Player_(Compact_Flash)
 [6]: http://dldi.drunkencoders.com/index.php?title=Win32_GUI