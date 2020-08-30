---
title: WordPress導入
author: hylom
type: post
date: 2009-10-21T17:31:12+00:00
url: /2009/10/22/wordpress導入/
category:
  - Docs
tags:
  - pyblosxom
  - wordpress

---
　ブログシステムをpyblosxom＋自前のバックエンドから、[WordPress][1]に変更してみた。WordPressはデフォルトではMySQLをデータベースとして使うけど、今回はプラグインを入れてsqliteを使う構成でセットアップ。

　sqliteを入れたのは、ファイルのコピーだけでなにも考えずにバックアップができるというのと、パフォーマンス的に有利なんじゃないかなー、という理由。テキストデータしか入れる気はないので、データベースサイズはせいぜい数MBだし、ファイルキャッシュが効けば結構速くなるんじゃないの？ とか考えてるんだけど、実際どうなってるかはちゃんと測ってないので不明。

　ちなみに、WordPressをsqliteを使うプラグインは[これ（PDO (SQLite) For WordPress）][2]。基本的には付属ドキュメント通りにセットアップすればOK（WordPressのwp-contentディレクトリ以下に配布ファイルをコピー→wp-config.phpファイルに「define(&#8216;DB_TYPE&#8217;, &#8216;sqlite&#8217;);」を追加）。Web上の情報では、ソースをいじったりする必要があるという話が書いてあるものもあったけど、自分が試したバージョン（WordPress 2.8.4＋PDO For WordPress 2.6.1）では設定ファイル以外のソースの変更は不要だった。

　ただ、suexecを使っていない環境ではもちろんデータベースディレクトリおよびデータベースファイルを作成できるようにパーミッションを変更しておく必要がある。データベースファイルはwp-contentディレクトリ以下に「database」というディレクトリが作成され、その中に作成されるので、一時的にwp-content内にWebサーバーを動かしているユーザー権限でディレクトリを作成できるように設定しておく必要あり。

#### pyblosxomの記事のインポート

　でもって、過去のpyblosxomの記事のインポートなんだけど、直接はインポートできないので、過去の記事からインポート用のファイルを作成する必要がある。WordPressの「[Importing Content][3]」ページでは[変換用スクリプトを用意してインポートする方法を紹介するページ][4]が紹介されているんだが、このスクリプトは日本語環境だと微妙な気がしたので、これを参考にPythonで書き直してみた。

　ただしこの変換スクリプト、カテゴリと記事コンテンツ、投稿日はインポートできるのだがタグとエントリのURL情報は無視してくれるのが困りどころ。おかげで過去記事のリンクが切れる……。カテゴリについては、.htaccessに次の1行を追加すれば解決なのだが、リンク切れはさぁどうしようかねぇ。

<pre>RewriteEngine On
RewriteBase /
RewriteRule ^(apple|bluegriffon|develop|fsm|handbrake|s|slashdot|twitter) category/$1 [R=301,L]

# BEGIN WordPress
　：
　：</pre>

 [1]: http://ja.wordpress.org/
 [2]: http://wordpress.org/extend/plugins/pdo-for-wordpress/
 [3]: http://codex.wordpress.org/Importing_Content
 [4]: http://blog.unto.net/meta/migrating-from-blosxom-to-wordpress/
