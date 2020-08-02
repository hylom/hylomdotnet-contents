---
title: python_sqlite3_commit
author: hylom
type: post
date: 2009-11-25T17:55:20+00:00
excerpt: '<p>　Pythonにはsqlite3という、SQLiteのインターフェイスモジュールがあるんだけど、Python 2.5の日本語ドキュメントのとおりやろうとすると微妙にハマる、という話。</p>'
url: /2009/11/26/python_sqlite3_commit/
categories:
  - Docs

---
　Pythonにはsqlite3という、SQLiteのインターフェイスモジュールがあるんだけど、Python 2.5の日本語ドキュメントのとおりやろうとすると微妙にハマる、という話。

　[日本語ドキュメントのsqlite3ページ][1]には、以下のようなコード例が載ってます。

<pre>c = conn.cursor()

# Create table
c.execute('''create table stocks
(date text, trans text, symbol text,
 qty real, price real)''')

# Insert a row of data
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")</pre>

　ところが、これだと実際にはinsertがデータベースに反映されない。実はinsertなどの操作を行った最後に、sqlite3.Connectionオブジェクトのcommit()メソッドを行わないとコミットが行われず、変更が実行されない模様。

　で、実は[Python 2.5.2ドキュメントのsqlite3ページ][2]には、このあとに以下のようなコードが追加されております。

<pre># Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()</pre>

　にも関わらず、「Connection Object」のページにはcommit()に関する記述がないのでさらに混乱は深まる……。ちなみに、[Python 2.6.4のドキュメント][3]ではちゃんとcommit()メソッドについて記述されており、commit()を実行しないとデータベースへの変更が行われないよ、またrollback()メソッドを実行すれば前回のcommit()までの内容を取り消せるよ、との旨が書かれてます。

　教訓：日本語ドキュメントを当てにせず、ちゃんと原文を読め。

 [1]: http://www.python.jp/doc/release/lib/module-sqlite3.html
 [2]: http://www.python.org/doc/2.5.2/lib/module-sqlite3.html
 [3]: http://docs.python.org/library/sqlite3.html#connection-objects
