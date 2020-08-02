---
title: VirtualBoxでGNOME Shellを使う（Fedora 16）
author: hylom
type: post
date: 2011-12-05T16:31:57+00:00
url: /2011/12/06/fedora16_on_virtualbox_with_gnome_shell/
categories:
  - Hacks
tags:
  - fedora
  - gnome
  - virtualbox

---
　VirtualBoxでFedora 16のデスクトップを使う場合、デフォルトだとGNOME Shellが利用できない。GNOME Shellの利用にはハードウェアアクセラレーションが必要なためだ。VirtualBoxの場合、Guest Additionをインストールすればハードウェアアクセラレーションが利用可能になり、GNOME Shellが利用可能になる。

#### VirtualBox Guest Additionのインストール

　基本的な設定は[Install Fedora 16 VirtualBox Guest Additions and Get Working Gnome Shell Inside Virtual Machine][1]という記事にある通り。

##### 1. 仮想マシンの設定の「ディスプレイ」項目で、ビデオメモリを128MBに設定、「3Dアクセラレーションを有効化」にチェックを入れる。

<div id="attachment_1509" style="width: 410px" class="wp-caption aligncenter">
  <a href="/img/blog/2011/12/vm_config1.png"><img src="/img/blog/2011/12/vm_config1-400x215.png" alt="VirtualBoxの設定" title="VirtualBoxの設定" width="400" height="215" class="size-medium wp-image-1509" srcset="/img/blog/2011/12/vm_config1-400x215.png 400w, /img/blog/2011/12/vm_config1.png 684w" sizes="(max-width: 400px) 100vw, 400px" /></a>
  
  <p class="wp-caption-text">
    VirtualBoxの設定
  </p>
</div>

##### 2. Guest Additionのインストールにはカーネルモジュールのビルドが必要なので、カーネルヘッダーや開発ツールをインストールしておく。

<pre># yum install kernel-devel kernel-headers dkms gcc-c++
</pre>

##### 3. VirtualBoxの「デバイス」−「Guest Additionsのインストール」を選択してGuest Additionsをマウントする。

##### 4. 下記を実行

<pre># cd /media/VBOXADDITIONS_4.1.6_74713/
# ./VBoxLinuxAdditions.sh
</pre>

##### 5. SELinuxの設定変更

　インストールされるVirtualBox Guest Addition関連ファイルのSELinuxラベルが不適切なので、変更する。

<pre># cd /opt/VBoxGuestAdditions-4.1.6/lib/
# /sbin/restorecon -v *.so 
</pre>

　実行後、ls -Zでラベルが「textrel\_shlib\_t」になっていることを確認する

<pre>$ ls -Z
drwxr-xr-x. root root unconfined_u:object_r:usr_t:s0   VBoxGuestAdditions
-rwxr-xr-x. root root unconfined_u:object_r:textrel_shlib_t:s0 VBoxOGLarrayspu.so
-rwxr-xr-x. root root unconfined_u:object_r:textrel_shlib_t:s0 VBoxOGLcrutil.so
-rwxr-xr-x. root root unconfined_u:object_r:textrel_shlib_t:s0 VBoxOGLerrorspu.so
-rwxr-xr-x. root root unconfined_u:object_r:textrel_shlib_t:s0 VBoxOGLfeedbackspu.so
-rwxr-xr-x. root root unconfined_u:object_r:textrel_shlib_t:s0 VBoxOGLpackspu.so
-rwxr-xr-x. root root unconfined_u:object_r:textrel_shlib_t:s0 VBoxOGLpassthroughspu.so
-rwxr-xr-x. root root unconfined_u:object_r:textrel_shlib_t:s0 VBoxOGL.so
</pre>

##### 6. ログアウトして再ログインする

　以上で作業完了。

<div id="attachment_1507" style="width: 410px" class="wp-caption aligncenter">
  <a href="/img/blog/2011/12/vm_fedora1.png"><img src="/img/blog/2011/12/vm_fedora1-400x319.png" alt="VirtualBox上のFedoraでGNOME Shellが動作している" title="VirtualBox上のFedoraでGNOME Shellが動作している" width="400" height="319" class="size-medium wp-image-1507" srcset="/img/blog/2011/12/vm_fedora1-400x319.png 400w, /img/blog/2011/12/vm_fedora1.png 1052w" sizes="(max-width: 400px) 100vw, 400px" /></a>
  
  <p class="wp-caption-text">
    VirtualBox上のFedoraでGNOME Shellが動作している
  </p>
</div>

 [1]: http://www.sysprobs.com/install-fedora-16-virtualbox-guest-additions-get-working-gnome-shell-inside-virtual-machine