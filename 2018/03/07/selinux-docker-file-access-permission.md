---
slug: selinux-docker-file-access-permission
title: SELinuxを有効にしている場合にDockerコンテナからホストのファイルシステムにアクセスできない場合の対処法
tag: [ docker, selinux ]
date: 2018-03-07T17:45:42+09:00
lastmod: 2018-03-07T17:45:42+09:00
publishDate: 2018-03-07T17:45:42+09:00
---

　dockerでローカルのファイルシステムをコンテナ内にマウントして利用するとき、パーミッションは適切なはずなのにそのディレクトリにアクセスできないトラブルに遭遇（環境はFedora 25）。

　とりあえず、SELinuxの状況を確認。

```
# getenforce
Enforcing
```

　有効となっていたので、ログ（/var/log/audit/audit.log）を確認。次のように対象ディレクトリ（ここでは「hal」）に対するログが見つかった。つまり、SELinuxによってアクセスがブロックされていたということ。

```
type=AVC msg=audit(1520416357.374:153155): avc:  denied  { write } for  pid=18595 comm="java" name="hal" dev="dm-0" ino=398292 scontext=system_u:system_r:container_t:s0:c825,c930 tcontext=unconfined_u:object_r:user_home_t:s0 tclass=dir permissive=0
```

　細かくSELinuxのルールを設定するのが適切なのだが、今回はテスト環境なので次のようにしてcontainer_tに関するアクセス制御を全部無効にすることで対処。

```
# semanage permissive -a container_t
```

