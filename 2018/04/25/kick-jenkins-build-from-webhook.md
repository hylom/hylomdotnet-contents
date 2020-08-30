---
slug: kick-jenkins-build-from-webhook
title: JenkinsのWebフックによるビルド設定メモ
tag: [ jenkins ]
date: 2018-04-25T22:15:53+09:00
lastmod: 2018-04-25T22:16:11+09:00
publishDate: 2018-04-25T22:15:53+09:00
---

　Jenkinsをアップデートしたらグローバルセキュリティ設定を確認しろというメッセージが出たので色々設定したら、gitのpushに対応させてビルドするために設定していたWebフックが動かなくなった。そのための対応メモ。アドホックにやったので正しい対策ではないかもしれない。

## グローバルセキュリティ設定



　「行列による権限管理（プロジェクト単位）」を有効にして、匿名ユーザーに対し「ジョブ」の「Build」を許可する。このとき、ログインしているユーザーに全権限を与えないとその後Jenkinsの操作ができなくなる場合がある（ググればその場合の対策法が出てくる）。

　また、「CSRF対策」は無効にする。有効にすると事前にトークンの取得が必要になるらしい（参考：[https://stackoverflow.com/questions/38137760/jenkins-rest-api-create-job](https://stackoverflow.com/questions/38137760/jenkins-rest-api-create-job)）。面倒臭いので無効にする。

## プロジェクト単位の権限設定



　匿名ユーザーに「ジョブ」の「Build」、「Read」、「Workspace」を有効にする。

　これでビルドできた。「リモートからビルド」は有効にしておくが、認証トークンが必要かどうかは不明。

