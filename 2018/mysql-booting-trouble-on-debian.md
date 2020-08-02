---
slug: mysql-booting-trouble-on-debian
title: Debianで突然mysqlサービスが起動しなくなった
tags: [ linux,mysql ]
date: 2018-05-07T14:02:44+09:00
lastmod: 2018-05-07T14:03:08+09:00
publishDate: 2018-05-07T14:02:44+09:00
---

　Debianのmysqlパッケージをアップデートしたら突然mysqlサービスが起動しなくなった。journalctlでエラーメッセージを見ると、次のように出力されている。

```
# journalctl -u mysql
  ：
  ：
May 07 06:10:09 gate mysqld[3528]: /usr/sbin/mysqld: Error on realpath() on '/var/lib/mysql-files' (Error 2)
May 07 06:10:09 gate mysqld[3528]: 180507  6:10:09 [ERROR] Failed to access directory for --secure-file-priv. Please make sure that directory exists and is accessible by MySQL Server. Supplied value : /var/lib/mysql-files
```

　この場合、/var/lib/mysql-filesディレクトリを作成すればOKのようだ。問題のパラメータ「--secure-file-priv」についてのドキュメントは[ここにある](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_secure_file_priv)。

```
# mkdir /var/lib/mysql-files
# chown mysql:mysql  /var/lib/mysql-files
# chmod 700 /var/lib/mysql-files
```

