---
slug: read-ecmascript2015-specification-part12
title: ECMAScript 2015の仕様書を読む（その12）
tags: [ ecmascript,javascript ]
date: 2016-05-03T00:59:30+09:00
lastmod: 2016-05-03T00:59:30+09:00
publishDate: 2016-05-03T00:59:30+09:00
---

　ECMAScript 2015の仕様書（[ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.html)）を読んでいます。今回はNumber、Math、Dateオブジェクトについて解説する第20章のうち、Dateオブジェクトについて。

## 第20章3節


　ECMAScriptでは基準時刻（UTC1970年1月1日）からのミリ秒で時刻を表現する。表現できるのはこの基準時刻±9,007,199,254,740,992（2の53乗）ミリ秒であり、これはおよそ±28万5,616年に相当する。ただし、実際にDateオブジェクトで扱えるのは1970年1月1日正午から±1億日（±8,640,000,000,000,000ミリ秒）。

　なお、1日は8640万ミリ秒。また、閏秒は考慮されないが、閏年は考慮される。月については0〜11（0が1月）の値で表現されるが、日は1〜31の値で表現される。曜日は0〜6（0が日曜日）。そのほか、ECMAScript処理系はタイムゾーンの処理や夏時間なども考慮する。

　ECMAScriptはISO 8601 Extended Formatベースのフォーマット仕様（YYYY-MM-DDTHH:mm:ss.sssZ）をサポートする。なお、年については最大6桁（および±）での表現が可能。

　Dateオブジェクトは、基準時刻からのミリ秒をそのオブジェクトの値として格納する。また、Dateオブジェクトのコンストラクタは内部オブジェクトになっている。このコンストラクタはサブクラス化が可能だが、その場合superキーワードを使ってDataコンストラクタをコンストラクタ内で呼び出す必要がある。

　デフォルトのDateコンストラクタは3つのパターンがある。どの場合もnewキーワードなしで呼ばれた場合、いかなる引数が与えられていても現在時刻に相当する文字列を返す。

　2つ以上の引数を取るケースは以下。この場合、引数で指定した日付時刻に相当するDateオブジェクトを返す。また、引数にNaNがあると「不正な時刻」に相当するDateオブジェクトを返す。

```
Date(year, month [, date [, hours [, minutes [, seconds [, ms]]]]])
```

　1つの引数を与えた場合、引数として与えられたオブジェクトが日付時刻値を格納していた場合はその日付時刻に相当するDateオブジェクトを、もし引数が文字列であり、かつ日付時刻としてパースできる場合はその日付時刻に相当するDatetオブジェクトを、そうでない場合は引数を数値に変換し、基準時刻にその数値を足した日付時刻に相当するDateオブジェクトを返す。

　引数が与えられなかった場合、現在の日付時刻に相当するDateオブジェクトを返す。

　Dateオブジェクトは次のメソッドを持つ。

```
Date.now()	基準時刻から現在時刻までの経過ミリ秒を返す
Date.parse(string)	引数を文字列としてパースし、基準時刻からその時刻までの経過ミリ秒を返す
```

　また、Dateオブジェクトのprototypeオブジェクトは下記のメソッド/プロパティを持つ。

```
Date.prototype.constructor	コンストラクタ
Date.prototype.getDate()	そのオブジェクトの日にちを返す（下記、同様）
Date.prototype.getDay()	
Date.prototype.getFullYear()	
Date.prototype.getHours()	
Date.prototype.getMilliseconds()	
Date.prototype.getMinutes()	
Date.prototype.getMonth	
Date.prototype.getSeconds()	
Date.prototype.getTime()	基準時刻からの経過ミリ秒を返す
Date.prototype.getTimezoneOffset()	UTCからローカル時刻へのオフセット（分）を返す
Date.prototype.getUTCDate()	そのオブジェクトのUTCでの日にちを返す（下記、同様）
Date.prototype.getUTCDay()
Date.prototype.getUTCFullYear()
Date.prototype.getUTCHours()
Date.prototype.getUTCMilliseconds()
Date.prototype.getUTCMinutes()
Date.prototype.getUTCMonth()
Date.prototype.getUTCSeconds()
Date.prototype.setDate(date)	そのオブジェクトの日付をdateに設定する（下記、同様）
Date.prototype.setFullYear(year [, month [, date]])
Date.prototype.setHours(hour [, min [, sec [, ms]]])
Date.prototype.setMilliseconds(ms)
Date.prototype.setMinutes(min [, sec [, ms]])
Date.prototype.setMonth(month [, date])	
Date.prototype.setSeconds(sec [, ms])	
Date.prototype.setTime(time)	
Date.prototype.setUTCDate(date)	そのオブジェクトのUTCでの日付をdateに設定する（下記、同様）
Date.prototype.setFUTCullYear(year [, month [, date]])
Date.prototype.setUTCHours(hour [, min [, sec [, ms]]])
Date.prototype.setUTCMilliseconds(ms)
Date.prototype.setUTCMinutes(min [, sec [, ms]])
Date.prototype.setUTCMonth(month [, date])	
Date.prototype.setUTCSeconds(sec [, ms])	
Date.prototype.toDateString()	相当する文字列を返す
Date.prototype.toISOString()	相当する文字列（ISO 8601 Extended Format）を返す
Date.prototype.toJSON(key)	JSONで使われる日付時刻文字列を返す
Date.prototype.toLocalDateString([ reserved1 [, reserved2]])	ローカル日付文字列を返す
Date.prototype.toLocalString([ reserved1 [, reserved2]])	ローカル文字列を返す
Date.prototype.toLocalTimeString([ reserved1 [, reserved2]])	ローカル時刻文字列を返す
Date.prototype.toString()	相当する文字列を返す
Date.prototype.toTimeString()	相当する時刻文字列を返す
Date.prototype.toUTCString()	相当するUTC文字列を返す
Date.prototype.valueOf()	基準時刻からの経過ミリ秒を返す
Date.prototype.toPrimitive[@@toPrimitive](hint)	相当するプリミティブ値を返す。hintは"default"もしくは"number"、"string"のどれか。"default"は"string"と同等。
```

