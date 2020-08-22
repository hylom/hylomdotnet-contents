---
slug: use-mojolicious-with-centos7
title: CentOS 7でMojoliciousを使う
tags: [ perl ]
date: 2017-03-09T19:58:29+09:00
lastmod: 2017-03-09T19:58:38+09:00
publishDate: 2017-03-09T19:58:29+09:00
---

　最近PerlのWebアプリケーションフレームワークMojoliciousをずっと触っているのだが、CentOS 7の標準リポジトリやEPELではパッケージが提供されていないため、別の方法でインストールする必要がある。まあPerlモジュールなのでCPANを使うのが一般的なのだが、一般的なCentOS 7環境だと依存ライブラリが不足していてインストールに失敗する模様。たとえば次のように実行すると、テスト段階でエラーが出る。

```
# yum install cpan
# cpan -i Mojolicious
```

　ということで依存しているモジュールを調べたのだが、とりあえず以下のように2つのパッケージをインストールすれば解決するようだ。

```
# yum install perl-Digest-MD5 perl-IO-Compress.noarch
# cpan -i Mojolicious
```

