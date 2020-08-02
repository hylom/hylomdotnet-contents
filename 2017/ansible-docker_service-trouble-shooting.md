---
slug: ansible-docker_service-trouble-shooting
title: Ansibleのdocker_serviceモジュールのトラブルシューティング
tags: [ ansible ]
date: 2017-06-08T18:12:04+09:00
lastmod: 2017-06-08T21:21:28+09:00
publishDate: 2017-06-08T18:12:04+09:00
---

　Ansibleにはdocker_serviceというDockerを操作するためのモジュールがあるのだが、「preview」というステータスであるため現状（2017-06-08現在）色々と地雷が埋まっている。その最たるものがまともなエラーメッセージを吐いてくれないというもの。1月時点でIssueとして挙がっているのだが（[#20480](https://github.com/ansible/ansible/issues/20480)）、実行してDocker関連のエラーが出た場合に出るメッセージが「Error starting project」のみ。

　[この問題を解決するプルリクエスト](https://github.com/ansible/ansible/pull/20510)も出ているのだが、現時点ではAnsibleのリリース版にはマージされていない。

　ということで、暫定的な対応としてプルリクエストを出した作者のリポジトリから[docker_service.py](https://github.com/shabble/ansible/blob/bug/docker_service_stderr3/lib/ansible/modules/cloud/docker/docker_service.py)を直接ダウンロードしてインストールされているものと置き換えて使うとトラブルシューティングが捗るかと思われます。

