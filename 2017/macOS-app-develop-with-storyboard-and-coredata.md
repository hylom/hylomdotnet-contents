---
slug: macOS-app-develop-with-storyboard-and-coredata
title: macOSアプリ開発でStoryboard＋Core Dataを使うときのハマり話
tags: [ macos,programming ]
date: 2017-04-09T22:55:35+09:00
lastmod: 2017-04-10T00:57:33+09:00
publishDate: 2017-04-09T22:55:35+09:00
---

　ふと思い立って久しぶりにmacOSアプリ開発を始めて見たのだが、Core Dataで管理しているデータを（CocoaBindingを使って） Storyboardを使って作った画面上に表示するところでハマったうえにググっても情報を探すのが大変だったのでメモ。

## 参考文献


・[Developers.IOの記事](http://dev.classmethod.jp/smartphone/iphone/remind-storyboard/)：Storyboardを使った開発の概要
・[Core Dataに関するAppleの公式ドキュメント（日本語）](https://developer.apple.com/jp/documentation/Cocoa/Conceptual/CoreData/index.html)：Core Dataの概要。ただし理解しにくい
・[上記ドキュメントの英語版](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CoreData/index.html)：Swift 3対応などのアップデート済み
・[Core Data の使い方（１）](http://www.nashuaworks.com/KTDContens/201507101234.html)：Core DataのデータをViewに表示する作業手順解説

## 作業と疑問点


　Xcode（7.2.1）でOS Xの「Cocoa Application」を選択してテンプレートからプロジェクトを作成。このとき「Use Storyboards」、「Create Document-Based Application」、「Use Core Data」にチェックを入れておく。続いてAppleのCore Dataプログラミングガイドの「管理オブジェクトモデルの作成」に従ってオブジェクトモデルを作成する。

　さらにこのドキュメントでは「Core Dataスタックの初期化」を行うよう記されていて、NSManagedObjectContext、NSPersistentStoreCoordinator、NSManagedObjectModelの3つが必要と記述されている。しかし、初期化コードとしてDataControllerクラスの実装例もあるのだが、このオブジェクトをどのオブジェクトが所持すべきなのか（ビューなのかドキュメントなのか）が記載されていない。

　プロジェクト作成時に「Use Core Data」にチェックを入れておくと、ドキュメントの基底クラスとしてNSPersistentDocumentが使われるのだが、[ドキュメント](https://developer.apple.com/reference/appkit/nspersistentdocument)を見る限り、自動的にCore Data関連の初期化を行って「ready-to-use」のNSManagedObjectContextのインスタンスを提供すると書いてある。この解釈だと、自前でCore Dataスタックの初期化をする必要はなさそうである。

　「Core Data の使い方（１）」ページではViewController内でNSManagedObjectContextのインスタンスを作成し、ここでCore Dataの初期化を行っているのだが、本来Core Dataの管理はDocument（MVCにおけるModel）の仕事であるべきで、ViewController内でこの作業を行うのはよろしくないのではないか、という疑問があるし、前述の通りNSPersistentDocumentを利用する場合この処理は不要であるはずである。

　しかし、Documentが持つNSManagedObjectのインスタンスをArray Controllerに参照させる手段が分からない。DocumentにArray Controllerのoutletを作成できれば、そのオブジェクトのsetManagedObjectContextを使ってNSManagedObjectContextインスタンスを渡すことはできるのだが、StoryboardではDocumentにArray Controllerのoutletを作成することもできない。

　ちなみにArray Controllerを使ってTable ViewとArray Controllerをバインドしただけだと、Array ControllerにNSManagedObjectContextが関連付けられていないため「cannot perform operation without a managed object context」というメッセージが表示される。

## 解決法


　[StackOverflowの「How do you bind a storyboard view to a Core Data entity when using NSDocument?」](http://stackoverflow.com/questions/35167244/how-do-you-bind-a-storyboard-view-to-a-core-data-entity-when-using-nsdocument)にそのものずばりの質問と回答があった。結論的には、まずDocument.swiftのmakeWindowControllers()の末尾に下記を追加する。

```
windowController.contentViewController!.representedObject = windowController.document
```

　これでView ControllerのrepresentedObjectがDocumentを参照するようになる。

　続いてArray ControllerのView Controllerで、Managed Object Contextで「Bind to」にチェックを入れ、「View Controller」を指定する。Model Key Pathには「representedObject.managedObjectContext」を指定する。以上で完了。ただ、このときModel Key Pathに「！」が表示されるのがちょっと気持ち悪い。

## まとめ



・「Use Core Data」を選択してプロジェクトのテンプレートを作った場合、独自に初期化コードを書く必要は無い
・DocumentからView Controllerにアクセスするのは面倒臭い

　なおこの辺の作業を行ったコードは[https://github.com/hylom/ttune/tree/76d43fe476c24f064aee51b7748529aa82a309d1](https://github.com/hylom/ttune/tree/76d43fe476c24f064aee51b7748529aa82a309d1)です。


