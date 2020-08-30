---
title: Pythonのwith構文と__enter__、__exit__
author: hylom
type: post
date: 2010-05-18T11:27:36+00:00
url: /2010/05/18/python_with_statemen/
category:
  - Docs
tags:
  - programming
  - python

---
　Pythonのwith構文がいまいち掴めなかったので、ざっとまとめてみた（いまさらながら）。ドキュメントは[Python リファレンスマニュアルの7.5 with 文][1]にある。

　withを使ったコード例は、下記のような感じ。

<pre>c = ClassHogeHoge()
with c:
    c.foobar()
</pre>

　上記のコードは、下記と等価となる。

<pre>c = ClassHogeHoge()
c.__enter__()
c.foobar()
c.__exit__()
</pre>

　つまり、withに続くインデントブロックを実行する前に指定したオブジェクトの「\_\_enter\_\_()」メソッドを呼び出し、実行後に「\_\_exit\_\_()」メソッドが暗に呼び出される、という仕組み。

　\_\_enter\_\_()と\_\_exit\_\_()の定義は、[Python リファレンスマニュアルの3.4.9 with文とコンテキストマネージャ][2]にある。\_\_enter\_\_()の引数はselfのみだが、\_\_exit\_\_()はself、exc\_type、exc\_value、tracebackの4つの引数をとる。withに続くインデントブロックが正常に実行された（つまり、例外が送出されなかった）場合、（self以外の）引数にはNoneが与えられる。なにか例外が発生した場合、その例外に関する情報が与えられるらしい。

　また、「with hogehoge as foo:」のような形でwith文を利用する場合、\_\_enter\_\_()の戻り値がfooに代入される。\_\_exit\_\_()の戻り値は例外処理の伝搬制御に使われ、Falseの場合例外が発生た場合でも例外を伝搬させず、Trueを返すと例外が伝搬されるとのこと。

　下記、使用例。

<pre>class CacheDB(object):
    DB_FILE = "database/db_dat"

    def __init__(self):
        self.con = None
        self.cur = None

    def __enter__(self):
        self.con = sqlite3.connect(self.DB_FILE)
        self.cur = self.con.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.con = None
            self.cur = None
            return False
        self.con.commit()
        self.cur.close()
        self.con.close()
        self.con = None
        self.cur = None
        return True

    def add(self, foo, bar, hoge):
        try:
            self.cur.execute("""insert into data ( foo, bar, hoge )
                           values (?, ?, ?);""", (foo, bar, hoge))

def main():
    usage = "%s logfile" % sys.argv[0]
    db = CacheDB()
    try:
        fname = args[0]
    except IndexError:
        sys.exit(usage)

    f = open(fname, "r")
    with db:
        for l in f:
            term = l.strip().decode("utf-8").rsplit("\t", 3)
            db.add(foo=term[0],
                   bar=term[1],
                   hoge=term[2])

if __name__ == '__main__':
    main()
</pre>

　タブ区切りのデータファイルを1行ずつ読んでデータベースに突込む、という処理。withを使うことで、データベースアクセスの準備→データ挿入→コミットという流れをきれいに実装できました。

 [1]: http://www.python.jp/doc/2.5/ref/with.html
 [2]: http://www.python.jp/doc/2.5/ref/context-managers.html
