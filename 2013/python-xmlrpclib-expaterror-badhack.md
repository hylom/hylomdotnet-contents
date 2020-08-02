---
slug: python-xmlrpclib-expaterror-badhack
title: Python 2.6/2.7のxmlrpclibでxml.parsers.expat.ExpatErrorが出た場合の対処
tags: [ python,programming ]
date: 2013-06-26T22:40:25+09:00
lastmod: 2013-06-26T22:40:55+09:00
publishDate: 2013-06-26T22:40:25+09:00
---

<p>　Python 2.6系および2/7系のxmlrpclibで、サーバーからはどう見ても正しいXMLが返ってきているはずなのにxml.parsers.expat.ExpatErrorが出た場合の対処方法メモ。</p>

<p>　xmlrpclibでは、サーバーから受け取ったXMLデータを一定サイズごとに分割してXMLパーサーに投入する、という処理を行っている。このときXMLパーサーにExpatを使っていると、受け取ったデータが分割される位置によっては、不正なXMLと認識されて以下のようにエラーになる模様（DebianのPython 2.6.6とMac OS XのPython 2.7.2で確認）。Expatを使わないようにするとこの問題は発生しない。</p>

<pre>
  File "/Users/hylom/repos/anpanel/myxmlrpclib.py", line 559, in feed
    self._parser.Parse(data, 0)
xml.parsers.expat.ExpatError: not well-formed (invalid token): line 30, column 114
</pre>

<p>　たぶん挙動的にExpatのバグのようだが、それを修正する気力もなかったので、とりあえずxmlrpclibでExpatを使わないようにすることで対処。たぶんパース速度は低下すると思われるが。具体的には、xmlrpclibをimportしたのち、XMLパーサーを取得するxmlrpclib.getparser関数を以下のようにして置き換える。</p>

<pre>
import xmlrpclib

# xmlrpclib's ExpatParser has bug, so do not use
org_getparser = xmlrpclib.getparser
def mygetparser(use_datetime=0):
    (p, t) = org_getparser(use_datetime)
    # if parser is ExpatParser, replace to SlowParser
    if isinstance(p, xmlrpclib.ExpatParser):
        p = xmlrpclib.SlowParser(p._target)
    return (p, t)
xmlrpclib.getparser = mygetparser
</pre>

<p>　ここでは、getparser関数の戻り値がExpatParserクラスのインスタンスだった場合、SlowParserクラスのインスタンスに置き換えるという処理をやっている。当然ながらかなりのdirty hackなので利用はおすすめしない。</p>
