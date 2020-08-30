---
title: gitメモ：ブランチを切ってないのにやばいコードを書いちゃった場合
author: hylom
type: post
date: 2010-07-30T00:32:22+00:00
url: /2010/07/30/git-branch-with-stash/
category:
  - Docs
tag:
  - git
  - programming

---
　gitを使ってコードの管理をしている場合において、実験的なコードを書く場合はソースコードを編集する前にブランチを作成しておくのが基本だ。しかし、ついブランチを作成し忘れたままでコードを変更してしまった、というパターンがある。

　この場合、下記のようにgit stashでいったん変更点を保存した上で直前のcommitに戻し、新たなブランチを作成してそこでgit stash applyを行えばよい。

<pre>$ git stash
$ git checkout hogehoge -b
$ git stash apply
$ git add hogehoge foobar
$ git commit
</pre>

　git stash、便利だ。
