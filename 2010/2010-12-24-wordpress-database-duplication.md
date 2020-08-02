---
title: WordPressのデータベースをコピー/移行する
author: hylom
type: post
date: -001-11-30T00:00:00+00:00
draft: true
url: /?p=1367
categories:
  - 未分類

---
　WordPressで運営していたブログを別のサーバーに移行する手順メモ。ローカルに検証環境を作成する場合などにも使えます。

　まず、ブログを運営しているマシン（もしくはデータベースを動かしているマシン）でデータベースのバックアップを取得する。

<pre>$ mysqldump -u ＜ユーザー名＞ ＜データベース名＞ -h ＜データベースサーバー名＞ -p | gzip > backup.sql.gz
</pre>

　取得したバックアップを移行先マシンにコピーし、データベースに投入する。このとき、バックアップ元のデータベースとは異なるユーザー名やデータベース名にすることも可能。

<pre>$ gunzip -c backup.sql.gz | mysql -u ＜ユーザー名＞ ＜データベース名＞ -p
</pre>

　以上でデータベースのコピーは完了なのだが、WordPressを別ドメインで動かす場合、このままではWordPressのサイトURLなどが不適当になるため、WordPressの管理インターフェイスにアクセスできない。そこで、mysqlを直接叩いて設定を変更する。

<pre>$ mysql -u ＜ユーザー名＞ ＜データベース名＞ -p
</pre>

まず、変更すべきポイントは「wp_options」テーブルの「siteurl」項目。ここに、サイトのURLが格納されている。

<pre>mysql> select option_name, option_value from wp_options where option_name = "siteurl";
+-------------+---------------------+
| option_name | option_value        |
+-------------+---------------------+
| siteurl     | http://hylom.net/wp | 
+-------------+---------------------+
1 row in set (0.00 sec)
</pre>

　これを下記のようにして変更する。

<pre>mysql> update wp_options set option_value = "http://＜新しいサイトのURL＞" where option_name = "siteurl";
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
</pre>

　変更後、一応確認。

<pre>mysql> select option_name, option_value from wp_options where option_name = "siteurl";+-------------+----------------------+
| option_name | option_value         |
+-------------+----------------------+
| siteurl     | http://**.***.178.78 | 
+-------------+----------------------+
1 row in set (0.00 sec)
</pre>

　以上の作業が完了すると、「http://＜変更後のURL＞/wp-admin/」でWordPressの管理インターフェイスにアクセスできるようになるはず。ログインして設定を確認しましょう。