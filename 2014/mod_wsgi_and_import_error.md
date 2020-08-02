---
slug: mod_wsgi_and_import_error
title: mod_wsgiでeasy_installとかでインストールしたPythonモジュールを読み込めない場合の対処
tags: [ selinux,python,apache ]
date: 2014-12-18T23:37:53+09:00
lastmod: 2014-12-18T23:43:12+09:00
publishDate: 2014-12-18T23:37:53+09:00
---

<P>
　WSGIを使ってWebアプリケーションを実装して、Apache＋mod_wsgi環境で実行しようとした場合に、特定のモジュールがインポートできないという問題が発生することがある。具体的には、SELinuxが有効な状態で、easy_installなどでインストールしたPythonモジュールをインポートできないというものだ。この場合、以下のようにしてPythonのsite-packagesディレクトリのラベルを修正することで対応できる。
</P>
<pre class="shell bash">
# restorecon -FRv /usr/lib/python2.7/site-packages/
</pre>

