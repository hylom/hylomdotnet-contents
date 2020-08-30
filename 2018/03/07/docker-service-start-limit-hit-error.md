---
slug: docker-service-start-limit-hit-error
title: 「start-limit-hit」といったメッセージが出てdocker serviceの起動に失敗した場合の対処法
tag: [ docker, linux ]
date: 2018-03-07T17:14:13+09:00
lastmod: 2018-03-07T17:15:07+09:00
publishDate: 2018-03-07T17:14:13+09:00
---

　systemdでdocker serviceの起動時に、次のようなエラーが出て起動できない場合がある（このメッセージはjournalctl -xeコマンドで確認）。

```
-- The result is failed.
 3月 07 18:28:10 fedora25 systemd[1]: docker.service: Unit entered failed state.
 3月 07 18:28:10 fedora25 systemd[1]: docker.service: Failed with result 'start-limit-hit'.
```

　このエラーは使用しているdockerのバージョンとsystemdのdocker.service設定ファイルの内容が合っていない場合に出るようだ。このエラーが出た環境は、Dockerが配布しているパッケージでDockerをインストール後、そのパッケージを削除してFedora 25標準のパッケージに入れ直したというもの。自分で作成して忘れていたのか、それともパッケージによってインストールされたのか分からないが、/etc/systemd/systemディレクトリ以下にdocker.serviceファイルが残っていたのが原因。

　このファイルを削除し、systemctl daemon-reloadでsystemdの設定を読み直したら復旧した。

