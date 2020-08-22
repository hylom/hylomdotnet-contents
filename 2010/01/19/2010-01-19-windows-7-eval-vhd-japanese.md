---
title: Windows 7の評価版仮想ハードディスクイメージを日本語で使う
author: hylom
type: post
date: 2010-01-19T12:18:29+00:00
excerpt: |
  <p>　Microsoftが、Windows 7の90日期間限定評価版がインストールされた仮想ハードディスクイメージ（Windows 7 90-Day Eval VHD）を無償公開している。<a href="http://www.forest.impress.co.jp/docs/news/20091015_321806.html">窓の杜の記事</a>などでも紹介されているが、これは同じくMicrosoftがWindows環境向けに無償提供している<a href="http://www.microsoft.com/japan/windows/virtual-pc/">Virtual PC</a>上で利用できるもので、（期間限定、評価目的限定ではあるものの）ライセンスの問題なしにWindowsの仮想環境を構築できる。多くのソフトウェアのインストール/アンインストールを繰り返すライターや、クリーンな環境で動作確認を行いたいようなソフト開発者にとって非常に便利なソリューションだ。
  
  <p>　ただし、注意しなければ行けないのが、現状公開されているのは英語版のEnterprise Editionのみという点。といっても、インストール後に日本語言語ファイル（Multi User Interface、MUI）をWindows Update経由でインストールし、いくつかの設定を行えば日本語版とほぼ同じインターフェイスに変更できる。ということで、以下ではWindows 7 90-Day Eval VHDを日本語化する手順をメモ代わりに解説しておこう。
url: /2010/01/19/windows-7-eval-vhd-japanese/
categories:
  - Docs

---
　Microsoftが、Windows 7の90日期間限定評価版がインストールされた仮想ハードディスクイメージ（Windows 7 90-Day Eval VHD）を無償公開している。[窓の杜の記事][1]などでも紹介されているが、これは同じくMicrosoftがWindows環境向けに無償提供している[Virtual PC][2]上で利用できるもので、（期間限定、評価目的限定ではあるものの）ライセンスの問題なしにWindowsの仮想環境を構築できる。多くのソフトウェアのインストール/アンインストールを繰り返すライターや、クリーンな環境で動作確認を行いたいようなソフト開発者にとって非常に便利なソリューションだ。

<!--more-->

　ただし、注意しなければ行けないのが、現状公開されているのは英語版のEnterprise Editionのみという点。といっても、インストール後に日本語言語ファイル（Multi User Interface、MUI）をWindows Update経由でインストールし、いくつかの設定を行えば日本語版とほぼ同じインターフェイスに変更できる。ということで、以下ではWindows 7 90-Day Eval VHDを日本語化する手順をメモ代わりに解説しておこう。

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/190complete.png"><img alt="日本語化されたWindows 7 90日試用版" src="http://hylom.net/img/blog/100119/190complete_s.png" title="日本語化されたWindows 7 90日試用版" width="500" height="421" /></a>
  
  <p class="wp-caption-text">
    日本語化されたWindows 7 90日試用版
  </p>
</div>

#### Windows 7 90-Day Eval VHDのダウンロードとインストール

　まずはMicrosoftの[ダウンロードページ][3]から、Microsoft Windows 7 90-Day Eval VHDをダウンロードする。なお、ダウンロードには正規版のWindowsが必要で、ダウンロード時に認証がかかるのでIEでダウンロードするほうが良いかもしれない。また、インストーラは3ファイルに分割されていて、合計で約1.8GBと大きいので、ダウンロード時にはHDDの残量に注意。

　ダウンロード後、3つのファイルを同じフォルダに保存して「Windows7Fullx86Ent90Days.part1.exe」を実行すると「Windows7Fullx86Ent90Days」というフォルダが作成され、その中の「Virtual Hard Disks」ディレクトリ内にある「Win7ENT90DAYS.vhd」がWindows 7がインストールされた仮想ハードディスクイメージとなる。

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/010vhd.png"><img alt="Windows 7 30日評価版の仮想ハードディスクイメージ" src="http://hylom.net/img/blog/100119/010vhd_s.png" title="Windows 7 30日評価版の仮想ハードディスクイメージ" width="500" height="364" /></a>
  
  <p class="wp-caption-text">
    Windows 7 30日評価版の仮想ハードディスクイメージ
  </p>
</div>

#### Virtual PCのインストール

