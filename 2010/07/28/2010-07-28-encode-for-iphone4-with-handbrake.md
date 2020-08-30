---
title: iPhone 4およびiPad向け動画をHandBrakeで作る
author: hylom
type: post
date: 2010-07-28T13:34:04+00:00
url: /2010/07/28/encode-for-iphone4-with-handbrake/
category:
  - Docs
tags:
  - codec
  - Handbrake
  - ipad
  - iphone

---
　先日、私の手元にもiPhone 4が到着。ということで、一部から要望を受けていたHandBrakeのiPhone 4用プロファイルをちょっと調査・研究してみた。

　iPhone 4の動画再生機能については、Webサイトにその仕様が掲載されている（[日本語のiPhoneページ][1]）。ただし、日本語ページには一部誤訳というか不明瞭な表記があるたので、[英語版iPhoneページ][2]を確認するほうが確実。これによると、iPhone 4の動画再生仕様は下記の通り。

  * H.264：最大720p、30fps。Main Profile（レベル3.1まで、音声はAAC-LCで最大160kbs、48kHz、ステレオ）対応。ファイルフォーマットは.m4v、.mp4、.mov
  * MPEG-4：最大2.5Mbps、640×480ピクセル、30fps。Simple Profile（音声はAAC-LCでチャンネルあたり最大160kbps、48kHz、ステレオ）対応。ファイルフォーマットは.m4v、.mp4、.mov
  * MotionJPEG（M-JPEG）：最大35Mbps、1280×720ピクセル、30fps。音声はulawもしくはPCMステレオ。ファイルオーマットは.avi

　iPhone 4の画面サイズは960×640。そのため、縦に持った際は幅640に、横に持った際は幅960に自動的に拡大/縮小されて表示される。また、iPhone 4のドックコネクタ経由での出力では1024×768サイズの出力に対応している模様。

　ちなみに、iPhone 4の動画再生仕様はiPadとまったく同一のようだ。なお、iPadの画面サイズは1024×768である。

　さて、iPhone 4で動画を見る場合、わざわざ容量がかさむMPEG-4を積極的に使う必要はない。そのため、下記ではH.264についてのみ考察を行っていく。

　上記のとおり、iPhone 4はスペック上はHigh Profileには対応していない。しかし、試して見たところHandBrake 0.9.4のプリセットである「High Profile」でエンコードした動画も問題なく再生できてしまった。High ProfileとMain Profileの違いは8x8DCTブロックやカスタム量子化マトリックス（CQM）、Cb/Cr別のQP制御、モノクロ（4:0:0）対応だが、実際8x8DCT以外については、設定の難しさの割に効果は微妙なところではある（そのうえHandBrakeでは設定できない）。

　High Profile非対応という機器でも8x8DCT対応のものはあるので、iPhone 4/iPadもそうなのだろう。HandBrakeでは「High Profile向け」と表示される「Pyramidal B-Frames」については、High ProfileでもOffになっているので気にしないことにする。

　ということで、とりあえずHandBrakeでiPhone 4およびiPad向けのエンコードを行う場合、プリセットのHigh Profile設定を利用すれば問題ないようだ。

　対応する縦横サイズやビットレートに関連する「レベル」については次の機会に。

 [1]: http://www.apple.com/jp/iphone/specs.html
 [2]: http://www.apple.com/iphone/specs.html
