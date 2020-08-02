---
slug: emacs-25.1-ime-flicker-problem
title: Mac OS X向けEmacs 25.1で日本語入力時にちらつく問題の原因
tags: [ emacs ]
date: 2017-04-17T00:26:43+09:00
lastmod: 2017-05-21T01:27:49+09:00
publishDate: 2017-04-17T00:26:43+09:00
---

　[Emacs for Mac OS X](https://emacsformacosx.com)で配布されているEmacsのMac OS X向けビルドでは、Emacs 24.4移行は標準でインラインでの日本語変換が可能になっている。これはEmacs 25.1でも同じだが、日本語入力時にカーソルがちらつく（1文字入力したり、変換するたびにカーソルが変換位置の先頭に一瞬移動してその後変換位置の最後に移動する）という現象が発生する。この問題はEmacs 24.5では発生していなかったので、24.5から25.1の間のどこかで混入したと思われる。そこで、EmacsのGitリポジトリをたどってこの問題がどこで発生するようになったのかを検証してみた。

　結論から言うと、[9e77c1b7bcfd0807be7fe67daf73c2320e864309](http://git.savannah.gnu.org/cgit/emacs.git/commit/?h=emacs-25.1&id=9e77c1b7bcfd0807be7fe67daf73c2320e864309)のコミットで問題が発生するようになっている。

　また、その1つ前の[ec10ba2792eef613caf47fff83e869d4bc177616](http://git.savannah.gnu.org/cgit/emacs.git/commit/?h=emacs-25.1&id=ec10ba2792eef613caf47fff83e869d4bc177616)のコミットでは問題は確認できなかった。

　問題のコミットで変更されているのはsrc/keyboard.cだったのがちょっと意外。てっきりMac OS X向けのコードであるns*.mあたりが原因だと思っていたのだが。おおむね問題の発生理由は想像できたのだが修正コードはもう少し周囲をチェックする必要があるのでまた今度。

　ちなみにこのコミットを見つけるために行った作業の流れだが、基本的にはいわゆる2分探索である。gitにはこの作業を自動で行うgit bisectコマンドがあるのだが、コンパイルしたバイナリに問題があるかどうかを自動で判別する手段がなかったのでビルド後にバイナリを実行して目視で問題が存在しているかをチェックしなければならなかったのが大変だった。

　（追記＠5/21）パッチを作成して[公開した](https://osdn.net/projects/macemacsjp/releases/p15426)。また、このパッチを利用せずとも（少なくともバージョン25.1および25.2では）この問題は以下のようにredisplay-dont-pause変数をnilに設定することで解決できることも発見した。

```
(setq redisplay-dont-pause nil)
```

　ただし、この変数はバージョン24.5でobsoleteとなっているので今後も利用できるかは分からない。また、[Emacsのバグトラッカーに問題が報告されていた](https://debbugs.gnu.org/cgi/bugreport.cgi?bug=23412)のでこれにコメントを入れておいた。