　続いて、Virtual PCのインストールを行う。Windows 7でVTが利用できる環境の場合は、[Windows Virtual PC][4]を、それ以外（Windows 7でVTが利用できない環境およびWindows Vista、XP）の場合、[Virtual PC 2007][5]を利用する。それぞれのインストールについては割愛（ダウンロードしてインストーラを実行するだけ）。

#### 仮想マシンの作成（Windows 7＋Windows Virtual PC環境）

　Virtual PCのインストールが終わったら、仮想マシンを作成する。以下はWindows 7＋Windows Virtual PCの場合。それ以外の場合は適当にググっていただきたい（汗）。

　Windows 7の場合、「＜ユーザーのホームディレクトリ＞\仮想マシン」というフォルダでWindows Virtual PCの操作を行う。まずはコマンドバーの「仮想マシンの作成」をクリックする。「仮想マシンを作成します」というウィザードが表示されるので、仮想マシン名とその保存先、メモリとネットワーク、仮想ハードディスクの設定を行う。マシン名は適当。メモリは1GBくらいは欲しいところ。最後の「仮想ハードディスクの追加」では、「既存の仮想ハードディスクを使用する」を選択し、「参照」をクリックしてWindows 7 90-Day Eval VHDの仮想ハードディスク（Win7ENT90DAYS.vhd）を指定する。

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/020new_vm.png"><img alt="「仮想マシンの作成」で仮想マシンを作成する" src="http://hylom.net/img/blog/100119/020new_vm_s.png" title="「仮想マシンの作成」で仮想マシンを作成する" width="500" height="101" /></a>
  
  <p class="wp-caption-text">
    「仮想マシンの作成」で仮想マシンを作成する
  </p>
</div>

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/050sel_vhd.png"><img alt="「仮想ハードディスクの追加」で「既存のハードディスクを使用する」を選択し、Windows 7のVHDファイルを選択する" src="http://hylom.net/img/blog/100119/050sel_vhd_s.png" title="「仮想ハードディスクの追加」で「既存のハードディスクを使用する」を選択し、Windows 7のVHDファイルを選択する" width="500" height="324" /></a>
  
  <p class="wp-caption-text">
    「仮想ハードディスクの追加」で「既存のハードディスクを使用する」を選択し、Windows 7のVHDファイルを選択する
  </p>
</div>

　以上で仮想マシンの作成は完了。作成された仮想マシンをダブルクリックすると、設定等に問題がなければ英語版Windows 7 Enterprise Editionが起動する。

　続いてWindows 7のセットアップを行う。始めにセットアップ画面が表示されるので、「Country or region」を「Japan」、「Time and currency」を「Japanese（Japan）」、「Keyboard layout」を「Japanese」に設定して「Next」をクリックする。なお、Virtual PCのウィンドウをクリックするとマウスポインタがVirtual PC内のWindows 7に取られてウィンドウ外に出せなくなる。ウィンドウ外にマウスポインタを出したい場合はAlt＋Tabを押せばOK。あとは通常のWindows 7のインストールと同様にセットアップを進めていく。

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/070setup.png"><img alt="セットアップ画面で「Japan」/「Japanese」を選択する" src="http://hylom.net/img/blog/100119/070setup_s.png" title="セットアップ画面で「Japan」/「Japanese」を選択する" width="500" height="407" /></a>
  
  <p class="wp-caption-text">
    セットアップ画面で「Japan」/「Japanese」を選択する
  </p>
</div>

#### 統合コンポーネントのインストール

　セットアップが完了したら、Windows Virtual PCの　「ツール」−「統合コンポーネントのインストール」を実行して統合コンポーネントをインストールしておく。これにより、Windows Virtual PC内外でマウスがシームレスに動くようになる。

<div style="width: 419px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/080inst_unity.png"><img alt="Virtual PCの「ツール」メニューから「統合コンポーネントのインストール」を選択する" src="http://hylom.net/img/blog/100119/080inst_unity_s.png" title="Virtual PCの「ツール」メニューから「統合コンポーネントのインストール」を選択する" width="409" height="201" /></a>
  
  <p class="wp-caption-text">
    Virtual PCの「ツール」メニューから「統合コンポーネントのインストール」を選択する
  </p>
</div>

　「統合コンポーネントのインストール」を選択すると確認ダイアログが表示され、「続行」をクリックすると仮想PCにインストールDVDがマウントされるので、「Run setup.exe」をクリックする。ウィザードが起動するので、「Next」をクリックしてインストールを進める。完了したら再起動。

