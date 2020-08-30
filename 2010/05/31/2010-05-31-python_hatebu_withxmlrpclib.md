---
title: Pythonで被はてなブックマーク数を取得する
author: hylom
type: post
date: 2010-05-31T10:43:54+00:00
url: /2010/05/31/python_hatebu_withxmlrpclib/
category:
  - Docs
tag:
  - module
  - python
  - xmlrpclib

---
　Pythonのxmlrpclibモジュールで、指定したURLの被はてなブックマーク数を取得する例。簡単ですね。

　server.bookmark.getCount()はURLをキー、被はてブ数の値とするdictionaryの形で返してくれるので、返ってきたデータの参照も楽勝です。URLの一覧を引数の形で与えなければならないのがなんか引っかかりますが……。

<pre>#!/usr/bin/env python

import xmlrpclib


def main():
    uri = "http://b.hatena.ne.jp/xmlrpc"
    server = xmlrpclib.ServerProxy(uri)
    urls = ("http://sourceforge.jp/magazine/10/04/26/0244255",
             "http://sourceforge.jp/magazine/10/04/27/0326224",
             "http://sourceforge.jp/magazine/10/04/30/0243232")

    t = server.bookmark.getCount(*urls)
    for item in t:
        print item, t[item]

if __name__ == "__main__":
    main()
</pre>
