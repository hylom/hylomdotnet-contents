---
title: Mac OS X上でのEmacs 24設定（主にoptionキー周り）
author: hylom
type: post
date: 2012-08-08T14:02:42+00:00
url: /2012/08/08/emacs-24-on-mac-os-x/
category:
  - Hacks
tag:
  - emacs
  - macosx

---
　Mac OS XでATOKを使っていると、通常「¥」キーでは¥が入力される。しかし、Mac OS X（というかUTF-8）では¥と\は違う物として扱われる。そのため、色々と面倒くさいことが発生する。ことえりでは「¥」キーで\を入力する設定があるのだが、ATOKにはない。キーマップを書き換えて対応する、という方法もあるのだが、そういった方法は個人的に嫌いなので、Emacs側の設定で何とかすることにする。

　設定は以下の3点。

<pre>(setq mac-option-modifier nil)
(setq mac-command-modifier 'meta)
(global-set-key (kbd "C-M-¥") 'indent-region)
</pre>

1行目でoptionキーをoptionキーとして認識させ、2行目でcommandキーをmetaキーとして認識させる。最後に、なぜかcontrol＋command＋option＋¥がC-M-\として認識されないので、代わりにC-M-¥にindent-regionを割り当てる。

とりあえず、これでしばらくはしのげるかなと。
