---
title: gitメモ：diffとやり直し
author: hylom
type: post
date: 2009-12-02T06:33:52+00:00
excerpt: 　最近久しぶりにgitを触って色々と忘れていたので再度メモ。
url: /2009/12/02/git_diff_rese/
categories:
  - Docs
tags:
  - git
  - programming

---
　最近久しぶりにgitを触って色々と忘れていたので再度メモ。

#### mergeを取り消す

　mergeを実行したらconflictが大量に出てしまったので取り消したい、という場合、下記を実行。

<pre class="command">$ git reset --hard ORIG_HEAD
</pre>

#### conflictを解決する

　gitにはmergeを実行した場合にconflictを解決するコマンド「git mergetool」がある。conflictしているファイルに対して、順番にdiffツールを実行して編集を促すもの。しかし、Windows上のMSysGit環境で実行したら見事にvimのdiffが実行されたので個人的にはデフォルトでは使えない認定（自分はvimはあまり使えないので）。

<pre class="command">$ git mergetool
</pre>

　.gitconfigの「merge」および「mergetool」項目で起動するツールを設定できるそうなので、今度はEmacsに設定してテストしてみようかな。

#### diffを使う

　[マニュアル][1]に書いてあるけど、「git diff」コマンドの書式は下記のとおり。

<pre>git diff &lt;比較元commit> &lt;比較先commit> [&lt;対象ファイルパス>]
</pre>

　ここで、比較元・比較先commitはハッシュだけでなく、「HEAD」（最新のコミット）や「HEAD^」（最新の1つ前のコミット）、「HEAD^^」（最新の2つ前のコミット）、「HEAD~4」（最新の4つ前のコミット）などのほか、tagも利用可能。

　例えば最新のコミットと、その1つ前のコミットでdiffを取るには次のようにする。

<pre class="command">$ git diff HEAD^ HEAD hogehoge.py
</pre>

 [1]: http://www.kernel.org/pub/software/scm/git/docs/git-diff.html
