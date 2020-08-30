---
title: コンテンツのロードを高速化するHTML5の「link prefetching」機能
author: hylom
type: post
date: 2010-06-03T03:42:08+00:00
url: /2010/06/03/html5_link_prefetch/
category:
  - Docs
tags:
  - html5
  - tuning

---
　[keyboardy][1]によると、HTML5にはlink prefetching機能があり、指定したコンテンツをあらかじめfetchしておく機能があるそうだ。

　fetchするコンテンツはLINKタグで指定する。たとえば、次のようなLINK要素をHTML内に記述しておくと、ロード時に「page2.html」がfetchされる。

<pre>&lt;link rel="next" href="page2.html"&gt;
</pre>

　また、次のように明示的にprefetchを指定することもできる。

<pre>&lt;link rel="prefetch" href="/img/img.jpg"&gt;
</pre>

　この機能はすでにFirefoxでは実装済みで、OperaやChrome、Safariでもすぐにサポートされるのでは、とのこと。Internet Explorerでは2020年代まで利用できないかも;-) だそうだ。

　ちなみに[Mozillaのlink prefetchingに関するドキュメント][2]によると、HTTPヘッダーでも次のようにしてprefetchするコンテンツを指定できる。

<pre>Link: &lt;/images/big.jpeg&gt;; rel=prefetch
</pre>

　さらに、METAタグでも指定できる。

<pre>&lt;meta http-equiv="Link" content="&lt;/images/big.jpeg&gt;; rel=prefetch"&gt;
</pre>

　また、 Firefoxの場合、http://で始まるURLのみに対応し、https://はセキュリティ関連の理由のためprefetchされない。また、FTPなどもprefetch対象外。prefetchはブラウザがidle状態で、たとえばコンテンツのローディングやダウンロードが行われている間は行われないそうだ。あとはユーザー設定でFirefoxのprefetchを無効にできるとか、prefetchリクエストは「X-moz: prefetch」ヘッダー付きで送信されるとか色々あるが、その辺は上記のドキュメントを参照。

 [1]: http://keyboardy.com/programming/html5-link-prefetching/
 [2]: https://developer.mozilla.org/en/link_prefetching_faq
