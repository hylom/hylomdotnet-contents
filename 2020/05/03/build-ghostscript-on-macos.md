---
slug: build-ghostscript-on-macos
title: macOSでGhostscriptをビルドする
tag: [ macos, oss ]
date: 2020-05-03T22:52:54+09:00
lastmod: 2020-05-03T22:54:32+09:00
publishDate: 2020-05-03T22:52:54+09:00
---

　PostScriptやPDFを扱う際にほぼ必ず出てくるGhostscriptですが、[公式サイト](https://www.ghostscript.com/)にはmacOS向けのバイナリが見当たりません。ということで、自前でビルドする手順 のメモです。

　なお、GhostscriptのmacOS向けバイナリとしては[Richard Koch氏によって配布されているもの](https://pages.uoregon.edu/koch/)もあるのですが、最新版はHigh Sierra以降向けでSierra環境では利用できません。また、brewコマンドでもインストールできますが、個人的にbrewコマンドをあまり使いたくない、という理由で自前でビルドしています。

　Ghostscriptのソースコードは、公式サイトの[ダウンロードページ](https://www.ghostscript.com/download/gsdnld.html)から入手できます。ダウンロード後、適当なディレクトリに展開しておきます。

#### 必要な依存ライブラリ



ビルドには以下のライブラリが必要です。

 - libpng（[http://www.libpng.org/pub/png/libpng.html](http://www.libpng.org/pub/png/libpng.html)）
 - littleCMS（lcms、[http://www.littlecms.com/download.html](http://www.littlecms.com/download.html)）
 - jbig2dec（[https://jbig2dec.com](https://jbig2dec.com)）
 - libjpeg（[http://www.ijg.org](http://www.ijg.org)）
 - freetype（[https://www.freetype.org/download.html](https://www.freetype.org/download.html)）

　このうち、libpng、lcms、jbig2decはダウンロードしたアーカイブを展開して./configure;make;make installというおなじみの手段でビルド＆インストールが行えます（一部はfreetypeとlibjpegのようにソースツリー内に展開するだけで一緒にビルドできるようなのですが未確認）。

　freetypeとlibjpegについては、アーカイブをGhostscriptのソースコードを展開したディレクトリ（ソースツリーのトップディレクトリ）に展開し、そのディレクトリ名を「freetype」および「jpeg」に変更しておくことで自動的にビルドされます。

　また、gxpsのビルドにはJPEG XRのサポートが必要なようなので今回は無効にしました。ということでGhostscript自体のconfigureオプションは次のようになります。

```
$ ./configure --without-xps
```

　あとはmakeコマンドを実行するとgsコマンドがビルドされ、「make install」で/usr/local/bin以下にgsコマンドがインストールされます。

　また、libgsが必要な場合、「make so」コマンドを実行するとバイナリがビルドされ、「make soinstall」でそれらをインストールできます（詳しくはbase/unix-dll.makを参照）。

