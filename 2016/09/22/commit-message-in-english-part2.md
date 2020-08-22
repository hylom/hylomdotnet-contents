---
slug: commit-message-in-english-part2
title: 英語によるコミットメッセージ文例その2
tags: [ english ]
date: 2016-09-22T01:04:10+09:00
lastmod: 2016-09-22T01:04:10+09:00
publishDate: 2016-09-22T01:04:10+09:00
---

　英語でコミットメッセージを書くときにうまい表現が思い浮かばずに困ることがあるので、色々なリポジトリを見て使えそうな表現をメモしていこうという記事です。

　今回は[torvalds/linux](https://github.com/torvalds/linux)より。コミットメッセージは動詞で始めて、また最初を大文字にはせず、文末のピリオドは無しというスタイルです（そこそこ例外あり）。

## Check for 〜


　〜をチェックする（[mm: usercopy: Check for module addresses](https://github.com/torvalds/linux/commit/aa4f0601115319a52c80f468c8f007e5aa9277cb)）

## Duplicate 〜


　〜を複製する（[cgroup: duplicate cgroup reference when cloning sockets](https://github.com/torvalds/linux/commit/d979a39d7242e0601bf9b60e89628fb8ac577179)）

## Don't clear 〜


　〜を消去しない（[mem-hotplug: don't clear the only node in new_node_page()](https://github.com/torvalds/linux/commit/9bb627be47a574b764e162e8513d5db78d49e7f5)）

## Only use〜


　〜だけを使う（[drm: Only use compat ioctl for addfb2 on X86/IA64](https://github.com/torvalds/linux/commit/47a66e45d7a7613322549c2475ea9d809baaf514)）

## A be not supported


　Aはサポートされない（[IB/mlx4: Diagnostic HW counters are not supported in slave mode](https://github.com/torvalds/linux/commit/69d269d38910e697e461ec5677368f57d2046cbe)）。珍しく名詞から始まっているコミット。

## Don't allow 〜


　〜を許可しない（[IB/ipoib: Don't allow MC joins during light MC flush](https://github.com/torvalds/linux/commit/344bacca8cd811809fc33a249f2738ab757d327f)）

## Do validate 〜


　〜を検証する（[perf/x86/intel/pt: Do validate the size of a kernel address filter](https://github.com/torvalds/linux/commit/1155bafcb79208abc6ae234c6e135ac70607755c)）

## Ignore 〜


　〜を無視する（[drm/i915: Ignore OpRegion panel type except on select machines](https://github.com/torvalds/linux/commit/ea54ff4008892b46c7a3e6bc8ab8aaec9d198639)）

## Require 〜


　〜を必要とする（[fscrypto: require write access to mount to set encryption policy](https://github.com/torvalds/linux/commit/ba63f23d69a3a10e7e527a02702023da68ef8a6d)）

## Do not register 〜


　〜を登録しない（[dwc_eth_qos: do not register semi-initialized device](https://github.com/torvalds/linux/commit/47b02f7294a483387772a46931da942b2ca9d845)）

## Remove 〜


　〜を取り除く（[nfp: remove linux/version.h includes](https://github.com/torvalds/linux/commit/312fada1f9f87fb55ace4b5a55a70a9eea5100fd)）

## Drop support for 〜


　〜のサポートをやめる（[nfp: drop support for old firmware ABIs](https://github.com/torvalds/linux/commit/313b345cbff566340022c82267a377e1e493ef90)）

