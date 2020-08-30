---
slug: emacs-magit-git-path
title: Emacsのmagitで使用するgitバイナリのパスを指定する方法
tag: [ emacs, git ]
date: 2020-07-20T19:28:04+09:00
lastmod: 2020-07-20T19:30:29+09:00
publishDate: 2020-07-20T19:28:04+09:00
---

　Xcodeと一緒にインストールしたgitコマンドをEmacsのmagitで使用すると、magitの各種処理がとても遅くなることは皆様ご存知かと思います。また、Xcodeを入れていない環境でmagitを使うと毎回Xcodeをインストールするか確認するダイアログが表示され非常に煩わしかったりします。

　この事象について背景を簡単に説明すると、最近のMacOS環境には/usr/bin/gitがデフォルトで存在するのですが、Xcodeをインストールしていない場合このファイルはただのstubで、実行するとXcodeのインストールを求めるダイアログを表示するという挙動になっています。また、Xcodeをインストールして、Xcode経由でgitをインストールすると、このgitが本物のgitのバイナリに差し替えられるのですが、このgitコマンドはAppleによってカスタマイズされているようで、起動が遅いという問題があります（多分EULAへの同意チェックとかそういうのが入っているっぽい）。そのため普段使いには/usr/local/bin以下に別途gitをインストールして使っている人も多いと思うのですが、magitはデフォルトでまず/usr/bin以下のgitを使う設定になっているので、その場合/usr/local/bin以下のgitが使われません。

　ということで、magitで/usr/local/bin以下のgitを使うようにするには、customize（M-x customize）でCustomize機能を呼び出し、「Exec Path」で検索→Exec Pathに/usr/local/binを追加、という手順で設定する必要があります。

　なお、「Magit Git Exectable」というcustomize項目もあるのですが、こちらを指定してもmagitではまずExec Pathで指定されたパスにgitコマンドを探しに行く模様です。そのため、Xcodeをインストールしていない環境で/usr/local/bin以下にgitをインストールし、Magit Git Executableで「/usr/local/bin/git」を指定した場合、gitに関連する操作をするたびにXcodeのインストールを求めるダイアログが表示される（そしてインストールせずにダイアログを消すと処理が正しく完了する）という面倒な感じになるのでご注意ください。

