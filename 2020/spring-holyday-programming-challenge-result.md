---
slug: spring-holyday-programming-challenge-result
title: GW引き篭もりチャレンジ：React＋Electronでアプリを作ってみた総括
tags: [ programming react electron javascript ]
date: 2020-05-06T19:15:09+09:00
lastmod: 2020-05-06T19:15:09+09:00
publishDate: 2020-05-06T19:15:09+09:00
---

　5連休も最終日となりましたが、あっという間でしたね。ということで本日は5日間分のReactアプリ作成レポートをまとめておりました。普段の仕事と変わらないことをやっていたような気もしますが、何もできない連休だったので仕方がないとも言えます。

 - [GW引き篭もりチャレンジ：Reactでアプリを作ってみる（1日目）](http://hylom.net/create-react-app-with-openapi-and-nodejs)
 - [Reactでアプリを作ってみる（2日目） - PDFからのサムネイル生成](http://hylom.net/generate-thumbnail-image-from-pdf-with-nodejs)
 - [Reactでアプリを作ってみる（3日目） - コンテンツの動的な表示](http://hylom.net/show-image-dynamically-by-react)
 - [Reactでアプリを作ってみる（4日目） - Electronを使ったアプリ化](http://hylom.net/convert-react-app-to-electron-app)
 - [Reactでアプリを作ってみる（5日目） - ダブルクリックでファイルを開く](http://hylom.net/handling-double-click-event-in-react)

　Reactのフル機能に触ったわけではないですが、さすがによくできているなと感じました。GUIアプリケーションの構築においてはコンポーネントごとにクラス化するというのが定番のアプローチなのですが、それをうまくJavaScriptの流儀に落とし込めていると思います。開発環境が簡単に構築でき、またコマンド1つで最終的なHTMLやminifyされたJavaScriptコードを出力できるのも便利でした。ただ、そのバックエンドはブラックボックス化されている（Webpackの設定ファイルなどはまったく触れない）ので、ここから外れた使い方をしようとすると面倒なのかもしれません。

　そして、React＋Electronの開発が以外に簡単でリリース版パッケージの作成も以外に容易にできるというのはちょっと驚きでした。今回はWebアプリを作ってそこからElectronアプリを作るという流れで作ったために若干無駄な作業が発生してはいますが、最初からElectronアプリを作ることを想定すればもっと迅速な開発ができるのではないかと思いました。

　なお連休は終わりますが、この電子書籍管理アプリについては普通に機能を追加していきたいのでゆったりと開発を続ける予定です。まずはタグやタイトルの管理機能を実装したいですね。

