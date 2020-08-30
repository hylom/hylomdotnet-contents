---
title: 激安・低サポートのVPS「prgmr.com」を借りる
author: hylom
type: post
date: 2010-07-02T07:49:58+00:00
url: /2010/07/02/start-vps-withprgmr-com%e3%80%8d%e3%82%92%e5%80%9f%e3%82%8a%e3%82%8b/
category:
  - Docs
tag:
  - hosting
  - vps
  - web

---
　最近、月額490円からの「[ServersMan@VPS][1]」が話題だ。ほかにも980円からの「[FC2 VPS][2]」など、低価格のVPSはいくつかあるが、それ以前から存在する低価格のVPSサービスとして一部の間で知られていたのが「[prgmr.com][3]」である。

　prgmr.comはXenを使用したVPSで価格は$5/月からと低価格なのが魅力の1つだが、安さだけなら国内のVPSサービスと大きくは変わらない。ではなぜprgmr.comが注目されているのかというと、そのアレなたたずまいと、サポートの簡素さによるところが大きい。prgmr.comのトップページにはほかのVPSサービスのような画像による装飾は一切なく、アスキーアートで書かれた「prgmr.com」というバナーと「We don&#8217;t assume you are stupid.」という文言、そして料金やXenベースVPSの特徴が紹介されているのみ。一般人ならとりあえずこのサイトが何であるかも理解できないだろう、という作りである。

　このようにアレゲ感たっぷりのprgmr.comであるが、その一方でかなり自由度は高く、OSはDebian GNU/Linux、Ubuntu 10.04、CentOS 5.5が選択できるほか、AMD64アーキテクチャのXen上で動作するOSなら（自力で）任意のOSがインストールできる（可能性がある）、追加料金なしでグローバルIP付与と、独自のサーバー管理＆Xenが分かる人にとってはかなり魅力的であったりする。

　ということで一部の人には魅力的なこのprgmr.com、ちょくちょく新規受付を開始しては定員に達して終了を繰り返しており、いつでも申し込みできるというわけではないのだが、ウォッチしていたらたまたま申し込み可能になっていたため、$12/月でメモリ512MiB、ディスク12GiB、月間ネットワーク転送量80GiBのプランを申しこんでみた。

#### Webでの申し込み後、メールでSSH公開鍵を送付。サーバー設定は必要十分

　Webで利用したいプランを選択し、オンラインフォームに必要事項を記入して申し込むと、下記のように利用したいディストリビューションとOpenSSH公開鍵を送信しろ、という旨のメールが来る。

> you ordered a xen vps, 512MiB ram, 12GiB Disk 80 GiB transfer Xen VPS, $12/month username hylom
> 
> Before I can set you up, I need to know what distro you would like and an OpenSSH format public key (on a *NIX, run ssh-keygen and send me either the id\_dsa.pub or id\_rsa.pub file in an attachment)

　あとはこのメールの返信として公開鍵を添付し、Debian GNU/Linuxを使いたいという旨を伝えるだけだ。

> Hi,
> 
> I want to use Debian GNU/Linux, and here&#8217;s my SSH public key.
> 
> Please check it. 

　設定が完了すると、その旨がメールで連絡される。また、しばらくすると金払ってねメールがやってくる模様。料金の支払いはPayPal。

　続く。

 [1]: http://dream.jp/vps/
 [2]: http://fc2-vps.com/
 [3]: http://prgmr.com/
