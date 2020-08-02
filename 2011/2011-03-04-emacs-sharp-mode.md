---
title: 'EmacsでC#（csharp-mode）を使う'
author: hylom
type: post
date: 2011-03-04T09:31:48+00:00
url: /2011/03/04/emacs-sharp-mode/
categories:
  - Docs
tags:
  - csharp
  - emacs

---
　EmacsでC#コードをいじりたかったのでcsharp-modeを導入した。

　csharp-modeは[Google Codeのcsharpmodeプロジェクト][1]から入手可能。

　とりあえず現時点での最新版「csharp-mode-0.7.6.el」をダウンロードし、csharp-mode.elにリネームして~/.emacs.d/lisp/以下にコピーし、.emacs.elに下記を追加した。

<pre>;; C# mode
(require 'csharp-mode)
(setq auto-mode-alist
      (append '(("\\.cs$" . csharp-mode)) auto-mode-alist))
</pre>

　ちなみに私の場合、.emacs.el中で下記のように~/.emacs.d/lispをロードパスに追加しているが、そうでない場合はsite-lispディレクトリなどロードパスに含まれている場所にcsharp-mode.elを置く必要がある。

<pre>;; add ~/.emacs.d/lisp to load-path
(add-to-list 'load-path "~/.emacs.d/lisp")
</pre>

　最後にEmacs上でM-x byte-compile-fileを実行してcsharp-mode.elを指定してバイトコンパイルして完了。これでC#のコードが色付き（ハイライト）で表示されるようになる。

 [1]: http://code.google.com/p/csharpmode/
