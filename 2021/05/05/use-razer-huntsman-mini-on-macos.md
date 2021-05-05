---
slug: use-razer-huntsman-mini-on-macos
title: テンキーレスミニキーボード「Razer HUNTSMAN MINI」をmacOSで使う
tag: [ keyboard, macos, emacs ]
date: 2021-05-05T16:00:00+09:00
lastmod: 2021-05-05T16:00:00+09:00
publishDate: 2021-05-05T16:00:00+09:00
---

　長年仕事用キーボードとしてHappy Hacking Keyboard（HHKB）Lite 2を使っていたのですが、だいぶタッチが渋くなっていること、そしてこの製品がすでに廃盤になっていることから将来的なmacOSサポートが期待できない点を考慮して、代替品としてRazerの[HUNTSMAN MINI](https://www2.razer.com/jp-jp/store/razer-huntsman-mini)という製品を導入してみました。テンキーレスのコンパクトサイズキーボードの選択肢はあまり多くはないのですが、HUNTSMAN MINIでは日本語配列モデルも提供されており、かつキー配列的にも素直な感じです。macOSのでは英数キーとかなキーで日本語入力のON/OFFを切り替えるため、スペースバーが長かったりすると違和感を感じるのですが、本製品はスペースバーの幅がAppleの純正キーボードとほぼ同じなのが決め手でした。

![Apple純正キーボードとHUNTSMAN MINIの比較](/2021/05/05/razer_vs_apple.jpeg "Apple純正キーボードとHUNTSMAN MINIの比較")

　HHKB Lite2と比較すると、サイズ的にはほぼ同じです。スペースキーが若干長く、また矢印キーがない点が大きな違いです。

![HHKB Lite2とHUNTSMAN MINIの比較](/2021/05/05/hhkb_vs_razer.jpeg "HHKB Lite2とHUNTSMAN MINIの比較")

　このキーボードは一般的なWindowsキーボードと同様、最上段の「1」キーの左には半角/全角キーがり、また「A」キーの左はCaps Lockキーがあるのですが、これらは純正のキー配列カスタマイズツールで変更可能で、かつ変更した内容はキーボード自体に保存されます。ただ、このカスタマイズツールは現状Windows版しか提供されていません。以前はmacOS版も提供されていたのですが、数年前にリリースされた最新バージョンからはmacOSのサポートが廃止されたようです。そのためキー配列のカスタマイズにはWindowsマシンが必要ですが、一度設定さえしてしまえば、Macでも特別なドライバなしで同じキー配列で利用可能です。

![設定ツールRazer Synapse 3](/2021/05/05/synapse.png "設定ツールRazer Synapse 3")

　ただし、このカスタマイズツールではWindowsキーに関してはカスタマイズできず、また無変換キーや変換キーをmacOSで使われる英数キーやかなキーに割り当てることもできません。WindowsキーについてはmacOSではCommandキー、AltキーはOptionキーとして認識されるのですが、Apple純正キーボードではこれらがちょうど逆の位置にあります。これについてはmacOS側で入れ替えを行うことができるので、そちらで対応可能です。また、英数キーやかなキーが使えない問題は、無変換キーにCtrl＋Shift＋:、変換キーにCtrl＋Shift＋Jというショートカットキーを割り当てることで一般的には対応が可能です（参考資料：[Macの日本語入力ソースを設定する/切り替える]((/2021/05/05/karabiner.png "Karabiner Elementsを導入する"))）。

![macOSのキーボード設定](/2021/05/05/macos_keyboard_config.png "macOSのキーボード設定")

## Karabiner Elementsを導入する

　ひとまずはこの設定で利用していたのですが、なんとEmacsではCtrl＋Shift＋:やCtrl＋Shift＋Jというショートカットキーを使えない（Emacsのショートカットキーとして認識されてしまう）ことが判明。一応Emacs側で無理やりシステムイベントを発生させることで対応は可能ではあるのですが（参考資料：[OSXにおけるIMEの変更 #10](https://github.com/emacs-jp/issues/issues/10)）、これは内部でコマンドを実行している関係で微妙に切り替えにタイムラグが発生するため、頻繁に入力モードの切り替えを行う使い方には向いていないと感じました。

　ということで、最終的にはmacOSでWindows向けキーボードを使う際の定番ツールである[Karabiner-Elements](https://karabiner-elements.pqrs.org/)を導入して無変換キーを英数キーに、変換キーをかなキーに割り当てることにしました。Karabiner-Elementsを使うとmacOS標準設定でのCommandキーとOptionキーの入れ替えが効かなくなるようなので、その設定もKarabiner-Elements側で行なっています。

![Karabiner-Elementsの設定](/2021/05/05/karabiner.png "Karabiner-Elementsの設定")

　このように設定関係で紆余曲折はありますが、Razer HUNTSMAN MINIはキーボードとしての機能自体はよくできており、キータッチにも不満はありません。有線キーボードではありますが、お値段的にはHHKBと比べて1.5〜2万円ほどお安いので、キーボードに3万円近く出すのはちょっと……という方にはおすすめです。
