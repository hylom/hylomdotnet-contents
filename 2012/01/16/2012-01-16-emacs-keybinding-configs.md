---
title: Emacsのキーバインディング設定
author: hylom
type: post
date: 2012-01-16T11:06:30+00:00
url: /2012/01/16/emacs-keybinding-configs/
category:
  - 未分類

---
　Emacsの設定ファイル（.emacsなど）でキーバインディングを設定する場合の作法はググると色々なものが出てくるのだが、最近では[kbd関数][1]を利用するのが一般的なようだ。コントロールキー同時押しや特殊キーに関数を割り当てる場合、一昔前は分かりにくい表記で書いていたが、kbd関数を使うと割と簡潔にキーを指定できる。

　たとえばCtrl＋Shift＋Insertというキーに「add-anchor」関数を割り当てる場合は下記のようにする。

<pre>(global-set-key (kbd "C-S-&lt;insert&gt;") 'add-anchor)
</pre>

　あと、global-set-key関数を使う以外に、define-key関数を「global-map」引数付きを使う人もいるようだが、こちらについてはどちらも意味的には同じ。たとえば上記の例をdefine-keyを使って書くと、次のようになる。

<pre>(define-keyglobal-map (kbd "C-S-&lt;insert&gt;") 'add-anchor)
</pre>

　「global-map」の代わりに「current-global-map」を使っても、基本的には同じ。Emacsのマニュアル中、キーマップ周りは「[Commands for Binding Keys][2]」にあるのでこちらもご参照を。

 [1]: http://www.gnu.org/software/emacs/manual/html_node/elisp/Key-Sequences.html
 [2]: http://www.gnu.org/software/emacs/manual/html_node/elisp/Key-Binding-Commands.html
