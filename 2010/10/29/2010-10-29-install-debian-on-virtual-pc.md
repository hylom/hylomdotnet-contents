---
title: WindowsのVirtual PCにDebian GNU/Linux lennyをインストールするメモ
author: hylom
type: post
date: 2010-10-29T09:01:52+00:00
draft: true
url: /?p=1354
category:
  - Docs
tags:
  - debian
  - linux
  - virtualization
  - virtualpc

---
　WindowsのVirtual PCにDebian GNU/Linux lennyをインストールしようとしたら数回トラブったのでメモ。

  1. インストーラの起動時のカーネルオプションとして「vga=791 noreplace-paravirt」を追加（デフォルトのオプションに「vga=vesa」があるので、そこを置き換えればOK） 
      * 仮想ハードディスクは固定サイズにする。可変サイズだとディスクエラーが発生することがある 
          * インストールCDはできるだけ最新のものを利用しましょう 
              * インストール後はgrubのmenu.lstを修正。カーネルオプションとして「noreplace-paravirt」を追加する </ol> 
                　あと、apt-get update時に「the public key is not available: NO_PUBKEY ほげほげ」と言われて失敗したら「debian-archive-keyring」や「debian-keyring」パッケージをインストールしてみる（これが最適な方法なのか確証は持てないが、とりあえずこれで更新できた）。
