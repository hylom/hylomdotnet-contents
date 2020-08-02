---
slug: kubectl-notacceptable-error
title: kubectlコマンドで「NotAcceptable」というエラーが出たときの話
tags: [ kubernetes, k8s, linux ]
date: 2018-07-04T18:20:48+09:00
lastmod: 2018-07-04T18:21:00+09:00
publishDate: 2018-07-04T18:20:48+09:00
---

　テスト用のKubernetesクラスタをメンテナンスしていたら、突然クラスタの操作ができなくなった。次のようなエラーが出る。

```
$ kubectl get nodes
No resources found.
Error from server (NotAcceptable): unknown (get nodes)
```

　色々調べたところ、うっかりkubectlコマンドをアップデートしてしまってクラスタ側とバージョンが一致しなくなっていた（クラスタ側は1.7.7、kubectlコマンドは1.11）。kubectlコマンドをダウングレードすることで対処できた。


