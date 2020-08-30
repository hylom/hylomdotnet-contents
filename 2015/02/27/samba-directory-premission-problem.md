---
slug: samba-directory-premission-problem
title: Sambaで共有したディレクトリ内のパーミッション問題
tag: [ linux, tips ]
date: 2015-02-27T19:36:50+09:00
lastmod: 2015-02-27T19:36:59+09:00
publishDate: 2015-02-27T19:36:50+09:00
---

<p>
　Sambaで共有したLinuxマシン上のディレクトリにWindowsからアクセスした際、作成したファイルのパーミッションが755とかになってしまう問題がある。この場合、smb.confで「map archive = no」を指定すると解決する。副作用などについてはググれ。
</p>
