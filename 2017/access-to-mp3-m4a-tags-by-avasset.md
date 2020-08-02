---
slug: access-to-mp3-m4a-tags-by-avasset
title: AVFoundation小ネタ1：AVAssetを使ってmp3やm4aのタグ情報を取得する
tags: [ swift,osx ]
date: 2017-05-21T01:28:53+09:00
lastmod: 2017-05-21T01:29:13+09:00
publishDate: 2017-05-21T01:28:53+09:00
---

　macOS（10.7以降）やiOS（4以降）などで利用できる[AVAsset](https://developer.apple.com/reference/avfoundation/avasset)クラスを利用することで、別途外部のライブラリを使用せずにmp3ファイルやm4a（AAC）ファイルのメタデータ（タグ情報）を取得できる。AVAssetはさまざまな動画や音声ファイルに対応しており、同様のやり方で動画ファイルのメタデータも取得できると思われる（未検証）。

　特定のファイルのメタデータを取得するには、まずAVAsset(URL: url)メソッドを使ってAVAssetオブジェクトを作成する。url引数には対象ファイルのパスをNSURL形式で指定する。

```
let path = ＜ファイルのパス＞
let url = NSURL(fileURLWithPath: path)
let asset = AVAsset(URL: url)
```

　メタデータにはmetadataプロパティやcommonMetadataプロパティ経由でアクセスできる。このプロパティは[AVMetadataItem](https://developer.apple.com/reference/avfoundation/avmetadataitem)の配列となっている。この配列に対しfor inループなどを使ってメタデータを探して処理を行えば良い。

```
for metadata in asset.metadata {
    // metadataオブジェクトを使ってメタデータを得る
}
```

## AVMetadataItemの中身　


　ここまでは簡単なのだが、AVMetadataItemクラスはさまざまな形式のファイルに対応するための抽象化がされており、ドキュメント初見では意味が分かりにくいかもしれない。

　まずkeySpaceプロパティだが、ここにはそのメタデータがどのファイル形式でサポートされているものなのかを示す文字列が格納されている。ここで使われる文字列のうちいくつかはあらかじめ定数として定義されている（[Key Spaces](https://developer.apple.com/reference/avfoundation/media_assets_playback_and_editing/av_foundation_metadata_key_constants/key_spaces)）。たとえばmp3が格納しているタグ情報であるID3で利用できるメタデータの場合、keySpaceプロパティの値はAVMetadataKeySpaceID3（文字列としては"org.id3"）になる。AVMetadataItemクラスには、指定したメタデータの配列から指定したkeySpaceに対応するメタデータだけを取り出すmetadataItemsFromArrayというクラスメソッドも用意されている。

　また、keyプロパティにはメタデータを識別する情報（キー）が格納されている。この情報は必ずしも文字列であるとは限らないため、型はStringではなく(NSCopying & NSObjectProtocol)?になっている。そのため、これを文字列として参照したい場合はidentifierプロパティを使う。

　文字列形式のメタデータキーについても定数があらかじめ定義されている。たとえば[ID3の場合](https://developer.apple.com/reference/avfoundation/media_assets_playback_and_editing/av_foundation_metadata_key_constants/id3_metadata_keys)、タイトルはAVMetadataID3MetadataKeyTitle、アルバム名はAVMetadataID3MetadataKeyAlbumTitleという定数が定義されている。たとえばタイトルとアルバム名を取り出したい場合、これを使って次のようにすれば良い。

```
for metadata in AVMetadataItem.metadataItemsFromArray(asset.metadata, withKey: nil, keySpace: AVMetadataKeySpaceID3) {
    guard let key = metadata.identifier else { continue }

    if key == AVMetadataID3MetadataKeyTitle {
        if let v = metadata.stringValue {
            title = v
        }
    }
    if key == AVMetadataID3MetadataKeyAlbumTitle {
        if let v = metadata.stringValue {
            album = v
        }
    }
    :
    :
}
```

　値が格納されているvalueプロパティについても型はStringではなく(NSCopying & NSObjectProtocol)?になっているので、stringValueやnumberValue、dateValueなどのメソッド経由で取り出すのが良い。

　さて、ファイル形式によって利用できるkeyは異なる。たとえば同じタイトルでも、ID3ならAVMetadataID3MetadataKeyTitleDescription、iTunesならAVMetadataiTunesMetadataKeySongNameというキーになっている。種別ごとにキーが異なるのは面倒なので、AVMetadataItemにはcommonKeyというプロパティが用意されており、たとえばタイトルを示すメタデータであればこのプロパティにAVMetadataCommonKeyTitle（文字列としては"title"）というデータが入っている。こちらも[あらかじめ定数が定義されている](https://developer.apple.com/reference/avfoundation/media_assets_playback_and_editing/av_foundation_metadata_key_constants/common_metadata_keys)。こちらを利用することで、ファイル形式によらず情報を取得できる。

```
for metadata in asset.metadata {
    if metadata.commonKey == AVMetadataCommonKeyTitle {
        if let v = metadata.stringValue {
            title = v
    }
}
```

## iTunes形式のメタデータに関する注意点


　iTunes形式のメタデータ（keySpaceがAVMetadataKeySpaceiTunesのメタデータ）では、identifierプロパティに「itsk/%A9nam」といった文字列が格納されている。いっぽう、あらかじめ定義されている[iTunes Metadata Keys](https://developer.apple.com/reference/avfoundation/media_assets_playback_and_editing/av_foundation_metadata_key_constants/itunes_metadata_keys)では、たとえばタイトルを示すAVMetadataiTunesMetadataKeySongNameの値は「@nam」という文字列になっており、これらが一致しない。そのため、次のようにしてidentifierの値を変換した上で比較する必要がある。

```
guard let key = metadata.identifier else { continue }
// key is like 'itsk/%A9nam', so split and decode
let comps = key.componentsSeparatedByString("/")
    if (comps[0] != "itsk") {
        continue
    }
    let k = comps[1].stringByReplacingOccurrencesOfString("%A9", withString: "@")
}
```