<div style="width: 367px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/100unity_setup2.png"><img alt="仮想マシンに統合コンポーネントが含まれた仮想CDがマウントされる" src="http://hylom.net/img/blog/100119/100unity_setup2_s.png" title="仮想マシンに統合コンポーネントが含まれた仮想CDがマウントされる" width="357" height="318" /></a>
  
  <p class="wp-caption-text">
    仮想マシンに統合コンポーネントが含まれた仮想CDがマウントされる
  </p>
</div>

#### 日本語言語ファイルのインストール

　日本語言語ファイルはWindows Updateの追加コンポーネントとして用意されている。Windows Updateを起動し、「optional updates are available」をクリックすると各種言語ファイルなどが表示されるので、「Japanese Language Pack」にチェックを入れて「OK」をクリック、Windows Updateを実行する。インストールの完了後、いったん再起動。

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/120instlangpack2.png"><img alt="Windows Updateで「optional updates are available」をクリックする" src="http://hylom.net/img/blog/100119/120instlangpack2_s.png" title="Windows Updateで「optional updates are available」をクリックする" width="500" height="376" /></a>
  
  <p class="wp-caption-text">
    Windows Updateで「optional updates are available」をクリックする
  </p>
</div>

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/130instlangpack.png"><img alt="「Japanese Language Pack」にチェックを入れてインストールする" src="http://hylom.net/img/blog/100119/130instlangpack_s.png" title="「Japanese Language Pack」にチェックを入れてインストールする" width="500" height="376" /></a>
  
  <p class="wp-caption-text">
    「Japanese Language Pack」にチェックを入れてインストールする
  </p>
</div>

　再起動後、コントロールパネルの「Region and Language」で「Change display language」をクリックし、「Display language」の「Choose a display language」で「日本語」を選択、「OK」をクリックする。ここでいったんログオフが要求されるので、そのままログオフする。

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/150sel_lang.png"><img alt="「Region and Language」の「Keyboards and Languages」の「Display Language」で「日本語」を選択する" src="http://hylom.net/img/blog/100119/150sel_lang_s.png" title="「Region and Language」の「Keyboards and Languages」の「Display Language」で「日本語」を選択する" width="500" height="572" /></a>
  
  <p class="wp-caption-text">
    「Region and Language」の「Keyboards and Languages」の「Display Language」で「日本語」を選択する
  </p>
</div>

　再度ログインすると、UIが日本語化される。続いて、コントロールパネルの「地域と言語」を開き、「管理」タブで「ようこそ画面と新しいユーザーアカウント」の「設定のコピー」をクリックする。「現在のユーザー」および「ようこそ画面」、「新しいユーザーアカウント」の言語を設定するダイアログが表示されるので、ダイアログ下の「ようこそ画面とシステムアカウント」および「新しいユーザーアカウント」にチェックを入れ、「OK」をクリックする。再起動が要求されるので、そのまま再起動を実行しよう。

<div style="width: 510px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/170welcome.png"><img alt="「地域と言語」の「管理」タブで「設定のコピー」をクリックする" src="http://hylom.net/img/blog/100119/170welcome_s.png" title="「地域と言語」の「管理」タブで「設定のコピー」をクリックする" width="500" height="586" /></a>
  
  <p class="wp-caption-text">
    「地域と言語」の「管理」タブで「設定のコピー」をクリックする
  </p>
</div>

<div style="width: 492px" class="wp-caption aligncenter">
  <a href="http://hylom.net/img/blog/100119/180welcome2.png"><img alt="「現在の設定のコピー先」の両方にチェックを入れる" src="http://hylom.net/img/blog/100119/180welcome2_s.png" title="「現在の設定のコピー先」の両方にチェックを入れる" width="482" height="602" /></a>
  
  <p class="wp-caption-text">
    「現在の設定のコピー先」の両方にチェックを入れる
  </p>
</div>

　以上で日本語化が完了。日本語版Windows 7と同様のインターフェイスが利用できるようになる。90日という期間限定だが、Windows 7 Enterpriseの全機能が利用できる。

 [1]: http://www.forest.impress.co.jp/docs/news/20091015_321806.html
 [2]: http://www.microsoft.com/japan/windows/virtual-pc/
 [3]: http://www.microsoft.com/downloads/details.aspx?FamilyID=606ae07e-b7db-405b-974b-dd61fc41add4&#038;displaylang=en
 [4]: http://www.microsoft.com/japan/windows/virtual-pc/download.aspx
 [5]: http://www.microsoft.com/downloads/details.aspx?familyid=04D26402-3199-48A3-AFA2-2DC0B40A73B6&#038;displaylang=ja
