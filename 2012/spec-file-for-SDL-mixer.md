---
slug: spec-file-for-SDL-mixer
title: SDL_mixerのspecファイル
tags: [ rpm, centos, programming ]
date: 2012-09-12T16:54:03+09:00
lastmod: 2013-04-16T23:38:29+09:00
publishDate: 2012-09-12T16:54:03+09:00
---

<p>　<a href="http://www.libsdl.org/projects/SDL_mixer/">SDL_mixer</a>はCentOS用のパッケージが用意されていない＆提供されているSRPMをx64環境でビルドすると64ビットバイナリが/usr/lib/以下にインストールされてしまうという問題があるので、これを修正するspecファイルを作成した。<a href="https://gist.github.com/3705028">Gist:SDL_mixer.spec</a>で公開している。</p>

<iframe src="/embed/https://gist.github.com/anonymous/3705028.js"></iframe>

