---
slug: centos-redhat-registry-certs-error
title: CentOS＋Docker関連でregistry.access.redhat.comのDockerレジストリからpullできなくなった場合の対処
tags: [ centos, linux ]
date: 2018-12-04T18:46:37+09:00
lastmod: 2018-12-04T18:51:53+09:00
publishDate: 2018-12-04T18:46:37+09:00
---

　CentOS 7でpython-rhsm-certificatesパッケージの仕様が変わり、今までここに含まれていたRed Hat関連の証明書がなくなってしまった模様（[CentOS Bug Tracker](https://bugs.centos.org/view.php?id=14785")）。そのせいで、Red Hatが提供しているDockerコンテナリポジトリであるregistry.access.redhat.comにCentOS 7環境からアクセスできなくなる状況が発生する。

　たとえば、CentOS上で組んだKubernetes環境ではregistry.access.redhat.com/rhel7/pod-infrastructureというコンテナが使われるのだが、このイメージがPullできなくなるエラーが発生する。

```
ErrImagePull: "image pull failed for registry.access.redhat.com/rhel7/pod-infrastructure:latest, this may be because there are no credentials on this request.  details: (open /etc/docker/certs.d/registry.access.redhat.com/redhat-ca.crt: no such file or directory)"
```

　この変更はほかのさまざまなパッケージでも影響が出ているようだが、根本的な問題解決はRed Hat/Cent OS側で対処してもらうしかない。とりあえずは古いpython-rhsm-certificatesパッケージをダウンロードして、そこから問題の証明書を抜き出して手動で配置することで対処は可能。手順的には下記となる。

```
$ wget http://mirror.centos.org/centos/7/os/x86_64/Packages/python-rhsm-certificates-1.19.10-1.el7_4.x86_64.rpm
$ rpm2cpio python-rhsm-certificates-1.19.10-1.el7_4.x86_64.rpm | cpio -iv --to-stdout ./etc/rhsm/ca/redhat-uep.pem | tee redhat-uep.pem
$ sudo cp redhat-uep.pem /etc/rhsm/ca/
```


