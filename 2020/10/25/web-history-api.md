---
slug: web-history-api-guide
title: WebブラウザのHistory APIの挙動を知ろう
tag: [ web, api ]
date: 2020-10-25T20:00:00+09:00
lastmod: 2020-10-25T20:00:00+09:00
publishDate: 2020-10-25T20:00:00+09:00
---

仕事でWebブラウザのHistory APIに関する質問を受けたのですが、意外と分かりにくいのでここでまとめておきます。

なお、History APIに関する大体のことはMDNの[History API を取り扱う](https://developer.mozilla.org/ja/docs/Web/API/History_API/Working_with_the_History_API)というドキュメントにまとめられていますので、こちらも参照しましょう。

### 履歴とは

Webブラウザ上では、閲覧履歴はスタック（本記事では「履歴スタック」と呼ぶ）として管理されます。履歴スタックはWebブラウザのウィンドウやタブごとに用意されています。ページの進む/戻る操作ではこの履歴スタック自体は変更されず、履歴スタック上の現在位置のみが変更されます。

Aタグなどであるページから別のページに遷移した場合、履歴スタック上の現在位置よりも先にある履歴項目が削除され、続いて履歴スタックの先頭ににそのURLを含む新たな履歴項目が追加されます。

<img src="/img/blog/2020/10/history_stack.png" width="500" height="300" alt="履歴スタックのイメージ">

### History APIとは

History APIは、履歴スタックを操作するインターフェイスです（[MDNのドキュメント](https://developer.mozilla.org/ja/docs/Web/API/History)）。履歴上で前に閲覧したページに戻ったり、戻った後に再度元のページに戻る、といった操作が可能です。ただし、Webブラウザの閲覧履歴はプライバシに関わるものとされるため、閲覧履歴のURLやタイトルなどへのアクセスはできません。

Webブラウザ上では、`window.history`がHistoryインターフェイスを実装したオブジェクトになっています。


### History APIの使用例1：前のページに戻る/次のページに進む

History APIでよく使われ、かつ理解しやすい使用例として、前のページに戻ったり、次のページに進む、というものがあります。これは、`history.back()`および`history.forward()`メソッドで実行できます。

`history.back()`は、Webブラウザの「前に戻る」ボタンを押した場合と同じ挙動を実行します。また、`history.forward()`は「次に進む」ボタンを押した場合と同じ挙動を実行します。

「2つ前に戻る」「3つ先に進む」といった操作を行える`history.go()`メソッドも用意されています。先に進む場合は正の数、前に戻る場合は負の数でいくつ進む/戻るかを指定します。たとえば`history.go(1)`は`history.forward()`と、`history.go(-1)`は`history.back()`と同じです。引数が指定されていない場合は、現在のページをリロードします。

`history.length`は履歴スタック上にいくつの項目（履歴）が存在しているかを示す値です。ただし、現在表示されているページが履歴スタック上のどの位置にあるかを知ることはできません。そのため、あまりこのプロパティのユースケースはないと思います。

### History APIの使用例2：ブラウザのURLバーに表示されているURLを操作する

History APIでは、履歴だけでなくWebブラウザのURLバーに現在表示されているURLの操作を行うAPIも提供されています。[history.replaceState()](https://developer.mozilla.org/ja/docs/Web/API/History/replaceState)がそのメソッドです。

たとえば、URLバーに表示されているURLを「＜現在表示しているWebページのドメイン＞/foo/bar」に書き換えるには、次のように実行します。

```
window.history.replaceState(null, "", "/foo/bar");
```

クエリパラメータやハッシュを指定することも可能です。たとえば次のように実行すると、URLバーの表示内容は「＜現在表示しているWebページのドメイン＞/foo/bar?hoge=1#baz」になります。

```
window.history.replaceState(null, "", "/foo/bar?hoge=1#baz")
```

こういった操作は、JavaScriptを使って動的にページのコンテンツを変更するようなWebサイトで、現在の状態に特定のURLでアクセスさせたい（いわゆるパーマリンク、Permalinkを生成したい）場合に利用できます。

### History APIの使用例3：新たな履歴を生成することなしにページ遷移を行う

さて、この`history.replaceState()`メソッドを実行すると、URLバーの表示内容が変わり、また`window.location.href`の値も指定したURLに変化します。一方でページの読み込みは行われず、また`history.length`の値も変化しません。これを利用し、ページをリロードする`history.go(0)`と組み合わせることで、新たな履歴を生成することなしにページ遷移を発生させることができます。

```
window.history.replaceState(null, "", "＜遷移したいパス＞");
window.history.go(0);
```

この場合、たとえば実行前の`history.length`が1なら、実行後も`history.length`は1のままです。

### History APIの使用例4：ページ遷移なしに新たな履歴を生成する

History APIでは、逆にページ遷移なしに新たな履歴を生成することもできます。そのためのメソッドが、[history.pushState()](https://developer.mozilla.org/ja/docs/Web/API/History/pushState)です。

たとえば次のように実行すると、履歴スタックの先頭に「＜現在指定しているWebページのドメイン＞/hoge」というURLが追加されます。

```
window.history.pushState(null, "", "/hoge");
```

このとき、URLバーの表示内容は「＜現在指定しているWebページのドメイン＞/hoge」になります。`window.location.href`もこの値になります。`pushState()`実行前に表示されているページが履歴スタック上の先頭であれば、`history.length`は1増えます。ただし、実際のページ遷移（ページの読み込み処理）は実行されません。

この状態でブラウザの戻るボタンを押したり、`history.back()`もしくは`history.go(-1)`を実行すると、URLバーの表示内容や`window.location.href`の内容は`pushState()`実行前のものに戻ります。ただし、その場合も実際のページ遷移（ページの再読み込み）は発生しません。

### History APIの使用例5：実際にページ遷移が発生しない戻る/進む操作を検出する

前項で説明したように、`history.pushState()`で履歴を生成した後に戻るボタンを押したり`history.back()`もしくは`history.go(-1)`を実行すると、履歴スタック上の現在位置は変化しますが、ページ遷移は発生しません。こういったページ遷移なしの戻る/進む操作は、`window`の`popstate`イベントで検出できます。

たとえば次のように`popstate`イベントに対するイベントハンドラを設定しておくと、ページ遷移なしの戻る/進む操作が発生した際にConsoleにそのイベント内容が出力されます。

```
window.addEventListener("popstate", (e) => console.log(e));
```

### History APIの使用例6：履歴スタック上の履歴項目に任意の情報を紐付ける

`history.replaceState()`や`history.pushState()`では、第1引数として`null`や任意のオブジェクトを与えることができます。このオブジェクトは、`replaceState()`の場合履歴スタック上の現在位置にある履歴項目内に、`pushState()`の場合は新しく生成された履歴項目内に格納されます。

履歴スタック上の現在位置にある履歴項目内に格納されたオブジェクトは、`history.state`プロパティとして参照できます。

たとえば、あるページを表示している状態で、次のように`history.replaceState()`で`state`オブジェクトとして`{foo: 1}`を設定します。

```
window.history.replaceState({foo: 1}, "");
```

この状態で`history.state`を確認すると、指定したオブジェクトが格納されていることが分かります。

```
> history.state
{foo: 1}
```

その後、Aタグなどで別ページに遷移すると、`history.state`の値は別のものに変わります。

```
> history.state
null
```

別ページへの遷移後、戻るボタンや`history.back()`などで元のページに戻ると、`history.state`の値はそのページに紐づけたものに戻ります。

```
> history.state
{foo: 1}
```

なお、この`history.state`は前述の`popstate`イベントのイベントハンドラに渡される[PopStateEvent](https://developer.mozilla.org/en-US/docs/Web/API/PopStateEvent)の`state`プロパティとしても参照できます。


### 備考：履歴スタックが更新される条件

原則として、History APIを使用せずにページのURL（`window.location.href`）が変更されると、必ず履歴スタックは更新されます。たとえば`<a href="#hoge">`のようなハッシュのみを指定したAタグをクリックした場合、ページのロードは発生しませんが、履歴スタックは更新され、もし現在の履歴スタック上の位置が先頭だった場合、新たな履歴がスタックに追加され、`history.length`は1増えます。
