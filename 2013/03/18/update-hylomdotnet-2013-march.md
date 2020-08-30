---
slug: update-hylomdotnet-2013-march
title: hylom.netのアップデート
tag: [ node.js, hylom.net ]
date: 2013-03-18T00:13:34+09:00
lastmod: 2013-03-18T00:15:54+09:00
publishDate: 2013-03-18T00:13:34+09:00
---

<p>　hylom.netのCMSを、いままで使っていたWordPressからNode.jsで実装した独自のシステムに移行させました。WordPressに大きな不満はなかったのですが、もう少し気軽に記事を書きたいと思ったのと、Node.jsベースのシステムであればもう少しパフォーマンスを出せるのではないかと思ったのが移行のきっかけです。</p>

<p>　システムとしては、先日発売されたNode.jsの書籍「<a href="http://www.sbcr.jp/products/4797370904.html">はじめてのNode.js －サーバーサイドJavaScriptでWebアプリを開発する－</a>」で解説しているブログシステム「<a href="http://sourceforge.jp/users/hylom/pf/node_sample_nblog/scm/">nblog</a>」をベースにカスタマイズしています。まだまだ最低限の機能しか実装していないのですが、今後デザイン面も含めて改善予定ですのでご期待ください。</p>

<p>　また、旧hylom.netのコンテンツは従来のURLでそのままアクセスが可能なようになっています。こちらは、WordPressを別のポートで稼働させた上でNode.js側でリバースプロクシ的な処理をするコードをブログシステムに埋め込むことで実現しています。一応WordPressのデータのインポートをする仕組みは作っているのでいつかは旧コンテンツもNode.jsベースのシステムで閲覧できるようにする予定です。</p>
