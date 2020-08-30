---
slug: google-adsense-fake-phishing-site
title: Google Adsense/Adwords公式サイトのように偽装したフィッシングサイトにご注意を
tag: [ security ]
date: 2017-10-06T17:45:26+09:00
lastmod: 2017-10-06T18:03:05+09:00
publishDate: 2017-10-06T17:45:26+09:00
---

　Google Adsenseの管理画面にログインしようとしたところ、あやうくフィッシングサイトに引っかかりそうになったので注意喚起。

　Google検索で、「google adsense」と検索すると「google.com - Log In - Sign Up」という広告が出ました。「広告」という表示とともに、ドメインとして「adwords.google.com」が表示されているので、これだけを見るとGoogleによる正規の広告のように見えます（なお、現時点では対処されたのかすでに表示されなくなっています）。

<blockquote class="twitter-tweet" data-lang="en"><p lang="ja" dir="ltr">Googleに見せかけたフィッシングサイトに引っかかりそうになったので注意喚起。「google adsense」でググるとトップにURLとして「adwords.google.com」ドメインが表示された広告が出るが、これがフィッシングサイトへの誘導になっている（続く） <a href="https://t.co/97esL2inYC">pic.twitter.com/97esL2inYC</a></p>&mdash; hylom (@hylom) <a href="https://twitter.com/hylom/status/916235929236389890?ref_src=twsrc%5Etfw">October 6, 2017</a></blockquote>

　ところが、この広告をクリックすると「adwords-google-website.com」というドメインのサイトに飛ばされます。このサイトやログイン画面はGoogleのものに似ていますが、よく見るとSSL接続ではありませんし、サインイン画面も非SSL接続。Googleでこれはあり得ません。

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="ja" dir="ltr">この広告をクリックすると、「adwords-google-website.com」」というドメインのサイトに飛ばされる。ここでSIGN INをクリックするとおなじみサインインページが表示されるのだが、サインイン画面にも関わらずSSL接続ではない（これで気付いた）。（続く） <a href="https://t.co/S7RyC9IZUv">pic.twitter.com/S7RyC9IZUv</a></p>&mdash; hylom (@hylom) <a href="https://twitter.com/hylom/status/916236736123899905?ref_src=twsrc%5Etfw">October 6, 2017</a></blockquote>

　このサイトのドメイン情報をWHOISで調べて見ると、登録者組織は記入されておらず、連絡先メールもyandex.comドメイン。Googleとは関係なさそうです。

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="ja" dir="ltr">このドメイン「adwords-google-website.com」をWHOISで調べると、連絡先はなぜかyandex.comドメインでどう見てもGoogleとは関係なさそう。ということでフィッシングサイトだと思われます。 <a href="https://t.co/8XFJZ6pQHF">pic.twitter.com/8XFJZ6pQHF</a></p>&mdash; hylom (@hylom) <a href="https://twitter.com/hylom/status/916237133991493632?ref_src=twsrc%5Etfw">October 6, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

　[はてなブックマークコメント](http://b.hatena.ne.jp/entry/enkaism.hatenadiary.jp/entry/2017/10/02/230602)によると、どうもAdWordsでは表示するURLを任意に指定できてしまうようです。

　また、このサイトにメールアドレスとパスワードを入力すると、それに加えて登録している電話番号の入力も求められます（架空のアカウント情報を使って検証しています）。

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="ja" dir="ltr">ちなみに、このフィッシングサイトのログイン画面にメールアドレス/パスワードを入力すると、Googleアカウントに登録している電話番号を入力するよう求められます（架空のアドレスで試しております）。番号を入力すると正規サイトにリダイレクトされる模様。 <a href="https://t.co/mhPHIuy0dH">pic.twitter.com/mhPHIuy0dH</a></p>&mdash; hylom (@hylom) <a href="https://twitter.com/hylom/status/916240698424225792?ref_src=twsrc%5Etfw">October 6, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ということで、皆様ご注意ください。AdSenseの管理画面をブックマークしておらず、毎回ググってログインしようとしていると引っかかってしまいますよ……。
