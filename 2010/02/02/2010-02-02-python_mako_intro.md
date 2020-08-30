---
title: Mako Templaters for Pythonメモ1：Makoってなに？
author: hylom
type: post
date: 2010-02-02T06:32:06+00:00
url: /2010/02/02/python_mako_intro/
category:
  - Docs
tag:
  - mako
  - programming
  - python
  - template

---
　最近Pythonのテンプレートエンジン「[Mako][1]」を触ってるんだけど、日本語の情報が全然ないのでまとめてみる。

<div style="width: 460px" class="wp-caption aligncenter">
  <a href="http://www.makotemplates.org/"><img alt="Mako公式Webサイト" src="/img/blog/100202/mako_web.png" title="Mako公式Webサイト" width="450" height="261" /></a>
  
  <p class="wp-caption-text">
    Mako公式Webサイト
  </p>
</div>

<!--more-->

　Makoは「Hyperfast and lightweight templating for the Python platform.」（Pythonプラットフォーム向けの超高速で軽量なテンプレートエンジン）だ。Pythonのテンプレートエンジンとしては、Python標準ライブラリに含まれている[string.Template][2]や、Webフレームワークの[Django][3]に組み込まれている[Djangoテンプレートエンジン][4]、そして[Cheetah][5]などが知られているが、Makoはそれらよりも高速で、テンプレート内にPythonコードを埋め込む機能や、キャッシュ機構などを備えてるのが特徴だ。また、文法もPython風であり習得しやすいのも利点だろう。

　いっぽう、特に大きな欠点は（いまのところ）見つかっていないのだが、日本語環境で利用する場合は文字コードをうまく扱うように適切にオプションを与える必要がある。

　ちなみに、MakoのWebサイトにはPython向けテンプレートエンジンのパフォーマンス比較が掲載されているのだが、ほかのテンプレートエンジンと比べてMakoは同等レベル以上に高速、という結果が出ているようだ。

#### Makoのインストール

　Makoは[ダウンロードページ][6]から行える。配布されているtar.gz形式のソースコードをダウンロードしてインストールできるほか、Pythonモジュール用のインストールマネージャ「[easy_install][7]」を利用してもインストールできる。

　ソースコードからインストールする場合は、ダウンロードしたアーカイブを展開し、次のように実行する。

<pre># python setup.py install
</pre>

　ちなみに、makoはすべてPythonコードで記述されているため、基本的にはPythonが動く環境であればどのプラットフォームでも動作するはずだ。

　つづく。

 [1]: http://www.makotemplates.org/
 [2]: http://docs.python.org/library/string.html#template-strings
 [3]: http://www.djangoproject.com/
 [4]: http://djangoproject.jp/doc/ja/1.0/ref/templates/api.html
 [5]: http://www.cheetahtemplate.org/
 [6]: http://www.makotemplates.org/download.html
 [7]: http://peak.telecommunity.com/DevCenter/EasyInstall
