---
slug: show-image-dynamically-by-react
title: Reactでアプリを作ってみる（3日目） - コンテンツの動的な表示
tags: [ react, javascript, node.js, programming ]
date: 2020-05-06T16:14:38+09:00
lastmod: 2020-05-06T19:16:45+09:00
publishDate: 2020-05-06T16:14:38+09:00
---

　GWなのでReactで電子書籍管理アプリを作ってみようという話の3日目です。

 - [GW引き篭もりチャレンジ：Reactでアプリを作ってみる（1日目）](http://hylom.net/create-react-app-with-openapi-and-nodejs)
 - [Reactでアプリを作ってみる（2日目） - PDFからのサムネイル生成](http://hylom.net/generate-thumbnail-image-from-pdf-with-nodejs)
 - Reactでアプリを作ってみる（3日目） - コンテンツの動的な表示
 - [Reactでアプリを作ってみる（4日目） - Electronを使ったアプリ化](http://hylom.net/convert-react-app-to-electron-app)
 - [Reactでアプリを作ってみる（5日目） - ダブルクリックでファイルを開く](http://hylom.net/handling-double-click-event-in-react)

# PDFからのサムネイル画像の作成と読み込み



　2日目の課題として残っていたサムネイル画像をどうやって扱うか問題だが、とりあえずテンポラリディレクトリ上に一時的にサムネイル画像ファイルを生成し、その直後にそのファイルを読み込んだ後削除することで、ローカルファイルシステム上にサムネイルを保持させない方針にしてみる。この時ファイル名に気をつけないと、実行のタイミングによっては一時的に作った画像ファイル名が衝突して意図しないものにすり替わるというトラブルが発生する可能性があるため、作成する画像ファイル名は電子書籍ファイルのパス名のハッシュを用いて生成するようにする。

```
function makeTempFile(vpath, ext) {
  const tmpdir = os.tmpdir();
  let pathname = path.join(tmpdir, getHash(vpath, 'sha256') + ext);

  let done = false;
  let n = 0;
  while (!done) {
    try {
      fs.writeFileSync(pathname, "", {flag: 'wx'});
      done = true;
    }
    catch (e) {
      pathname = path.join(tmpdir, getHash(vpath + String(n), 'sha256') + ext);
      n++;
    }
  }
  return pathname;
}
```

　ファイル名の重複を確実に回避するため、空ファイルを作成しておいて、その後Ghostscriptでそのファイルを上書きするという方針にしている。ファイル作成時に「wx」オプションを指定しているので、同名のファイルが存在した場合ファイル作成が失敗する→それを検知して別のファイル名を作成して再度ファイル作成を試みる、を繰り返すというアルゴリズムになっている。

　また、変換処理の実行時にメッセージが表示されてログが汚れるので「-q」オプションを追加して進捗メッセージは非表示にする。オプション配列の後ろの方にこのオプションをつけないとなぜか有効に動かない模様でちょっとハマる。


```
  const gsCmd = [ "-sDEVICE=jpeg",
                  "-o",
                  destination,
                  "-sDEVICE=jpeg",
                  "-r72",
                  `-dFirstPage=${page}`,
                  `-dLastPage=${page}`,
                   "-q",
                  realPath];
```

　なお、ここまでスルーしていたが、このアプリ内では電子書籍のパスを仮想パス（vpath）で扱っている。これは設定ファイルで指定した電子書籍ファイルが格納されているディレクトリの絶対パスをMD5でハッシュ化し、そのハッシュ＋個別のファイルの相対パスに相当する。うっかりミスでファイルシステム内全体にアクセスできるようになってしまう可能性を減らすためにこのような仕様にしている。

　最終的にPDFファイルのサムネイルを取得する関数は次のような形となった。将来的にJPEG以外の形式でサムネイルを作成する可能性も考慮して一緒にcontentTypeも返している。

```
function getPdfThumbnail(vpath, page) {
  const pathname = makeTempFile(vpath, ".jpeg");
  generatePdfThumbnail(vpath, pathname, page);

  const data = fs.readFileSync(pathname);
  fs.unlinkSync(pathname);

  return { contentType: 'image/jpeg',
           data: data };
}
```

# OpenAPIのサービス仕様定義の修正とAPIサーバーの修正



　続いては、電子書籍ファイルの仮想パスを指定すると、それに対応したサムネイル画像を返すAPIをAPサーバーに追加する。まずはサービス仕様ファイルにこのAPIを記述する。これは指定された電子書籍ファイルが見つかればimage/jpeg形式で対応する画像を返し、そうでない場合は404を返すというもの。

```
paths:
  /books/{vpath}/thumbnail:
    get:
      x-swagger-router-controller: Default
      description: Returns a thumbnail of the book
      operationId: getBookThumbnail
      parameters:
        - in: path
          name: vpath
          schema:
            type: string
          required: true
          description: virtual path of the book
      responses:
        "404":
          description: A book with the given vpath was not found
        "200":
          description: A thumbnail of book
          content:
            image/jpeg:
              schema:
                type: string
                format: binary
```

　この定義ファイルをSwagger Editorに読み込ませて再度サーバーコードを生成してみたのだが、ロジックを毎回再生成されるディレクトリツリーから分離した場所に記述するのが面倒そうな感じだったため、すでに実装しているサーバーコードに手動で追加したパスに対する処理を定義する。といっても編集が必要なのはservice/DefaultService.jsとcontrollers/Default.js、api/openapi.yaml（サービス仕様定義ファイル）の3つのみ。最後のサービス仕様定義ファイルについてはマスターとしている親ディレクトリのもののシンボリックに置き換えておいた。

　まず、[service/DefaultService.js](https://github.com/hylom/ebmgr/blob/8b13a855070acd100bcd8475de6b14a0e7939314/api-server/service/DefaultService.js)内にロジックに相当するコードを記述。このコードは既存コードを参考にしてPromiseを返すようにしている。

```
/**
 * Returns a thumbnail of the book
 *
 * vpath String virtual path of the book
 * returns byte[]
 **/
exports.getBookThumbnail = function(vpath) {
  return new Promise(function(resolve, reject) {
    const thumb = ebmgr.getThumbnail(vpath);
    if (thumb) {
      resolve(thumb);
    } else {
      resolve();
    }
  });
}
```

　続いていわゆるコントローラに相当する処理を[controllers/Default.js](https://github.com/hylom/ebmgr/blob/8b13a855070acd100bcd8475de6b14a0e7939314/api-server/controllers/Default.js)に書く。ここにはHTTPヘッダやレスポンスを返すというWebサーバー的に必要な処理を記述する。このサーバーはexpressjsを使っているので、expressjsの流儀に従ってレスポンス/リクエストオブジェクト経由でレスポンスを返す処理を記述すればOK。

```
module.exports.getBookThumbnail = function getBookThumbnail (req, res, next, vpath) {
  Default.getBookThumbnail(vpath)
    .then(function (thumb) {
      if (!thumb) {
        // resource not found
        res.writeHead(404);
        res.end();
        return;
      }
      res.writeHead(200, {'Content-Type': thumb.contentType });
      res.end(thumb.data);
    })
    .catch(function (response) {
      res.writeHead(500);
      res.end();
    });
};
```

　これでAPIサーバーを起動して/docs以下にアクセスしてSwaggerでテストする。問題なく動作したので続いてクライアント側のコードを記述する。

# Reactアプリのコード更新



　OpenAPIクライアント経由でgetBooksメソッドを実行して取得した電子書籍リストでは、pathプロパティでその電子書籍ファイルの仮想パスが与えられている。API仕様では/api/v1/books/{URIエンコードされた仮想パス}/thumbnailというパスに対しGETメソッドを投げるとサムネイル画像がimage/jpegというContent-Typeで返ってくるようになっているので、[ThumbnailGrid.js](https://github.com/hylom/ebmgr/blob/8b13a855070acd100bcd8475de6b14a0e7939314/react-app/src/ThumbnailGrid.js)ファイル内のrender()メソッドが返すHTML内のimgタグのsrc属性でこのURLを指定する。Reactのテンプレート（JSX）内で文字列連結をする場合、{}の中でJavaScriptコードとして連結処理を記述しなければならないのにちょっとハマる。

```
render() {
  const makeThumb = x => {
    const encodedPath = encodeURIComponent(x.path);
    return (
        <li key={x.title}>
        <img class="thumbnail" src={"/api/v1/books/" + encodedPath + "/thumbnail"} />
        </li>
    );
  };
  const listItems = this.state.items.map(makeThumb);
  return (
      <div className="ThumbnailGrid">
      <ul>{listItems}</ul>
      </div>
  );
}
```


　これでReactのテストサーバーを起動してテスト。ちゃんとサムネイルは表示される。

<img src="/img/blog/2020/05/react_thumbs.png" height="400" />

　ただ、画像が表示されるまでちょっと待たされる感じになっている。ログを見るとこんな感じ。

```
GET /api/v1/books/0f276cdfc8a2c99c988ef7b88141f377%2FOP%E3%82%A2%E3%83%B3%E3%83%95%E3%82%9A%2F6_1-4_Analog_Filteres.pdf/thumbnail 200 136.203 ms - -
   **** Error reading a content stream. The page may be incomplete.
               Output may be incorrect.

   **** Error: File has unbalanced q/Q operators (too many Q's)
               Output may be incorrect.
   **** Error: File did not complete the page properly and may be damaged.
               Output may be incorrect.
GET /api/v1/books/0f276cdfc8a2c99c988ef7b88141f377%2FOP%E3%82%A2%E3%83%B3%E3%83%95%E3%82%9A%2F6_5-8_Analog_Filteres.pdf/thumbnail 200 202.495 ms - -
```

　ここから、サムネイル生成処理には1つあたりおおむね数百ミリ秒ほどかかっていることが分かる。さすがにちょっとUI的に重いが、とりあえずここの部分の最適化はToDoに突っ込んで置いてまたの機会に。ghostscriptのエラーメッセージについては、画像自体はちゃんと表示されているので現時点では無視。

# ZIP形式の電子書籍ファイルからのサムネイル画像取得



　ZIP形式の電子書籍ファイルについても、同じようにサムネイル画像を表示したい。アルゴリズム的にはZIPファイル内のファイルをスキャンして最初に見つかったjpegファイルを取り出せばOKだろう。モジュールとしてはJSZip（[https://www.npmjs.com/package/jszip](https://www.npmjs.com/package/jszip)）とADM-ZIP（[https://www.npmjs.com/package/adm-zip](https://www.npmjs.com/package/adm-zip)）というものが見つかった。利用者数はどちらも十分に多く、どっちを選択しても問題なさそうだが、ADM-ZIPはほかに依存するモジュールがない（Dependenciesが0）という点が気に入ったのでそちらを選択。

　サムネイル取得関連のメソッドを整理し、ZIP用とPDF用に分割。すんなりとZIPファイル内から最初の画像ファイルを取得するコードを実装できた（[コード全文](https://github.com/hylom/ebmgr/blob/8b13a855070acd100bcd8475de6b14a0e7939314/ebmgr.js)）。

```
function getZipThumbnail(vpath) {
  const realPath = vpathToRealPath(vpath);
  const zip = new AdmZip(realPath);
  const rex = /(\.jpeg|\.jpg)$/;

  for (const entry of zip.getEntries()) {
    if (!entry.isDirectory && rex.test(entry.entryName)) {
      console.log(entry.entryName);
      const data = zip.readFile(entry);
      return { contentType: 'image/jpeg',
               data: data };
    }
  }
}
```

　getThumbnail()関数では拡張子に応じてgetPdfThumbnail()もしくはgetZipThumbnail()を呼び出すことで適切にサムネイルを生成できるようにする。

```
exports.getThumbnail = getThumbnail;
function getThumbnail(vpath, page) {
  // check given path
  const realPath = vpathToRealPath(vpath);
  if (!realPath) {
    return undefined;
  }

  const ext = path.extname(realPath).toLowerCase();
  if (ext == ".pdf") {
    page = page || 1;
    return getPdfThumbnail(vpath, page);
  }
  if (ext == ".zip" || ext == ".cbz") {
    return getZipThumbnail(vpath);
  }
};
```

　これでZIP圧縮形式の電子書籍ファイルのサムネイルもとりあえず表示できるようになった。

# 開発サーバーを使わないアプリ実行（Reactアプリのデプロイ）


　まずはサムネイル画像表示までを実現できたので、ここでReactの開発サーバー外でクライアントを動作できることを確認する。Reactアプリのディレクトリで「npm run build」コマンドを実行すると、アセットがビルドされてリリース用のコードが作成され、buildディレクトリ内にそれら一式が出力される。このディレクトリ内のファイルをWebサーバーで公開することで、開発用サーバーを使わずにアプリを実行できる。

　今回はAPIサーバーのディレクトリ内にReactアプリディレクトリ内のbuildディレクトリへのシンボリックリンクを「public」という名前で作成する。続いてAPIサーバーの[index.js](https://github.com/hylom/ebmgr/blob/80b1b0a2b0b373a6e6ae2044472a56dc89fa1774/api-server/index.js)を修正し、EBM_MODE環境変数の値によってプロキシの有効/無効を切り替えるように変更。これでEBM_MODE環境変数がdevelopment以外の場合、buildディレクトリ内のコンテンツが/以下で公開されるようになる。

```
// check running environment
const mode = process.env.EBM_MODE || 'development';

if (mode == 'development') {
  // add routes for React
  app.use(/^\/(?!(docs|api)\/).*/, createProxyMiddleware({ target: 'http://localhost:3000', changeOrigin: true }));
} else {
  app.use(express.static('public'));
}
```

　動作チェックをすると、問題なく動く。Reactアプリはデプロイが面倒そうな先入観があったのだが、意外に簡単だった。ただしnpm run buildコマンドはそれなりに実行に時間がかかるので頻繁に実行することは想定しないほうが良い感じ。

　ということで本日はここまで。作業時間は4時間ほど。

