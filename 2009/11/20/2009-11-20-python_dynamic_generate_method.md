---
title: Pythonネタ：クラスメソッドを動的に生成する
author: hylom
type: post
date: 2009-11-19T18:09:31+00:00
excerpt: '<p>　Pythonには動的に関数を作ったり、クラスのメソッド呼び出しをカスタマイズするための機構が用意されています。ということで、それを使って遊んでみた。</p>'
url: /2009/11/20/python_dynamic_generate_method/
categories:
  - Docs

---
　Pythonには動的に関数を作ったり、クラスのメソッド呼び出しをカスタマイズするための機構が用意されています。ということで、それを使って遊んでみた。

　まず、Pythonではクラスで\_\_getattr\_\_メソッドを定義することで、クラスに対する任意の属性値アクセスを横取りすることができる。

　Pythonのクラスやオブジェクトは、それぞれが持つ属性（クラスならメンバ関数/変数）を\_\_dict\_\_というdictionary内に格納している。たとえばとあるオブジェクトaに対し「a.x」という操作を行うと、まずPython処理系はそのオブジェクトが持つ\_\_dict\_\_内で「x」という名前を持つメンバ変数/関数を探し、存在しなければ続いてそのオブジェクトのクラスが持つ\_\_dict\_\_内、続いてそのクラスの派生元クラスの\_\_dict\_\_内、という順でメンバ変数/関数を探索する。

　この作業を行って、通常すべての\_\_dict\_\_内で該当する名前が存在しなければエラーとなり例外を発生させるのだが、もしオブジェクト/クラス/派生元クラス内で\_\_getattr\_\_()メソッドが定義されていた場合、例外を発生させずに\_\_getattr\_\_()メソッドが呼び出される仕組みになっている。

　まぁ、サンプルコードを見たほうが分かりやすいかと。下記は、メソッドを呼び出すと、そのメソッド名を返すというクラス「echo」の例。

<pre>$ python
Python 2.6.1 (r261:67515, Jul  7 2009, 23:51:51)
[GCC 4.2.1 (Apple Inc. build 5646)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; class echo(object):
...     def __getattr__(self, name):
...             return lambda: name
...
&gt;&gt;&gt; o = echo()
&gt;&gt;&gt; o.hoge()
'hoge'
&gt;&gt;&gt; o.foobar()
'foobar'
&gt;&gt;&gt; o.abcdefg()
'abcdefg'</pre>

　\_\_getattr\_\_()メソッドは、あるオブジェクトの属性値/属性メソッドにアクセスしようとした際に、そのオブジェクト/クラス/派生元クラス内で目的となる属性が見つからなかった場合に呼び出される。引数nameにはアクセスしようとした属性の名前が与えられる。ここではlambda構文を使用し、引数nameを返す関数を\_\_getattr\_\_の戻り値とした。

　また、オブジェクトの\_\_dict\_\_属性に値を追加することで、動的に任意の属性をオブジェクトに追加できる。

　下記は、オブジェクトにメソッドを追加するメソッド「teach」を備えたクラス「echo2」の例。

<pre>&gt;&gt;&gt; class echo2(object):
...     def teach(self, key, value):
...             self.__dict__[key] = lambda : value
...
&gt;&gt;&gt; o = echo2()
&gt;&gt;&gt; o.hoge()
Traceback (most recent call last):
  File "", line 1, in
AttributeError: 'echo2' object has no attribute 'hoge'
&gt;&gt;&gt; o.teach("hoge", "foobar")
&gt;&gt;&gt; o.hoge()
'foobar'
&gt;&gt;&gt; o.teach("abcdefg", "alphabet")
&gt;&gt;&gt; o.abcdefg()
'alphabet'</pre>

　このへんの仕組みがどのような場合に有効化というと、たとえば単純なメソッドを大量に用意したい場合。下記は、「False」を返すis\_a()〜is\_z()までを一気に定義するというもの。

<pre>&gt;&gt;&gt; for i in "abcdefghijklmnopqrstuvwxyz":
...     o.__dict__["is_"+i] = lambda : False
...
&gt;&gt;&gt; o.is_a()
False</pre>

　覚えておくと、たまにラクができるかも。
