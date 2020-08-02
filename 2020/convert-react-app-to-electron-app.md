---
slug: convert-react-app-to-electron-app
title: Reactでアプリを作ってみる（4日目） - Electronを使ったアプリ化
tags: [ electron react javascript programming ]
date: 2020-05-06T17:13:39+09:00
lastmod: 2020-05-06T19:15:42+09:00
publishDate: 2020-05-06T17:13:39+09:00
---

　サムネイル画像表示ができたので、本日はこのアプリをアプリフレームワーク[Electron](https://www.electronjs.org)を使ってスタンドアロンで動作するアプリケーション化してみます。

 - [GW引き篭もりチャレンジ：Reactでアプリを作ってみる（1日目）](http://hylom.net/create-react-app-with-openapi-and-nodejs)
 - [Reactでアプリを作ってみる（2日目） - PDFからのサムネイル生成](http://hylom.net/generate-thumbnail-image-from-pdf-with-nodejs)
 - [Reactでアプリを作ってみる（3日目） - コンテンツの動的な表示](http://hylom.net/show-image-dynamically-by-react)
 - Reactでアプリを作ってみる（4日目） - Electronを使ったアプリ化
 - [Reactでアプリを作ってみる（5日目） - ダブルクリックでファイルを開く](http://hylom.net/handling-double-click-event-in-react)

# WebアプリをElectronアプリ化する際の要件



　Electronでは、一般的なWebアプリでは実現できないローカルファイルシステムへのアクセスが可能になる。これを利用することで、Webサーバーを使わずにそのアプリ単独で完結するアプリを開発できる。

　ただ、Electron内で表示される画面はあくまでHTMLベースのものなので、画像を表示させたい場合はURLでそのコンテンツの場所を指定する必要がある。今回のサムネイル画像のような動的に生成した画像を表示させたい場合、選択肢としてはelectronのプロセス内でWebサーバーを立ち上げてそこにHTTPでリクエストを投げて画像を取得するか、どこかにファイルとして保存してそのパスをURLとして指定する、もしくは[data:スキーマのURL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)を使うという3通りがある。今回は別途Webサーバーを立ち上げたくはないので、data:スキーマを利用することにする。

　また、Electron内で実行するコードからはNode.jsの任意のモジュールが利用できるため、電子書籍ファイル一覧の取得やサムネイルの取得はこれらの処理を実装したebmgr.jsを直接importして利用すれば良いだろうと思っていたのだが、今回使用したcreate-react-appベースの開発環境ではfsなどのモジュールが利用できないように細工がされている模様（[# データアクセスのためのクラス実装


　Electronではアプリ全体を管理するプロセスと画面表示に関連するプロセスが分離されており、前者をメインプロセス、後者をレンダープロセスと呼ぶ。レンダープロセスとメインプロセスはIPCで簡単に通信ができるので、IPC経由でebmgr.jsに実装されている関数を呼び出せるプロクシクラス（[https://github.com/hylom/ebmgr/blob/9aa49967ff2ed933009b454ee035e32b68c0609f/react-app/src/ipc-client.js ipc-client.js](https://github.com/hylom/ebmgr/blob/9aa49967ff2ed933009b454ee035e32b68c0609f/react-app/src/ipc-client.js ipc-client.js)(https://github.com/facebook/create-react-app/issues/3074]）。しょうがないので、これらの処理はElectronのメインプロセスで実行することにする。)）を実装し、クライアントからはこのプロクシクラス経由で各種関数を呼び出す設計とした。

　なお、IPCを利用するにはelectronモジュールを読み込む必要があるのだが、非Electron環境ではその動作は失敗する。そのため、次のように条件分岐を入れた上でモジュールを読み込ませる必要がある。

```
let ipcRenderer;
if (window.require) {
  const electron = window.require('electron');
  ipcRenderer = electron.ipcRenderer;
}
```

　IPC周りのコードは次のように実装した。メインプロセスに対し、「FunctionCall」というメッセージとともにメソッド名、リクエストID、パラメータを送信すると、その処理結果が「＜メソッド名＞_＜リクエストID＞」というメッセージとともに非同期に返される、という流れとなっている。返されるメッセージに対するイベントハンドラは、一回限りのハンドラを登録するonce()メソッドで登録している。

```
let requestId = 0;
const timeoutMilSec = 30000; // 30 seconds

const channelSend = 'FunctionCall';

export default class IpcClient {
  sendRequest(method, params) {
    requestId++;
    return new Promise((resolve, reject) => {
      ipcRenderer.send(channelSend, method, requestId, params);
      const listener = (event, result, error) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(result);
      };
      const channelRecv = `${method}_${requestId}`;
      ipcRenderer.once(channelRecv, listener);
      setTimeout(() => {
        ipcRenderer.removeListener(channelRecv, listener);
        reject({message: "response too late",
                name: 'TimeOutError'});
      }, timeoutMilSec);
    });
  }

  getBooks() {
    return this.sendRequest('getBooks');
  }

  getBookThumbnail(path) {
    return this.sendRequest('getBookThumbnail', path)
      .then(result => {
        result.data = new Blob([result.data]);
        return result;
      });
  }
}
```

　この場合、何らかの不具合で結果が返ってこないと永遠にそのハンドラが残り続けてメモリリークが発生するので、タイムアウト時間（30秒）を設定してこの時間内に結果が返ってこない場合失敗したとみなしてイベントハンドラを削除するようにしている。

　また、  getBookThumbnail()内で受け取った画像データをBlobに変換しているが、これはswagger-client経由で同じ処理を実行した場合の動作に合わせるために行なっている。

　メインプロセス側のコードは次のようにした。

```
const channelSend = 'FunctionCall';
ipcMain.on(channelSend, (event, method, requestId, params) => {
  const channelRecv = `${method}_${requestId}`;
  if (method == 'getBooks') {
    ebmgr.getBooks().then(
      result => {
        event.reply(channelRecv, result);
      },
      error => {
        event.reply(channelRecv, undefined, error);
      }
    );
    return;
  } else if (method == 'getBookThumbnail') {
    ebmgr.getBookThumbnail(params).then(
      result => {
        event.reply(channelRecv, result);
      },
      error => {
        event.reply(channelRecv, undefined, error);
      }
    );
    return;
  }
  event.reply(channelRecv, undefined, { message: "method not found",
                                        name: "InvalidMethodError" });
});
```

　あわせて、Electron環境ではIPC経由、Web環境ではOpenAPI経由で同一の関数にアクセスできるよう、OpenAPI経由での呼び出しについても同じインターフェイスを持つクラス（[OaClient](https://github.com/hylom/ebmgr/blob/2377dd201cc864dbaa53f38a7c53437d8cacca01/react-app/src/openapi-client.js)）を実装し、Electron環境かどうかをチェックして適切なクラスのインスタンスを返すgetClient()関数を[client.js](https://github.com/hylom/ebmgr/blob/2377dd201cc864dbaa53f38a7c53437d8cacca01/react-app/src/client.js)というファイルに実装した。

```
import OaClient from './openapi-client';
import IpcClient from './ipc-client';

export default function getClient() {
  if (isElectron()) {
    return new IpcClient();
  } else {
    return new OaClient();
  }
}
```

　これで、getClient()経由でクライアントオブジェクトを取得し、それに対しgetBooks()やgetBookThumbnail()を呼び出すことで、Electron/Webブラウザどちらの環境でも同じコードで処理を記述できるようになる。

　electronのメインプロセスのコード（[main.js](htt＊ps://github.com/hylom/ebmgr/blob/2377dd201cc864dbaa53f38a7c53437d8cacca01/electron/main.js)）はドキュメントのサンプルコード（[```
win.loadURL('http://localhost:3333/');
```

　こうすることで、index.htmlファイルをReactのテストサーバーから直接取得できるようになり、開発効率が上がる。

# 画像をdata:URL経由で表示させる



　まずReactアプリのコンポーネントとして、画像を表示する[https://github.com/hylom/ebmgr/blob/2377dd201cc864dbaa53f38a7c53437d8cacca01/react-app/src/Thumbnail.js Thumbnail](https://github.com/hylom/ebmgr/blob/2377dd201cc864dbaa53f38a7c53437d8cacca01/react-app/src/Thumbnail.js Thumbnail)(https://www.electronjs.org/docs/tutorial/first-app#electron-development-in-a-nutshell]）ほぼそのままだが、IPC関連のコードを追加しているのと、loadFileの部分を次のように変更している。)コンポーネントを作成する。Reactのコンポーネントはその属性として任意のオブジェクトを受け取れるようになっており、渡されたオブジェクトはconstructor()の引数として渡される。これを引数にsuper()を実行することで、this.propというプロパティでその値にアクセスできるようになる。

```
class Thumbnail extends Component {
  constructor (props) {
    super(props);
    this.state = { thumbnail: null,
                 };
  }
```

　ここでは、「item」という属性として電子書籍ファイルの情報（パス、タイトル）を受け取ることを想定し、そのパスを与えてgetBookThumbnail()メソッドを実行することでサムネイル画像を取得する。この処理は非同期で実行されるので、componentDidMount()メソッド内で実行する。画像を取得できたら、[FileReaderオブジェクト](https://developer.mozilla.org/ja/docs/Web/API/FileReader)を使ってそれをdata: URLに変換してstate.thumbnailに格納し、これをsrc属性に指定したimg要素を出力させる。

```
  componentDidMount() {
    const client = getClient();
    client.getBookThumbnail(this.props.item.path).then(
      result => {
        //console.log(result);
        const reader = new FileReader();
        reader.readAsDataURL(result.data);
        reader.addEventListener('load', event => {
          this.setState({thumbnail: reader.result});
        });
      }
    );
  }

  render() {
    if (this.state.thumbnail) {
      const b64Data = this.state.thumbnail;
      return (
          <div className="Thumbnail">
          <img className="thumbnail" alt={this.props.item.title} src={b64Data} />
          </div>
      );
    } else {
      return (
          <div className="Thumbnail">loading...</div>
      );
    }
  }
}
```


　[ThumbnailGridコンポーネント](https://github.com/hylom/ebmgr/blob/2377dd201cc864dbaa53f38a7c53437d8cacca01/react-app/src/ThumbnailGrid.js)では、このThumbnailコンポーネントを利用する形にrender()を修正した。

```
render() {
  const makeThumb = x => {
    const encodedPath = encodeURIComponent(x.path);
    return (
        <li key={x.title}>
        <Thumbnail item={x} />
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

# Electronアプリの起動



　Electronを利用したコードは、electronコマンド経由で実行する必要がある。毎回手で打ち込むのは面倒なので、Makefileを作成した。

```
run:
	./node_modules/.bin/electron main.js
```

　これで試しにアプリを実行したところ、サムネイル変換処理が終わるまでアプリが固まることが判明。ghostscriptの実行を同期的に行なっているのが原因と思われる。ということで、[ebmgr.js](https://github.com/hylom/ebmgr/blob/2377dd201cc864dbaa53f38a7c53437d8cacca01/ebmgr.js)内でexportしている関数はすべてPromiseを返す非同期関数に書き換える。

```
function getZipThumbnail(vpath) {
  const realPath = vpathToRealPath(vpath);
  const zip = new AdmZip(realPath);
  const rex = /(\.jpeg|\.jpg)$/;

  for (const entry of zip.getEntries()) {
    if (!entry.isDirectory && rex.test(entry.entryName)) {
      console.log(entry.entryName);
      const data = zip.readFile(entry);
      return Promise.resolve({ contentType: 'image/jpeg',
                               data: data });
    }
  }
  return Promise.reject();
}
```


　ZIPファイルの処理をするAdmZipは非同期処理をサポートしていないようなので単にPromiseでラップした結果を返すだけ。PDFの処理をしているghostscript4jsは非同期に処理を実行するexecuteメソッドを提供しているので、それをPromiseでラップしている。

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

  return new Promise((resolve, reject) => {
    gs.execute(gsCmd, err => {
      if (err) {
        reject(err);
        return;
      }
      resolve(destination);
    });
  });
```

　getPdfThumbnail()はエラー処理をサボっているので、async funtion化でPromiseを返すようにした。Node.jsではfs.promises以下にPromiseを返すメソッドが用意されているのでこれを活用している。

```
async function getPdfThumbnail(vpath, page) {
  const pathname = await makeTempFile(vpath, ".jpeg");
  await generatePdfThumbnail(vpath, pathname, page);

  const data = await fs.promises.readFile(pathname);
  await fs.promises.unlink(pathname);

  return { contentType: 'image/jpeg',
           data: data };
}
```

　これらに対応して、サーバー側でこれらを呼び出しているコードも書き換えておく。

　さて、相変わらず処理は重いものの、これでアプリがサムネイルのロード環境まで固まる現象は解決。ただ、すべての画像が一斉に表示されるという別の問題に気付く。とはいえ現時点ではクリティカルな問題ではないのでToDOに入れて一旦放置。

# スタンドアロンなElectronアプリ化



　この状態では、Electronアプリ内で表示するHTMLファイルはAPIサーバー経由で取得しているので、これを静的なHTMLに切り替えることでアプリがスタンドアロンで動作するように変更する。まず、create-react-appでビルドしたアセットディレクトリ（build）のシンボリックリンクをelectronディレクトリ内に「public」という名前で作成し、この中のindex.htmlをElectronアプリ側のmain.js内で次のようにロードさせてみる

```
  win.loadFile('./public/index.html');
```

　すると、動かない。これは、create-react-appで作成した環境でビルドして出力されたindex.htmlファイルではJSやCSS、画像などの各種リソースがすべて「/」から始まる絶対パスで書かれているため。ググったところ、これはReactアプリのpackage.jsonに「"homepage": "."」を追加することで解決できるとあったので（[　これでWebサーバーレスでアプリを実行できるようになったので、これらをアプリとしてパッケージングしてみる。基本的にはドキュメント（[https://www.electronjs.org/docs/tutorial/application-distribution](https://www.electronjs.org/docs/tutorial/application-distribution)(https://github.com/facebook/create-react-app/blob/1d03579f518d2d5dfd3e5678184dd4a7d8544774/docusaurus/docs/deployment.md]）、これを試したところ無事解決。)）で書かれている通りの作業をすることになる。

　これは定期的に実行することになるので、Makefileを書く。

```
APP_DEST=release
ELECTRON_PREBUILT=electron/electron/dist
ELECTRON_DIR=electron
RES_DIR=$(APP_DEST)/Electron.app/Contents/Resources/app
REACT_DIR=react-app

dist: $(APP_DEST)
        rsync -a $(ELECTRON_PREBUILT)/ $(APP_DEST)
        rsync -a --exclude='*~' \
                 --exclude='ebmgr.js' \
                 --exclude='Makefile' \
                 --exclude='electron' \
                 --exclude='public' \
                 $(ELECTRON_DIR)/ $(RES_DIR)/
        cp -a ebmgr.js config.json $(RES_DIR)/
        rsync -a $(REACT_DIR)/build/ $(RES_DIR)/public/

$(APP_DEST):
        mkdir -p $(APP_DEST)
```

　また、Electronアプリ内でghostscript4jsやadm-zipモジュールを利用できるよう、package.jsonファイルに依存性を追加しておく。

```
  "dependencies": {
    "adm-zip": "^0.4.14",
    "electron": "^8.2.5",
    "ghostscript4js": "^3.2.1"
  },
```

　これでElectronのアイコンをダブルクリックすると起動するアプリ化完了。

<img src="/img/blog/2020/05/electron_ebmgr.png" />

　デバッグ中なのでDevToolsが表示されているが、これはElectronアプリのmain.js内の次のコードを削除すれば表示されなくなる。

```
  win.webContents.openDevTools();
```

　本日はここまで。作業時間はちょっと使ってしまって5時間ほど。

