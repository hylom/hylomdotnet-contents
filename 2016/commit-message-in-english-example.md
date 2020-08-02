---
slug: commit-message-in-english-example
title: 英語によるコミットメッセージ文例その1
tags: [ english,deveploer ]
date: 2016-09-21T01:20:38+09:00
lastmod: 2016-09-22T01:04:43+09:00
publishDate: 2016-09-21T01:20:38+09:00
---

　英語でコミットメッセージを書くときにうまい表現が思い浮かばずに困ることがあるので、色々なリポジトリを見て使えそうな表現をメモしていこうという記事です。

　今回は[WordPress/WordPress](https://github.com/WordPress/WordPress)より。コミットメッセージは動詞で始め、最後にピリオドを付けるというスタイルです。

## Correct 〜


　〜を修正する（[Docs: Correct the description of `{$taxonomy}_term_new_form_tag` hook, making it more consistent with other `*_form_tag` hooks.](https://github.com/WordPress/WordPress/commit/3c5204f9f481e6839f60ee50e17c1551b6234f2b)）。

## Make A 〜


　Aを〜にする（[Media: Make media library searchable by filename.](https://github.com/WordPress/WordPress/commit/8f36a570cbebf537b6c58f766986caa9bbdba48a)）。続く説明文で使われているapply A to B（AをBに適用する）も使えそう。

## Let A be 〜


　Aを〜にする（[Customize: Let `static_front_page` section be contextually active based on whether there are any published pages.](https://github.com/WordPress/WordPress/commit/d84c343cc6194950373678678a2020a070d8ed72)）。

## Avoid 〜


　〜を回避する（[XML-RPC: Avoid a PHP notice in `::pingback_ping()` if page title was not found.](https://github.com/WordPress/WordPress/commit/788c3680f90b7570f8f9b5277f5d6bf57d7d9209)）。

## Ensure 〜


　〜を確実にする（[Customize: Ensure nav menu items lacking a label use the title from the original object.](https://github.com/WordPress/WordPress/commit/037a236e423d0a38d00767f0659b0837116dde27)）。

## Improve 〜


　〜を改良する（[Media: Improved media titles when created from filename.](https://github.com/WordPress/WordPress/commit/405def3da40f9090361d9be9ad94b51a8fbe3f2d)）。

## Enable A to 〜


　〜するようAを有効にする（[REST API: Enable sanitize_callback to return WP_Error.](https://github.com/WordPress/WordPress/commit/794dd5d8cb7d3f11779cb86d1eff66fbd1947840)）。

## Adjust 〜


　〜を調整する（[Media: Adjust `test_video_shortcode_body()` after ［38597］.](https://github.com/WordPress/WordPress/commit/84cf528449e831412ad3405ea50fedcb745420ae)）。

## Implement 〜


　〜を実装する（[Customize: Implement previewing of form submissions which use the GET method.](https://github.com/WordPress/WordPress/commit/edf170c943cfcfa122565c8f30c8b807e44e4dac)）。

## Eliminate 〜


　〜を取り除く（[Query: Eliminate unnecessary `wp_list_filter()` call in `get_queried_](https://github.com/WordPress/WordPress/commit/132f3d0d19743a28dc97ee8ec868f07aa534cbdc)）。

## Prevent A from 〜


　Aを〜から防ぐ（[Menus: Prevent non-published posts/pages from being returned in search results for adding as nav menu items](https://github.com/WordPress/WordPress/commit/84f9592f88a19dd3fb4d1b8780679c99ea678688)）。

## Sanitize 〜


　〜をサニタイズする。サニタイズは不要な情報を取り除くこと（[Media: Sanitize upload filename.](https://github.com/WordPress/WordPress/commit/c9e60dab176635d4bfaaf431c0ea891e4726d6e0)）。

## Split 〜


　〜を分割する（[Role/Capability: Split meta and primitive capabilities in the helper functions in the roles and capability tests so primitive capability tests can be made more accurate.](https://github.com/WordPress/WordPress/commit/9cf899d6f9e6ffc5fde7f3bb0b1aeb7012ae8cad)）

## Deprecate 〜


　〜を廃止する（[Multisite: Deprecate `wp_get_network()`.](https://github.com/WordPress/WordPress/commit/58bca4922709aae51a50646796c86895e0035265)）。

## Don't do 〜


　〜しないようにする（[Comments: Don't do direct SQL query when fetching decendants.](https://github.com/WordPress/WordPress/commit/3a4169d7abe25dafc676eee6668d2d1851882c6b)）。

