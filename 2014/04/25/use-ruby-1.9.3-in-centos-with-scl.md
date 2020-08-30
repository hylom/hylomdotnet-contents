---
slug: use-ruby-1.9.3-in-centos-with-scl
title: CentOSでRuby 1.9.3やPython 2.7、Python 3.3などを使う簡単な方法
tag: [ centos, linux ]
date: 2014-04-25T20:29:43+09:00
lastmod: 2014-04-28T18:58:36+09:00
publishDate: 2014-04-25T20:29:43+09:00
---

<p>　昨年、『<A href="http://sourceforge.jp/magazine/13/09/13/151500">米Red Hat、RHELの開発環境をアップデートする「Developer Toolset 2.0」および「Software Collections 1.0」をリリース</a>』という話題がありました。</p>

<p>　Red Hat Enterprise Linux（RHEL）は安定性を重視し、かつ長期にわたって利用されることを想定しているため、ディストリビューションに含まれているソフトウェアは比較的古めのものになっています。そのため、RHELに標準で含まれていない最新のソフトウェアを利用したい場合、自分でソースコードからビルドするか、サードパーティのリポジトリを利用する必要がありました。</p>

<p>　この「Software Collections」（以下SCL）は、そういった背景の下、RHELに含まれていないソフトウェア、もしくはRHELに含まれているものよりもバージョンが新しいソフトウェアを提供するもので、たとえば以下のようなソフトウェアが提供されます。</p>

<pre class="list">
Ruby 1.9.3 (ruby193)
Python 2.7 (python27)
Python 3.3 (python33)
PHP 5.4 (php54)
Perl 5.16.3 (perl516)
Node.js 0.10 (nodejs010)
MariaDB 5.5 (mariadb55)
MySQL 5.5 (mysql55)
PostgreSQL 9.2 (postgresql92)
</pre>

<p>　特にRubyにおいては、近年RHELに収録されているRuby 1.8.7をサポートしないライブラリやソフトウェアが増えてきたため、Ruby1.9.3が簡単に導入できるのは便利なところです。</p>

<p>　そして、CentOSがRed Hatの正式プロジェクトとなった影響なのか、このSCLもCentOSで利用できるようになりました（<a href="http://lists.centos.org/pipermail/centos-announce/2014-February/020164.html">CentOS-announceメーリングリストに流れたアナウンスメール</a>）。</p>

<p>　導入方法は非常に簡単で、「centos-release-SCL」パッケージをインストールするだけです（<a href="http://wiki.centos.org/AdditionalResources/Repositories/SCL">ドキュメント</a>）。ただし、利用できるのはx86_64のみとなっています。</p>

<pre class="shell">
# yum install centos-release-SCL
</pre>

<p>　centos-release-SCLパッケージのインストール後は、yumコマンドでそれぞれのパッケージをインストールできるようになります。たとえばruby 1.9.3をインストールするには、以下のようにします。</p>

<pre class="shell">
# yum install ruby193
</pre>

<p>　ただし、SCLに含まれるソフトウェアは、そのままでは実行できません（ruby193というパッケージをインストールしても、ruby193というコマンドが利用できるようになるわけではない）。実行する二は、sclコマンドを利用する必要があります。sclコマンドは、引数で指定したパッケージを有効にした状態で指定したコマンドを実行するものです。たとえば、以下のようにするとRuby 1.9.3を有効にした環境で「ruby -v」コマンドを実行できます。</p>

<pre class="shell">
$ scl enable ruby193 'ruby -v'
ruby 1.9.3p448 (2013-06-27) [x86_64-linux]
</pre>

<p>　また、次のように引数にシェルを指定すれば、指定したパッケージが有効になったシェル環境を起動できます。</p>

<pre class="shell">
$ scl enable ruby193 bash
$ ruby -v
ruby 1.9.3p448 (2013-06-27) [x86_64-linux]
$ exit
</pre>

<p>　ちなみに、この環境でRubyGemをインストールしたい場合はroot権限でsclコマンドを実行してからgemコマンドでインストールする必要があります。</p>

<pre class="shell">
# scl enable ruby193 bash
# gem install ＜インストールしたいパッケージ＞
</pre>

<p>　そのほかの使い方などは<a href="https://access.redhat.com/site/documentation/en-US/Red_Hat_Software_Collections/1/html-single/1.0_Release_Notes/index.html#sect-Installation_and_Usage-Use">ドキュメント</a>をご参照ください。</p>

