---
slug: spotify-with-raspberry-pi
title: Raspberry Piを使ってSpotifyをheadlessで聞く
tag: [ spotify, raspberry-pi, linux ]
date: 2018-03-21T17:23:26+09:00
lastmod: 2018-03-21T17:31:49+09:00
publishDate: 2018-03-21T17:23:26+09:00
---

　Raspberry Piを使ってSpotifyを再生できるデバイスを作ったので手順などを備忘録代わりに。使用したデバイスはRaspberry Pi Zero W。OSはRaspbian（Stretch）。なお利用にはSpotifyの有料アカウントが必須。

## Spotify Connectデバイスとして使用する


　Spotifyを再生するためには、デバイス側でSpotifyにログインしてプレイリストなどの情報を取得して再生する、という処理を全部行うやり方と、PC/Macやスマートフォン、タブレットなどのSpotifyアプリ側で認証やプレイリスト/楽曲管理などを行い、Spotifyとの通信およびデータダウンロード、再生などのみをデバイス側で行う「Spotify Connect」という機能を使うやり方がある。

　Spotify Connectデバイスとして利用する場合、[Raspotify](https://github.com/dtcooper/raspotify)というソフトウェアを利用すると簡単に実現できる。[librespot](https://github.com/librespot-org/librespot)というオープンソースで開発されているSpotifyクライアントライブラリが使われているが、これらを含有したRaspberry Pi向けのバイナリパッケージが配布されているので、これをインストールし、設定ファイルを編集してサービスを起動するだけで良い。

　設定ファイルは/etc/default/raspotify。変更したのはデバイス名を指定する「DEVICE_NAME」、ビットレートを指定する「BITRATE」といくつかのオプション。オプションについては[librespotのドキュメント](https://github.com/librespot-org/librespot/wiki/Options)にまとめられているが、ここでは使用するALSAデバイスを指定する「--device」、Spotifyアプリとの接続に使用するポートを指定する「--zeroconf-port」、キャッシュディレクトリを指定する「--cache」、音量の自動調整を有効にする「--enable-volume-normalisation」、初期音量を指定する「--initial-volume」を使用している。--deviceの引数はALSAの設定によって変わるので適宜適切なものを選択（後述）。ユーザー名などはSpotifyアプリ経由で取得するので設定不要。「--zeroconf-port」は指定しなくても良いのだが、指定するとポートを固定できるためファイアウォールの設定が簡単になる。

```
# /etc/default/raspotify -- Arguments/configuration for librespot

# Device name on Spotify Connect
#DEVICE_NAME="raspotify"
DEVICE_NAME="5potpy"

# Bitrate, one of 96 (low quality), 160 (default quality), or 320 (high quality)
#BITRATE="160"
BITRATE="320"

# Additional command line arguments for librespot can be set below.
# See `librespot -h` for more info. Make sure whatever arguments you specify
# aren't already covered by other variables in this file. (See the daemon's
# config at `/lib/systemd/system/raspotify.service` for more technical details.)
#
# To make your device visible on Spotify Connect across the Internet add your
# username and password which can be set via "Set device password", on your
# account settings, use `--username` and `--password`.
#
# To choose a different output device (ie a USB audio dongle or HDMI audio out),
# use `--device` with something like `--device hw:0,1`. Your mileage may vary.
#
#OPTIONS="--username <USERNAME> --password <PASSWORD>"
OPTIONS="--device mydev --zeroconf-port 65432"

# Uncomment to use a cache for downloaded audio files. Cache is disabled by
# default. It's best to leave this as-is if you want to use it, since
# permissions are properly set on the directory `/var/cache/raspotify'.
CACHE_ARGS="--cache /var/cache/raspotify"

# By default, the volume normalization is enabled, add another volume argument
# here if you'd like, ie `VOLUME_ARGS=--initial-volume 100`.
VOLUME_ARGS="--enable-volume-normalisation --initial-volume 100"
```

　設定ファイルを作成したら、systemctlコマンドでサービスを開始できる。

```
# systemctl start raspotify
```

　ログはjournalctlコマンドで閲覧できる。

```
# journalctl -u raspotify
```

　確認していないが、zeroconfを使っているとのことで別途avahi-daemonも必須かもしれない。

```
# systemctl start avahi-daemon
```

## Webブラウザ経由で操作できるSpotifyクライアントを使う


　基本的にはSpotify Connect経由での利用で事足りるのだが、Webブラウザ経由で操作できるクライアントについても試しに導入してみた。こちらは[Mopidy](https://www.mopidy.com/)というミュージックサーバーソフトウェアとSpotify用のプラグインを組み合わせて利用することで実現できる・

　Mopidy自体はRaspbian標準でパッケージが提供されているので、これをインストールする。

```
# apt-get install mopidy
```

　次に、Spotify用のプラグインをインストールする。必要なのは下記。

 - [mopidy-mopify](https://github.com/dirkgroenen/mopidy-mopify)：MopidyにSpotify連携用のWeb UIを追加するプラグイン
 - [mopidy-spotify](https://github.com/mopidy/mopidy-spotify)：MopidyにSpotifyからのストリーミング再生機能を追加するプラグイン
 - libspotify：かつてSpotifyが公式に提供していたSpotify連携ライブラリ。すでに開発終了でいつサポートが終了してもおかしくない
 - pyspotify：libspotifyのPythonラッパー

　libspotifyとコンパイル済みのpyspotifyはMopidyのaptリポジトリから入手可能（[ドキュメント](https://docs.mopidy.com/en/latest/installation/debian/)）。自分は次のように直接ダウンロードして使用した。

```
$ wget http://apt.mopidy.com/dists/jessie/non-free/binary-armhf/libspotify12_12.1.103-0mopidy1_armhf.deb
$ wget http://apt.mopidy.com/dists/jessie/contrib/binary-armhf/python-spotify_2.0.5-0mopidy1_armhf.deb
```

　いくつか依存するパッケージがあるので、それはapt-getでインストールする。mopidy-spotifyとmopidy-mopifyについてはpipでインストールできる。

```
# pip install Mopidy-Spotify
```

```
# pip install Mopidy-Mopify
```

　続いて設定ファイルの編集。

```
[core]
cache_dir = /var/cache/mopidy
config_dir = /etc/mopidy
data_dir = /var/lib/mopidy

[logging]
config_file = /etc/mopidy/logging.conf
debug_file = /var/log/mopidy/mopidy-debug.log

[local]
media_dir = /var/lib/mopidy/media

[m3u]
playlists_dir = /var/lib/mopidy/playlists

[http]
enabled = true
hostname = 192.168.1.210
port = 6680
zeroconf = Mopidy HTTP server on $hostname

[mopify]
enabled = true
debug = false

[spotify]
enabled = true
username = ＜Spotifyのユーザー名＞
password = ＜Spotifyのパスワード＞
client_id = ＜client ID＞
client_secret = ＜client secret＞
bitrate = 320
```

　hostnameやusername、passwordは各自適切な物を指定する。client_idおよびclient_secertは[MopidyのWebサイト](https://www.mopidy.com/authenticate/#spotify)にアクセスして「LOG IN WITH SPOTIFY」リンクをクリックしてOAuth認証を行うと、このページにリダイレクトされて設定すべきclient_idおよびcluent_secretが表示される。これをコピペすればOK。


## ALSAの設定


　RaspotifyもMopidyもサウンド出力にはALSAを使用する。認識されているデバイスは/proc/asound/cardsファイルで確認できる。たとえば次の例では、デバイス0としてRaspberry Pi内蔵オーディオ（Raspberry Pi Zero Wの場合HDMI経由での出力に相当するはず）、デバイス1としてUSB端子に接続したオーディオIFが認識されている。

```
# cat /proc/asound/cards
 0 [ALSA           ]: bcm2835 - bcm2835 ALSA
                      bcm2835 ALSA
 1 [USB            ]: USB-Audio - ＜USBサウンドデバイスの情報がここに表示される＞
```

　ALSAの場合、各アプリケーションが使用するサウンドデバイスに関する設定は/etc/asound.confで行える。今回はデフォルト設定（pcm.!default）に加えて、「pcm.mydev」という設定を作ってこれをRaspotifyで使用するよう指定している（前述）。dmixerの設定ではuidが異なる複数のプロセスからの非排他的音声出力を可能にするため「ipc_key_add_uid 0」「ipc_perm 0660」の2つを指定している。また、「slave」以下で「hw:1」を指定することで、オーディオデバイス1、つまりUSBサウンドデバイスを使用するよう指定している。

```
# cat /etc/asound.conf 
pcm.mydev {
  type plug
  slave {
    pcm "dmixer"
  }
}

pcm.!default {
  type plug
  slave {
    pcm "dmixer"
  }
}

pcm.dmixer {
  type dmix
  ipc_key 1024
  ipc_key_add_uid 0
  ipc_perm 0660
  slave {
    pcm "hw:1"
  }
}
```


## 問題点


　Mopidyでは一部のプレイリストが適切に取得できなかったりする模様。これはlibspotifyがもうdeprecatedであるためらしい。

　また、MopidyとRaspotify両方で発生する問題だが、ネットワークが遅くなる時間帯だとストリームのキャッシュに時間がかかったり、間に合わずに音切れが発生する状況となっている。Spotifyアプリだとこの問題は発生しないのでパケットを調べたりしたのだが、どうもSpotify公式アプリはakamai経由でコンテンツをダウンロードしているため混雑時でも高速にコンテンツをダウンロードできているようだ。この機能はMopidy（libspotify）やlibrespotではサポートされていないようなので、簡単には解決できなさそうである。

