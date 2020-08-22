---
slug: read-ecmascript2015-specification-part2
title: ECMAScript 2015の仕様書を読む（その2）
tags: [ ecmascript, javascipt ]
date: 2016-03-09T00:39:25+09:00
lastmod: 2016-03-09T00:40:58+09:00
publishDate: 2016-03-09T00:39:25+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)）を読んでいます。今回は第10章と第11章。第11章ではECMAScript 2015で追加されたテンプレートリテラルについての記述があるほか、細かいコード表記ルールが記載されているので目を通しておくと良い。

## 第10章


　ECMAScriptのソースコードについて。ソースコードはUnicodeで記述する。Unicodeではさまざまな符号化形式（UTF-8やUTF-16など）があるが、これについては規格では言及されていない。

　ECMAScriptコードが「use strict」ディレクティブで始まると、そのコードはStrictモードコードとして解釈される。また、モジュールコードやクラス宣言などもstrictモードのコードとなる。そのほか、一定の条件を満たすコードはstrictモードのコードとなる。それ以外のコードは非strictモードのコードとなる。

## 第11章


　ECMAScriptの文法について。

 - タブやVT、FF、スペースなどはすべてホワイトスペースとして扱われる。
 - CR、LF、LS、PSが改行として扱われる。CRとLFが続いた場合、単一の改行として扱われる。
 - コメントには複数行コメント（「/*」から「*/」で囲まれた部分）と単一行コメント（「//」から行末まで）がある
 - 「識別子」（変数名やメソッド名）は「ID_Start」プロパティを持つ任意のUnicode文字、「$」、「_」、「\」＋Unicodeのエスケープシーケンスから始まる必要がある。また、利用できる文字は「ID_Continue」プロパティを持つ任意のUnicode文字と「$」、「_」、「\」＋Unicodeのエスケープシーケンス、<ZWNJ>（ZERO WIDTH NON-JOINNER、U+200C）、<ZWJ>（ZERO WIDTH JOINNER、U+200D）。

　ECMAScriptには予約語があり、これらを識別子として使うことはできない。予約語一覧は以下のとおり。

```
break do in typeof
case else instanceof var
catch export new void
class extends return while
const finally super with
continue for switch yield
debugger function this
default if throw
delete import try
```

　また、次の2つは将来のための予約語（Future Reserved Words）とされており、こちらも利用できない。

```
enum await
```

　そのほか、strictモードでは下記も予約語とされている。

```
implements package protected
interface private public
```

　そのほか、「null」や「true」「false」も利用できない。

　数値リテラルについては、整数、小数、「e」や「E」を使った10のn乗表記、「0B」「0b」を使った二進数表記、「0o」「0O」を使った8進数表記、「0x」「0X」を使った16進数表記が可能。16進数表記では大文字/小文字の両方が利用可能。

　「"」もしくは「'」で囲んだ文字列は文字列リテラルとなる。どちらも改行を含むことはできない。また、「\」に続く文字はエスケープシーケンスとなる。複数行で記述したい場合、「\」＋改行を使う。また、エスケープシーケンスとしては「\'」「\"」「\\」「\b」「\f」「\n」「\r」「\t」「\v」と「\＜数値＞」、「\x＜16進数＞」、「\uXXXX」、「\u{XXXX}」が利用できる（XXXXは16進数4文字）。

　「/＜正規表現＞/＜フラグ＞」という文字列は正規表現リテラルとなる。正規表現内では「\」、「/」、「[」は使えない。また、正規表現の1文字目に「*」は使えない。改行も使えない。これらを使いたい場合は代わりにエスケープシーケンスを使う。

　「`」で囲まれた文字列はテンプレートリテラルとなる。この機能はES6で新たに実装されたもの。文字列リテラルと異なり、改行を含むことが可能。このとき、CRLF（\r\n）やCR（\r）はLF（\n）に変換される。また、エスケープシーケンスのほか、「${」と「}」でコードを囲むことでその値を文字列に取り込むことができる。

　ECMAScript処理系は必要に応じて自動的にセミコロンを挿入する。自動セミコロン挿入には3つの基本ルールがある。これは積極的に使うべきではないので説明は割愛。

