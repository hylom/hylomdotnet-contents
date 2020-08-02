---
slug: generate-thumbnail-image-from-pdf-with-nodejs
title: Reactでアプリを作ってみる（2日目） - PDFからのサムネイル生成
tags: [ node.js, programming, javascript ]
date: 2020-05-06T15:27:58+09:00
lastmod: 2020-05-06T19:17:00+09:00
publishDate: 2020-05-06T15:27:58+09:00
---

　前から触ってみたかったReactを使って、前から欲しいと思っていた電子書籍管理アプリを作ってみたレポート2日目です。今日はサムネイル画像生成の話でReactは全然関係ありません。

 - [GW引き篭もりチャレンジ：Reactでアプリを作ってみる（1日目）](http://hylom.net/create-react-app-with-openapi-and-nodejs)
 - Reactでアプリを作ってみる（2日目） - PDFからのサムネイル生成
 - [Reactでアプリを作ってみる（3日目） - コンテンツの動的な表示](http://hylom.net/show-image-dynamically-by-react)
 - [Reactでアプリを作ってみる（4日目） - Electronを使ったアプリ化](http://hylom.net/convert-react-app-to-electron-app)
 - [Reactでアプリを作ってみる（5日目） - ダブルクリックでファイルを開く](http://hylom.net/handling-double-click-event-in-react)


　電子書籍ファイルのサムネイルを表示させるために、表紙（つまり電子書籍の1ページ目）の画像の生成が必要となる。PDFファイルの場合、なんらかのツールを使って変換処理が必要となる。

　Node.js向けにはpdf-image（[https://www.npmjs.com/package/pdf-image](https://www.npmjs.com/package/pdf-image)）やpdf2pic（[https://www.npmjs.com/package/pdf2pic](https://www.npmjs.com/package/pdf2pic)）というPDFを扱えるモジュールがあるが、どちらもimagemagick（graphicsmagick）を使うようだ。しかし、imagemagickはインストールが面倒臭い上に脆弱性が度々発見されていたりするため、あまり使いたくない。結局PDFのラスタライズ機能だけがあれば良い訳で、調べたところGhostscriptライブラリ（libgs）のJavaScriptバインディングであるghostscript4js（[https://github.com/NickNaso/ghostscript4js](https://github.com/NickNaso/ghostscript4js)）というものがあり、これを使えば直接GhostscriptをNode.jsアプリから呼び出してPDFを画像化できるようだ。

　なお、GhostscriptのmacOS向けバイナリは公式には公開されていないのでインストールが若干面倒。これについては[別記事](http://hylom.net/build-ghostscript-on-macos)で書いた。

　実際にこれを使ってPDFからJPEG形式のサムネイル画像ファイルを生成するgenerateThumbnail()というメソッドを実装してみた（[コード全文はこちら](https://github.com/hylom/ebmgr/blob/b7571da8916bbec70e7ff79c164814e0f2494e75/ebmgr.js)）。とりあえずこれでサムネイル画像の生成は可能になった。

```
const gs = require('ghostscript4js');

exports.generateThumbnail = function generateThumbnail(vpath, page) {
  page = page || 1;
  const realPath = _vpathToRealPath(vpath);
  const target = path.parse(realPath);
  const outputPath = path.join(target.dir, target.name + '.jpeg');

  const gsCmd = [ "-sDEVICE=jpeg",
                  "-o",
                  outputPath,
                  "-sDEVICE=jpeg",
                  "-r72",
                  `-dFirstPage=${page}`,
                  `-dLastPage=${page}`,
                  realPath];

  gs.executeSync(gsCmd);
  return outputPath;
};
```

　ghostscript4jsのドキュメントには書いていないが、gs.executeCmdメソッドに渡すGhostscriptのオプションは単なる文字列だけでなく、このように文字列の配列形式で与えることも可能。パス名にスペースを含むファイル名を処理する場合はこのように配列形式で与えないとうまく処理できないようだ。また、"-sDEVICE=jpeg"が複数回登場しているが、なぜかこのように重複して指定しないとうまくファイルが生成されなかった。

　さて、この実装だと電子書籍ファイルと同じディレクトリにサムネイル画像を生成することになる。そのあたりの仕様をどうするか検討する必要がある。

　2日目は（Ghostscriptのビルドでちょっと時間を食ってしまったので）ここまで。作業時間は3時間ほど。

