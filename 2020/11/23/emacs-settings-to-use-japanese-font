---
slug: emacs-settings-to-use-japanese-font
title: macOSの最近のEmacsで日本語フォントがいわゆる中華フォントになる問題の解決方法
tag: [ emacs, macos ]
date: 2020-11-23T21:00:00+09:00
lastmod: 2020-11-23T21:00:00+09:00
publishDate: 2020-11-23T21:00:00+09:00
---


Emacsをアップデートしたところ、日本語（というか漢字）がいわゆる「中華フォント」になってしまった。中華フォントといっても繁体字なので問題なく読めるのだが、たとえば「化」の3画目が4画目に対して突き抜ける感じになったりするので、文章を書くときに気が乗らない。解決方法を試行錯誤したところ、これは`set-language-environment`を`"Japanese"`に設定するだけで簡単に解決した。

```
(set-language-environment "Japanese")
```

あとついでにフォント設定も微調整。

```
(create-fontset-from-ascii-font "menlo-14" nil "menlo14")
(set-fontset-font "fontset-menlo14" 'unicode "menlo-14" nil 'append)
(add-to-list 'default-frame-alist '(font . "fontset-menlo14"))
```

あと、Emacs 27.1ではいつの間にか日本語変換時のちらつき問題も解決していた。素晴らしい。
