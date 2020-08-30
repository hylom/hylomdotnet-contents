---
title: Maildirでの日本語フォルダの扱い（procmailで日本語フォルダへ振り分ける）
author: hylom
type: post
date: 2011-03-03T09:43:01+00:00
url: /2011/03/03/maildir-with-japanese-folder-name/
category:
  - Docs
tag:
  - japanese
  - mail
  - maildir
  - procmail

---
　最近procmailでメールの振り分けをしているのだが、日本語のフォルダへの振り分けってどうするの？　と悩んだので調べた。

　命名規則自体は[RFC2060][1]に記載されているとおり、UTF-7の修正版が用いられている（[UTF-7についてはIT用語辞典を参照のこと][2]）。

　Maildir以下のサブフォルダはこの規則に従って作成されるので、目的となる日本語フォルダ名を修正版UTF-7（IMAP-UTF7などとも呼ばれる）に変換し、それを振り分け先として指定すれば良い。

　IMAP-UTF7への変換は[文字コード変換ツール][3]があるので、こちらを使えばお手軽。たとえば「登録関係」というフォルダなら、「.&#038;dnuTMpWiT8I-」というフォルダ名となる。

 [1]: http://www.lins.jp/~obata/imap/rfc/rfc2060ja.html#s5.1
 [2]: http://www.sophia-it.com/content/UTF-7
 [3]: http://e-zackie.com/tool/code_convert.php
