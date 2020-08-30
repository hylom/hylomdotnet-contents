---
slug: handling-double-click-event-in-react
title: Reactでアプリを作ってみる（5日目） - ダブルクリックでファイルを開く
tag: [ react, node.js, javascript, programming ]
date: 2020-05-06T18:54:27+09:00
lastmod: 2020-05-06T19:16:25+09:00
publishDate: 2020-05-06T18:54:27+09:00
---

　本来はアプリ内で電子書籍ファイルを開けると良いのですが、ちゃんとした電子書籍ビューアを作るのは正直大変なので、とりあえずサムネイル画像をダブルクリックすると外部アプリケーションでそのファイルを開くようにしてみます。

 - [GW引き篭もりチャレンジ：Reactでアプリを作ってみる（1日目）](/2020/05/06/create-react-app-with-openapi-and-nodejs)
 - [Reactでアプリを作ってみる（2日目） - PDFからのサムネイル生成](/2020/05/06/generate-thumbnail-image-from-pdf-with-nodejs)
 - [Reactでアプリを作ってみる（3日目） - コンテンツの動的な表示](/2020/05/06/show-image-dynamically-by-react)
 - [Reactでアプリを作ってみる（4日目） - Electronを使ったアプリ化](/2020/05/06/convert-react-app-to-electron-app)
 - Reactでアプリを作ってみる（5日目） - ダブルクリックでファイルを開く


### Node.jsプログラムからファイルを指定したアプリで開く



　Node.jsでは[child_process](https://nodejs.org/api/child_process.html)モジュールのexec()やexec()関数を利用することでファイルを実行できる。ただしmacOS環境では/usr/bin/openコマンドを経由してファイルを開く方が楽である。このコマンドでは、次のように指定することで指定したアプリで指定したファイルを開くことができる。

```
open ＜ファイル＞ -a ＜アプリの絶対パス＞
```

　また、「-a ＜アプリの絶対パス＞」を指定しないと、そのファイルに紐づけられているデフォルトのアプリでファイルが開く。当然ながらこれはmacOS環境でしか動作しないので、Linux/Windows環境では普通にアプリケーションのバイナリファイルに引数として開きたいファイルを与えて実行すれば良いと思われる

　これを利用して、[ebmgr.js](https://github.com/hylom/ebmgr/blob/e18521fe7225652e502473100221c62a1759ebf3/ebmgr.js)に次のようにopenBook()メソッドを追加した。

```
function openBook(vpath) {
  // check given path
  const realPath = vpathToRealPath(vpath);
  if (!realPath) {
    return Promise.reject();
  }

  const openCmd = '/usr/bin/open';
  const args = [ realPath ];
  const opts = {};
  const viewer = getViewer(vpath);

  if (viewer && viewer.length) {
    args.push('-a');
    args.push(viewer);
  }

  return new Promise((resolve, reject) => {
    child_process.execFile(openCmd, args, opts,
                           (error, stdout, stderr) => {
                             if (error) {
                               reject(error);
                               return;
                             }
                             resolve();
                           });
  });
};
```

　getViewer()は電子書籍ファイルの拡張子を元に開くアプリのパスを返す関数で、今回の実行は単にconfigファイルのviewersパラメータを参照して対応する値を返すだけ。

```
function getViewer(vpath) {
  const ext = path.extname(vpath).toLowerCase();
  const viewers = config.viewers;
  return viewers[ext];
}
```

　config.jsonではこんな感じに指定している。この場合、ZIP形式ファイルは「/Applications/cooViewer.app」で開かれることになる。

```
  "viewers": {
    ".zip": "/Applications/cooViewer.app",
    ".cbz": "/Applications/cooViewer.app"
  }
```

　このメソッドをReactアプリから呼び出せるよう、[ipc-client/js](https://github.com/hylom/ebmgr/blob/e18521fe7225652e502473100221c62a1759ebf3/react-app/src/ipc-client.js)にopenBook()メソッドを追加。

```
  openBook(path) {
    return this.sendRequest('openBook', path)
      .then(result => {
        return result;
      });
  }
```

　なお今回Webアプリ版の方はこのメソッドを実装しない。OpenAPIクライアント（[openapi-client.js](https://github.com/hylom/ebmgr/blob/e18521fe7225652e502473100221c62a1759ebf3/react-app/src/openapi-client.js)）でこれを実行すると必ず失敗する。

```
  openBook(path) {
    return Promise.reject("openBook() is not implemented");
  }
```

### Reactでのダブルクリックの扱い


　Webアプリで要素のダブルクリックに対しアクションを取るにはdblclickイベントを使うのだが、ReactではonDoubleClickという属性を定義することでイベントハンドラを定義する。このイベントは[Thumbnail](https://github.com/hylom/ebmgr/blob/e18521fe7225652e502473100221c62a1759ebf3/react-app/src/Thumbnail.js)オブジェクトで発生させたいので、このクラス内にイベントハンドラを記述する。

　まずはrender()で返すHTMLのimgタグ内でこの属性を定義する。

```
  render() {
    if (this.state.thumbnail) {
      const b64Data = this.state.thumbnail;
      return (
          <div className="Thumbnail">
          <img className="thumbnail" alt={this.props.item.title} src={b64Data}
               onDoubleClick={() => this.onDoubleClickThumbnail()}/>
          </div>
      );
    } else {
      return (
          <div className="Thumbnail">loading...</div>
      );
    }
  }
```

　ここではイベントハンドラとしてonDoubleClickThumbnail()を実行する無名関数を指定している。onDoubleClickThumbnail()では次のようにclient経由でopenBookメソッドを実行している。

```
  onDoubleClickThumbnail() {
    const client = getClient();
    client.openBook(this.props.item.path).catch(error => {
      console.log(error);
    });
  }
```

　これでサムネイルのダブルクリックに反応してその電子書籍ファイルがconfig.json内で指定したアプリケーションで開かれるようになる。また、非Electron環境ではアプリケーションは開かず、コンソールにエラーメッセージが表示される。

### 環境に応じてElectronアプリのロード元を変更する



　デバッグ時にいちいちコードを変更してElectronアプリ内でのindex.htmlのロード元を変更するのは面倒臭い。そのため、Electronアプリの[main.js](https://github.com/hylom/ebmgr/blob/e18521fe7225652e502473100221c62a1759ebf3/electron/main.js)内で「EBM_MODE」環境変数を参照し、この値が「development」ならReactの開発サーバーから取得し、そうでなければローカルファイルを直接読み込むように挙動が変わるよう条件分岐を入れた。

```

  if (process.env.EBM_MODE == 'development') {
    win.loadURL('http://localhost:3333/index.html');
    win.webContents.openDevTools();
  } else {
    win.loadFile('./public/index.html');
  }
```

　ついでにdevelopmentモードの場合DevToolsを開くようにもしている。

　5日目はここまで。作業時間は1時間半ほど。

