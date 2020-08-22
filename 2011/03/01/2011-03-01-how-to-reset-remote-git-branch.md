---
title: Gitでブランチを間違えて作業した上にpushまでしちゃった場合の対処方法
author: hylom
type: post
date: 2011-03-01T11:01:39+00:00
url: /2011/03/01/how-to-reset-remote-git-branch/
categories:
  - Docs
tags:
  - development
  - git
  - programming

---
　時間ができたのでHandBrake 0.9.5の日本語化に着手しているのだが、うっかり0.9.4のブランチで作業してしまったあげく、SourceForge.JP上のリポジトリにpushしてしまい途方に暮れる。

　まあこういうミスをやる人は少ないだろうが、何かのヒントになるかもしれないので対処法をメモしておく。まず、「git log」コマンドで巻き戻したいcommitのハッシュを調べる。

<pre>$ git log
　：
　：
commit 1485a5a2bbbb43eedbe131c919b7d604bcbd506d
Author: unknown &lt;hirom@.(none)>
Date:   Tue Jan 5 19:19:44 2010 +0900

    update Installer, changelog, readme
</pre>

　今回は、この「1485a5a2bbbb43eedbe131c919b7d604bcbd506d」というcommitまで巻き戻すことにする。作業中のブランチが操作したいものであることを確認したうえで、「git reset ＜対象のハッシュ＞」を実行する。

<pre>$ git branch -a
  jp-0.9.3
* jp-0.9.4
  master
  original
  remotes/origin/HEAD -> origin/master
  remotes/origin/jp-0.9.3
  remotes/origin/jp-0.9.4
  remotes/origin/master
  remotes/origin/original

$ git reset 1485a5
Unstaged changes after reset:
M       Jamrules
M       Makefile
M       win/C#/Installer/Installer.nsi
M       win/C#/InstallerJp/doc/AUTHORS
M       win/C#/InstallerJp/doc/CREDITS
M       win/C#/InstallerJp/doc/NEWS
M       win/C#/Properties/AssemblyInfo.cs
M       win/C#/frmAbout.Designer.cs
</pre>

　「git log」で巻戻ったことを確認する。

<pre>$ git log
commit 1485a5a2bbbb43eedbe131c919b7d604bcbd506d
Author: unknown &lt;hirom@.(none)>
Date:   Tue Jan 5 19:19:44 2010 +0900

    update Installer, changelog, readme
</pre>

　バージョン管理されているファイル自体は巻き戻されていないので、「-f」オプション付きでチェックアウトしてファイルも巻き戻す。

<pre>$ git checkout -f
</pre>

　ここまでの作業でローカルブランチの巻き戻しは完了。続いてリモートブランチの巻き戻しを行う。ただし、当然ながらそのままpushすることはできない。

<pre>$ git push
Enter passphrase for key '/d/Users/hirom/.ssh/id_dsa':
To hylom@git.sourceforge.jp:/gitroot/handbrake-jp/handbrake-jp.git
 ! [rejected]        jp-0.9.4 -> jp-0.9.4 (non-fast-forward)
error: failed to push some refs to 'hylom@git.sourceforge.jp:/gitroot/handbrake-
jp/handbrake-jp.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again.  See the
'Note about fast-forwards' section of 'git push --help' for details.
</pre>

　そこで、いったんリモートブランチを削除した上で再度pushする。まずは削除。リモートブランチの削除は、「git push ＜リモートリポジトリ＞ :＜対象リモートブランチ＞」で行える。

<pre>$ git push origin :jp-0.9.4
Enter passphrase for key '/d/Users/hirom/.ssh/id_dsa':
To hylom@git.sourceforge.jp:/gitroot/handbrake-jp/handbrake-jp.git
 - [deleted]         jp-0.9.4
</pre>

　あとは再度ローカルリポジトリをpushするだけ。

<pre>$ git push origin jp-0.9.4:jp-0.9.4
Enter passphrase for key '/d/Users/hirom/.ssh/id_dsa':
Counting objects: 233, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (146/146), done.
Writing objects: 100% (165/165), 30.48 KiB, done.
Total 165 (delta 119), reused 0 (delta 0)
To hylom@git.sourceforge.jp:/gitroot/handbrake-jp/handbrake-jp.git
 * [new branch]      jp-0.9.4 -> jp-0.9.4
</pre>

　お粗末様でした。
