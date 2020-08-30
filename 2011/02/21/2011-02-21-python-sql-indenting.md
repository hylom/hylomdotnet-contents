---
title: Pythonコード中のSQL文インデントを考える
author: hylom
type: post
date: 2011-02-21T09:03:46+00:00
url: /2011/02/21/python-sql-indenting/
category:
  - Docs
tags:
  - programming
  - python
  - sql

---
　Pythonコード内にSQL文を書くときどうすれば良いのか、いまいち答えが探せなかったのでググって見た話。

　ちなみに、今までは下記のような感じのコードを書いていた訳だが、これ見るからに分かりにくい。

<pre># コード例その1
        cur.execute("""
          create table count (
            sid text,
            count int);""")

# コード例その2
        try:
            cur.execute("""insert into count ( sid, count )
                           values ( :sid, :count );""", d)
        except sqlite3.IntegrityError:
            cur.execute("""update count set sid = :sid, count = : count
                           where sid = :sid;""", d)
# コード例その3
        cmd = """select sid, title, date from stories where date >= ? and date &lt; ? and sid in (
                 select sid from topics where topic == ? and sid in (
                 select sid from topics where topic == ? )) order by date
        """
        cur.execute(cmd, (begin_t, end_t, t1, t2))
</pre>

　「SQL インデント」でググると、そういう話のネタが一杯出てくるでてくる。その中から拾ってみたのが下記。

  * [SQLプログラミング作法][1]
  * [SQL のコーディングスタイル（インデント） - 集中力なら売り切れたよ][2]
  * [SQL文をきれいにフォーマットしてくれる『SQL in Form』 - POP*POP ～ 世界のニュースをクオリティ重視で][3]
  * [VB.NETで作る！ | SQL文の字下げ目安][4]
  * [SQLの整形ツール～整形結果の例 - プログラマー'sペイジ][5]

　異端だけど、[俺的コーディングルール SQL編 – suVeneのアレ][6]というのも参考になった。

　で、この辺をまとめたところ、だいたい以下のようなルールに落ち着いた。

  * SQLキーワードは大文字で
  * 括弧挟まれた部分はインデントレベルを+1する
  * カンマ、ANDの直後で改行
  * カンマやANDでつなげられている部分はなるべくキーワード部分でそろえる

　このルールで書いたコードは下記のような感じ。

<pre># コード例その1
        cur.execute("""
            CREATE TABLE count (
                sid text,
                count int
            );
        """)

# コード例その2
        try:
            cur.execute("""
                INSERT INTO count (
                     sid,
                     count
                )
                VALUES (
                    :sid,
                    :count
                )
            """, d)
        except sqlite3.IntegrityError:
            cur.execute("""
                UPDATE count
                SET sid = :sid,
                    count = : count
                WHERE sid = :sid
            """, d)
# コード例その3
        cmd = """
            SELECT sid,
                   title,
                   date
            FROM stories
            WHERE date >= ? AND
                  date &lt; ? AND
                  sid IN (
                      SELECT sid 
                      FROM topics
                      WHERE topic == ? AND
                      sid IN (
                          SELECT sid
                          FROM topics
                          WHERE topic == ?
                      )
                  )
            ORDER BY DATE
        """
        cur.execute(cmd, (begin_t, end_t, t1, t2))
</pre>

　
  
　本当にこれで良いのかはまだ自信がないが、おおむね間違ってはいないと思う。ていうかコード内にSQL文を直書きせずO/Rマッパー使え、という話もあるが……。

 [1]: http://www.geocities.jp/mickindex/database/db_manner.html
 [2]: http://d.hatena.ne.jp/r_ikeda/20090630/indent
 [3]: http://www.popxpop.com/archives/2007/05/sqlsql_in_form.html
 [4]: http://shinshu.fm/MHz/88.44/archives/0000049011.html
 [5]: http://kamoland.com/wiki/wiki.cgi?SQL%A4%CE%C0%B0%B7%C1%A5%C4%A1%BC%A5%EB%A1%C1%C0%B0%B7%C1%B7%EB%B2%CC%A4%CE%CE%E3
 [6]: http://d.zeromemory.info/2007/01/19/coding-rule-sql.html
