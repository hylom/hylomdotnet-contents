---
slug: create-custom-component-with-web-components-and-svg
title: SVG＋Web Componentsで再利用可能なGUIコンポーネントを作る
tag: [ web, html5 ]
date: 2020-12-06T22:30:00+09:00
lastmod: 2020-12-06T22:30:00+09:00
publishDate: 2020-12-06T22:30:00+09:00
---

昨今のWeb開発の現場では、Vue.jsやReactといったページ内の要素をコンポーネント化して再利用しやすくするフレームワークが多く利用されています。しかし、これらのフレームワークのコンポーネントは相互運用性がありません。たとえばVue.js向けに作ったコンポーネントはReactでは利用できませんし、その逆も同様です。

一方で、特に外部のフレームワークなどを利用せずに、JavaScriptだけで自作のコンポーネントを作成できる「[Web Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components)」という技術もあります。Web ComponentではVue.jsやReactのような、DOMとデータの高度な紐づけ機能は提供されませんが、データをビジュアライズするだけであれば十分な機能を備えています。さらに、Web Componentsで作成したコンポーネントはVue.jsやReactでも使えます。

ということで、Web ComponentsとSVGを使って、ダイアル型のメーター（名前は「dial-meter」）というUIコンポーネントを作成してみました。ソースは[GitHubのhylom/web-component-demoリポジトリ](https://github.com/hylom/web-component-demo)で公開しています。[シンプルなデモページ](https://hylom.github.io/web-component-demo/)も用意しました。

## Web Componentsの概要と情報源

Web Componentsを利用すると、次のような手順で独自のタグ（カスタム要素）を実装できます。

 1. `HTMLElement`クラスを継承したクラスを定義する
 2. 定義するタグ名を第1引数、紐付けるクラス（1.で定義したクラス）を第2引数として与えて`customElements.define()`メソッドを実行する

たとえば`<dial-meter>`というカスタム要素を実装する場合、まず`HTMLElement`を継承した`DialMeter`というクラスを作成し、`customElements.define('dial-meter', DialMeter)`を実行して登録します。

```
class DialMeter extends HTMLElement {
  constructor() {
    super();
  }
}
customElements.define("dial-meter", DialMeter);
```

このJavaScriptコードをWebブラウザ内で実行すると、`<dial-meter>`という要素がページ内で利用できるようになります。

Web Componentsについて詳しくはMDNの「[Web Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components)」ドキュメントに一通りの基本的な内容がまとめられているので、本記事では基本的な解説はそちらに譲り、ハマったところ、注意点などについて簡単にまとめておきます。

## 既存の要素を拡張して独自コンポーネントを作ることはできない

Web Componentsでは、完全に新たなHTML要素を実装するだけでなく、既存のHTML要素を拡張する（機能を追加する）という機能も提供されています。この場合、拡張したいHTML要素に対応するクラスを継承したクラスを作成し、さらに`customElements.define()`の第3引数として`{ extends: ＜要素名＞ }`というオブジェクトを与えます。

たとえば`<div>`要素を拡張した`my-new-element`という要素を作成する場合なら、`HTMLDivElement`を継承した`MyNewElement`クラスを作成し、次のように`customElements.define()`を実行します。

```
customElements.define(`my-new-element`, MyNewElement, { extends: 'div' });
```

このようにして定義したカスタム要素は、拡張元の要素に「is」属性を付与した要素を作成することでドキュメント内で利用できます。

```
<div is="my-new-element"></div>
```

一方で、このようにして定義したコンポーネントは`<my-new-element></my-new-element>`のような形では利用できません。

## 作成するコンポーネント名には必ず「-」が含まれている必要がある

既存のHTMLタグとの競合を回避するため、作成するコンポーネントの名前には必ず「-」が含まれている必要があります。

## shadow DOMのルート要素として挿入できる要素の制約

Web Componentsでは、shadow DOMというドキュメントとは隔離されたDOMを使って要素をコンポーネント化します。たとえばこのshadow DOM内に`<div>`要素を挿入する場合、次のような処理を行います。

```
const shadow = this.attachShadow({mode: 'open'});

const div = document.createElement('div');
shadow.appendChild(div);
```

このようにして作成したshadow DOMは、ドキュメント内でそのカスタム要素が存在する位置にアタッチされるのですが、一方でshadow DOMのルート要素直下に挿入できる子要素には制約があり、`<div>`や`<p>`など、限られたものしか挿入できません。

利用できる要素は[MDNのドキュメント](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)に記載されていますが、たとえば`<img>`や`<svg>`タグは許可されていません。ただし、この制約はあくまでshadow DOMのルート要素直下にのみ適用されるため、shadow DOMのルート要素直下に`<div>`要素を挿入すれば、その`<div>`要素内には任意の要素を挿入できます。

今回作成したカスタム要素は`<svg>`要素を使ってUIを作成しているので、shadow DOMのルート直下には`<div>`を挿入して使用しています。

## 属性へのアクセス

Web Componentsで実装したカスタム要素は、DOM上では`customElements.define()`メソッドに与えたクラスのインスタンスになります。たとえば今回の例では、`<dial-meter>`要素は`DialMeter`クラスのインスタンスとなります。このとき、`<dial-meter>`に与えた属性は、`DialMeter`クラス内からは`this.getAttribute()`を使ってアクセスできます。

たとえば、`<dial-meter value="100">`のように記述した場合、この`value`属性の値は`this.getAttribute('value')`のようにして取得できます。

一方で、クラス内で毎回`getAttribute()`を使用するのはやや面倒です。そのため、クラス内から頻繁にアクセスする属性については次のようにgetter/setterを定義すると直感的にアクセスできるようになります。

```
get value() {
  return this.getAttribute('value');
}

set value(val) {
  this.setAttribute('value', val);
}
```

## 属性が変更された場合の対応

Web Components技術を使って実装されたカスタム要素は、一般的なHTML要素と同様に扱えます。つまり、`createElement()`で新規作成して`appendChild()`や`append()`、`prepend()`といったメソッドで追加したり、`replaceChildren()`で削除したり、DOM経由で属性を操作する、といった操作が行えます。こういった操作が行われた際には、カスタム要素に紐づけられたクラスの次のメソッドが実行されます。

 * カスタム要素がノードに追加された場合：`connectedCallback()`
 * カスタム要素がノードから削除された場合：`disconnectedCallback()`
 * カスタム要素が移動された場合：`adoptedCallback()`
 * カスタム要素の属性値が変化した場合：`attributeChangedCallback()`

なお、属性値に関してはあらかじめ`observedAttributes()`メソッドを定義し、このメソッドの戻り値で監視する属性名の配列を返すよう実装しておく必要があります。

たとえば「value」および「class」、「style」属性が変化したときに`attributeChangedCallback()`が呼び出されるようにする場合、次のように`observedAttributes()`メソッドを定義しておきます。

```
static get observedAttributes() {
  return ['value', 'class', 'style'];
}
```

また、`connectedCallback()`および`disconnectedCallback()`、`adoptedCallback()`には引数が渡されませんが、`attributeChangedCallback()`には次のように3つの引数が与えられます。

```
attributeChangedCallback(name, oldValue, newValue)
```

ここで`name`は変化した属性名、`oldValue`は変化前の値、`newValue`は変化後の値です。

## DOMとカスタム要素の構築タイミング

HTML内にカスタム要素を記述していた場合、`connectedCallback()`はそのカスタム要素のタグがパースされたタイミング（`DOMContentLoaded`イベントの発生前）に実行されます。

また、属性が指定されていた場合、まず`attributeChangedCallback()`が実行され、続いて`connectedCallback()`が実行されます。

DOMの構築後に`customElements.define()`でカスタム要素が登録された場合、そのタイミングで`attributeChangedCallback()`や`connectedCallback()`が実行されます。

## shadow DOM内の要素に適用されるスタイルシートの定義

Shadow DOM内に、適用したいCSSを`textContent`として持つ`<style>`要素を挿入することでスタイルシートを適用できます。

```
const style = document.createElement('style');
style.textContent = `＜適用したいCSS＞`;
shadow.appendChild(style);
```

`<link>`要素を挿入して外部のスタイルシートを読み込ませることも可能です。

```
const link = document.createElement('link');
link.setAttribute('rel', 'stylesheet');
link.setAttribute('href', '＜CSSファイルのURL＞');
shadow.appendChild(link);
```

## カスタム要素自体のstyleを指定する

上記の方法で読み込ませたスタイルシート中では、いくつか特殊な擬似クラスが利用できます。

 * `:host`：そのカスタム要素自体（shadow DOMのroot）のスタイル
 * `:host()`：引数で指定したセレクタがそのカスタム要素に適用されているに適用されるスタイル。たとえば`:host(.foo)`とすると、そのカスタム要素に「foo」と言うクラスが指定されていた場合のみに指定したクラスが適用される
  * `:host-content()`：引数で指定したセレクタに合致する要素内にそのカスタム要素が存在する場合に適用されるスタイル。たとえば`:host-content(h1)`とすると、h1要素の中に存在するそのカスタム要素のみに指定したスタイルが適用される。
  
ただし、`:host-content()`は現状Chrome系ブラウザでのみサポートされているようです。

また、Web Componentsに関連する擬似要素として、`:defined`と`::part()`の2つがあります。

まず`:defined`ですが、これはそのカスタム要素が定義されている（`customElements.define()`で定義されている）場合のみ適用されるスタイルを指定するものです。たとえば次のコードは`foo-bar`と言うカスタム要素が`customElements.define()`で定義されている場合にインライン要素として表示し、そうでない場合は非表示にすると言うものです。

```
foo-bar:not(:defined) {
  display: none;
}

foo-bar:defined {
  display: inline;
}
```

`::part()`は、：カスタム要素のshadow DOM内で`part`属性が指定されている要素を対象として選択するものです。たとえば`foo-bar`カスタム要素のshadow DOM内に`part="hoge"`と言う属性が指定された要素が存在する場合、次のようにしてその属性のみを対象にスタイルを適用できます。

```
foo-bar::part(hoge) {
  ...
}
```

shadow DOM内の要素は通常は外部のスタイルシートの影響を受けませんが、`part`属性とこの`::part()`セレクタを組み合わせることで、一部の要素のみ外部のスタイルシートでスタイルを変更できるようにすることが可能になります。

## スロット

shadow DOM内に`<slot name="＜スロット名＞">`と言う要素を挿入すると、この要素はそのカスタム要素内に囲まれた要素で、かつ`slot="＜スロット名＞"`という属性が指定された要素に置き換えられます。

たとえば`foo-bar`というカスタム要素のshadow DOMが次のようになっていたとします。

```
<p><slot name="hoge">blah blah blah</slot></p>
```

このとき、`<foo-bar>`カスタム要素を次のようにマークアップしてみます。

```
<foo-bar><i slot="hoge">wryyy</i></foo-bar>
```

すると、表示されるshadow DOMは次のように`<slot name="hoge">`要素が`<i slot="hoge">`要素に置き換えられたものになります。

```
<p><i>wryyy</i></p>
```

なお、`name`属性を指定せずに`<slot>`要素を使用すると、この`<slot>`要素はカスタム要素内の最初の子要素に置き換えられます。

## SVGの要素をSVGタグ内に挿入する

HTML内に直接`<svg>`要素を書く場合にはあまり意識しませんが、実は`<svg>`要素やその子要素として指定する`<path>`や`<circle>`といった要素は、HTMLの要素ではありません。そのため、`document.createElement()`メソッドでは作成できず、代わりに`document.createElementNS()`メソッドを使用して作成します。このメソッドは第1引数としてネームスペースを指定する必要があり、`<svg>`要素やその子要素を作成する場合には`http://www.w3.org/2000/svg`と言うネームスペースを指定します。

```
this._svg = document.createElementNS(`http://www.w3.org/2000/svg`, "svg");
```



