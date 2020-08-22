---
slug: build-kubernetes-cluster-on-fedora-28
title: Fedora28で自前Kubernetesクラスタを作るメモ
tags: [ fedora, linux, k8s, kubernetes ]
date: 2018-05-11T19:48:58+09:00
lastmod: 2018-05-15T19:10:46+09:00
publishDate: 2018-05-11T19:48:58+09:00
---

　とりあえず基本的な流れは以前[さくらのナレッジに書いたもの](https://knowledge.sakura.ad.jp/3681/)と同じ。ただし、クラスタノードのkubelet設定ファイル（/etc/kubernetes/kubelet）の「KUBELET_ARGS」に次のように「--kubeconfig」および「--require-kubeconfig」パラメータを追加した上で、kubelet.ymlファイルを用意する必要がある。

```
KUBELET_ARGS="--cgroup-driver=systemd --fail-swap-on=false --kubeconfig=/etc/kubernetes/kubelet.yml --require-kubeconfig"
```

　kubelet.ymlファイルはこんな感じ。

```
kind: Config
clusters:
- name: local
  cluster:
    server: http://＜api-serverのホスト名かIPアドレス＞:8080
users:
- name: kubelet
contexts:
- context:
    cluster: local
    user: kubelet
  name: kubelet-context
current-context: kubelet-context
```

　--api_servers（--api-servers）オプションは廃止されているので、このように設定ファイルでapi-serverのURLを指定しなければならない模様（[https://github.com/kubernetes/website/issues/7417](https://github.com/kubernetes/website/issues/7417)）。


## （追記@2018-05-15）


　kube-proxyにはiptables 1.6.2と組み合わせて使うとiptablesルールを適切に設定できないという[不具合](https://github.com/NixOS/nixpkgs/issues/35544)がある。Fedora 28のiptablesは1.6.2なので、これに引っかかる。Fedora 28のKubernetesパッケージに含まれているkubeletでは現時点でこれが修正されていない。とりあえずFedora 27用のiptables 1.6.1に置き換えることで問題は回避できそう。

```
$ wget https://dl.fedoraproject.org/pub/fedora/linux/releases/27/Everything/x86_64/os/Packages/i/iptables-1.6.1-4.fc27.x86_64.rpm
$ wget https://dl.fedoraproject.org/pub/fedora/linux/releases/27/Everything/x86_64/os/Packages/i/iptables-libs-1.6.1-4.fc27.x86_64.rpm
# dnf install iptables-*.rpm
```


