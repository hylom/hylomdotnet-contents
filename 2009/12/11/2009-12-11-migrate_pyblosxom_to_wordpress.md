---
title: pyblosxom用のブログ記事をWordPressにインポートする
author: hylom
type: post
date: 2009-12-10T15:54:45+00:00
excerpt: '<p>　以前このブログはPythonで書かれたブログシステム「<a href="http://pyblosxom.sourceforge.net/">pyblosxom</a>」を使って運用していたんだけど、機能拡張が面倒臭かった（＆色々細かいところが気にくわなかった）ので先日WordPressに移行しました。そこで面倒だったのが記事の移行。WordPressではMovableTypeとかBloggerとかからの移行ツールは充実しているんだけど、pyblosxomからの移行ツールは公式には用意されていません。また、参考情報としてWordPressの公式サイトで紹介されていた<a href="http://blog.unto.net/meta/migrating-from-blosxom-to-wordpress/">blosxomからの移行スクリプト</a>はURLやタグ情報を移行してくれなかったため、結局自前で変換スクリプトを用意することに。</p>'
url: /2009/12/11/migrate_pyblosxom_to_wordpress/
category:
  - Docs
tag:
  - pybloxsom
  - python
  - wordpress

---
　以前このブログはPythonで書かれたブログシステム「[pyblosxom][1]」を使って運用していたんだけど、機能拡張が面倒臭かった（＆色々細かいところが気にくわなかった）ので先日WordPressに移行しました。そこで面倒だったのが記事の移行。WordPressではMovableTypeとかBloggerとかからの移行ツールは充実しているんだけど、pyblosxomからの移行ツールは公式には用意されていません。また、参考情報としてWordPressの公式サイトで紹介されていた[blosxomからの移行スクリプト][2]はURLやタグ情報を移行してくれなかったため、結局自前で変換スクリプトを用意することに。

　幸い、WordPressのインポート/エクスポートで使われるWXL（WordPress XML）形式のファイルを簡単に生成できるモジュールをGoogle様が提供しているのを発見、そいつを使ってお気楽に作成できました。ということでここでご紹介。

　スクリプト本体は[github][3]で公開しているので必要な方は適宜どうぞ。「pyblosxom2wp.py」が本体です。このスクリプト内の頭で宣言している変数「title」にブログのタイトル、「link」にブログのリンクURL、「baseurl」をにBase URLが入るように書き換えて、次のように実行すると標準出力経由でインポート用XMLファイルが出力されます。

<pre>./pyblosxom2wp.py ＜pyblosxomの記事ディレクトリ＞ &gt; output.xml</pre>

あとはそいつをWordPressのインポート機能で読みこめばOK、のはず。これで、カテゴリやタグ、URLについてもできるだけ保持する形でインポートが可能です。

 [1]: http://pyblosxom.sourceforge.net/
 [2]: http://blog.unto.net/meta/migrating-from-blosxom-to-wordpress/
 [3]: http://github.com/hylom/pyblosxom2wp
