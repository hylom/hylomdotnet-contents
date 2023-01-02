---
slug: powershell-the-first-step
title: PowerShellはじめの一歩
date: 2023-01-02T17:50:00+09:00
lastmod: 2023-01-02T17:50:00+09:00
publishDate: 2023-01-02T17:50:00+09:00
draft: true
---

　ここ最近、自宅でのメインPCとしてWindows PCを使っています。WindowsのCUI環境と言えば長らくMS-DOSから続く「コマンドプロンプト」だったわけですが、昨今導入されたPowerShellは近代のシェルとして十分な機能を備えており、またWindows TerminalもCUIのためのインターフェイスとしてストレスなく常用できるレベルになっています。

　ということで、PowerShellを本格的に使ってみようということでまずは環境構築から始めてみました。なお、本記事はUNIX系OSで一般的なシェル（bash等）やWindowsのコマンドプロンプトについての知識を持っていることを前提として書いています。

## PowerShellの最新版をインストールする

　PowerShellはWindows 7以降に標準搭載されており、Windows 11/10にはバージョン5.xが同梱されています。いっぽうで現在のPowerShellの最新バージョンはバージョン7系（本記事執筆時点では7.3.1）となっています。ということで、PowerShellを本格的に利用したい場合は、まず最新版のPowerShellをインストールしましょう。PowerShell最新版はMicrosoft Storeで配布されているので、Microsoft Storeアプリを起動して、「powershell」で検索しインストールします。ちなみにPowerShell 7系はPowerShell 5系とは別のバイナリとしてインストールされるため、共存が可能です。

　なお、バージョン5.1系と7系の違いは[こちらの「Windows PowerShell 5.1 と PowerShell 7.x の相違点」ドキュメント](https://learn.microsoft.com/ja-jp/powershell/scripting/whats-new/differences-from-windows-powershell?view=powershell-7.3)にまとめられています。また、Microsoft的にはバージョン5系は「Windows PowerShell」、7系は「PowerShell」（「Windowsが付かない）という呼称になっているようです。

　ちなみに、実行中のPowerShellのバージョンは$PSVersionTableという変数に格納されています。

```
> $PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.22000.1335
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.22000.1335
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```

　PowerShellでは「$」で始まる文字列が変数となり、変数をシェル上で評価するとその中身が表示されます。つまり、上記は「$PSVersionTable」という変数の中身を表示させていることになります。

### スクリプトの実行セキュリティポリシー

　Windows 11/10に同梱されているPowerShell 5.1は、デフォルトではスクリプトの実行が一切できない設定になっています。これはセキュリティ強化のためと思われます。実際、Windows環境においてはマルウェアがPowerShellスクリプトを使って攻撃を行う事例が多数確認されています。そのため、PowerShell 5.1でスクリプトを実行させたい場合、明示的に実行ポリシーを変更する必要があります。いっぽう、Microsoft StoreからインストールしたPowerShell 7系はローカルマシン上にあるスクリプトについてデフォルトで実行可能な設定になっており、特に設定を変更せずに作成したスクリプトを実行できます（参考資料：[about Execution Policies](https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3)）。


## Windows Terminalのデフォルトシェルを変更する

　前述のように、Microsoft StoreからPowerShell 7系をインストールしたあともPowerShell 5.1はシステムにそのまま残されています。そのため、Windows Terminalを起動した際にデフォルトのシェルとしてPowerShell 7系を利用するためには、Windows Terminalの設定を明示的に変更する必要があります。PowerShell 7系をインストールすると「PowerShell」というプロファイルがWindows Terminalに追加されるので、これを既定のプロファイルに設定しておきましょう。

![「既定のプロファイル」設定](/2023/01/02/terminal_conf.png "「既定のプロファイル」設定")

## コマンドを確認する

　PowerShellでは、「動詞-ターゲット」というフォーマットでさまざまなコマンドが定義されています。たとえば利用できるコマンド一覧は、「Get-Command」というコマンドで表示できます。

```
> Get-Command

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           Add-AppPackage                                     2.0.1.0    Appx
Alias           Add-AppPackageVolume                               2.0.1.0    Appx
Alias           Add-AppProvisionedPackage                          3.0        Dism
：
：
```

　また、UNIX系OSにおけるmanコマンドに相当するのが「help」コマンドです。

```
> help Get-Command

NAME
    Get-Command

SYNTAX
    Get-Command [[-ArgumentList] <Object[]>] [-Verb <string[]>] [-Noun <string[
    ]>] [-Module <string[]>] [-FullyQualifiedModule <ModuleSpecification[]>] [-
    TotalCount <int>] [-Syntax] [-ShowCommandInfo] [-All] [-ListImported] [-Par
    ameterName <string[]>] [-ParameterType <PSTypeName[]>] [<CommonParameters>]

    Get-Command [[-Name] <string[]>] [[-ArgumentList] <Object[]>] [-Module <str
    ing[]>] [-FullyQualifiedModule <ModuleSpecification[]>] [-CommandType {Alia
    s | Function | Filter | Cmdlet | ExternalScript | Application | Script | Co
    nfiguration | All}] [-TotalCount <int>] [-Syntax] [-ShowCommandInfo] [-All]
     [-ListImported] [-ParameterName <string[]>] [-ParameterType <PSTypeName[]>
    ] [-UseFuzzyMatching] [-UseAbbreviationExpansion] [<CommonParameters>]


PARAMETERS
    -All
：
：
ALIASES
    gcm

REMARKS
    Get-Help cannot find the Help files for this cmdlet on this computer. It is
     displaying only partial help.
        -- To download and install Help files for the module that includes this
     cmdlet, use Update-Help.
        -- To view the Help topic for this cmdlet online, type: "Get-Help Get-C
    ommand -Online" or
           go to https://go.microsoft.com/fwlink/?LinkID=2096579.
```

　一部のコマンドには短いエイリアスが設定されており、`help`コマンドの出力結果の「ALIASES」でエイリアスを確認できます。たとえば`Get-Command`の場合、「gcm」でも同じ処理が実行できます。

　`help`コマンドに引数として与えた文字列に一致するコマンドが存在しない場合、その文字列を含むコマンド一覧が検索されて表示されます。

```
> help Get

Name                              Category  Module                    Synopsis
----                              --------  ------                    --------
Get-PSSessionCapability           Cmdlet    Microsoft.PowerShell.Core …
Get-PSSessionConfiguration        Cmdlet    Microsoft.PowerShell.Core …
：
：
```

## PowerShellの起動時に処理を実行する

　UNIX系のシェルでは、起動時にあらかじめ指定しておいた処理を実行することができます。たとえばbashの場合、ホームディレクトリの「.bashrc」や「.profile」といったスクリプトが自動的に実行されます。PowerShellでも同様の仕組みがあり、実行されるスクリプトのパスは「$profile」変数に格納されています。PowerShell 7系のデフォルトではユーザーディレクトリ下の「Documents\PowerShell\Microsoft.PowerShell_profile.ps」に設定されています。

```
> $profile
C:\Users\hylom\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

　デフォルトでは`Documents\PowerShell`ディレクトリは存在しないので、必要に応じてこのディレクトリも作成する必要があります。具体的には、PowerShell上で次のように実行します。

```
> ni (Split-Path $profile -Parent) -ItemType Directory

    Directory: C:\Users\hylom\Documents

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          2023/01/02     0:23                PowerShell
```

　「ni」は「New-Item」コマンドのエイリアスで、「-ItemType」オプションで「Directory」を指定することで、指定したディレクトリを作成できます。また、`ni`に続く括弧は、bashにおける「$()」に相当するもので、これを利用して括弧内の実行結果を別のコマンドの引数として与えることができます。括弧内の「Split-Path」はUNIX系OSで言うところの`dirname`コマンドや`basename`コマンドに相当するコマンドで、「-Parent」オプションを指定すると指定したパス文字列の親ディレクトリを返します。つまり、このコマンドは$profile変数に格納されているパスの親ディレクトリを作成する、というものになります。

　続いて次のように`ni`コマンドを実行してスクリプトファイルを作成し、続いて適当なエディタでファイルを編集します。

```
> ni $profile -ItemType file

    Directory: C:\Users\hylom\Documents\PowerShell

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          2023/01/02     0:23              0 Microsoft.PowerShell_profile.ps1
```

## PowerShellのショートカットキーを変更する

　bash等のUNIX系シェルでは、デフォルトではEmacs風のショートカットキーが利用できます。たとえばCtrl-hでbackspace、Ctrl-pやCtrl-nで履歴を遡ったり進んだりすることができます。一方、PowerShellのデフォルト設定ではまったく異なるショートカットキーが設定されており、UNIX系シェルに慣れた者としては非常に混乱します。

　PowerShellでは、「PSReadLine」というモジュールでコマンドライン編集を行っています（ドキュメント：[about PSReadLine](https://learn.microsoft.com/ja-jp/powershell/module/psreadline/about/about_psreadline?view=powershell-7.3)）。このPSReadLineの設定を変更することで、ショートカットキーやコマンドライン編集の挙動をカスタマイズできます。

　現在設定されているショートカットキー一覧は、「Get-PSReadLineKeyHandler」で確認できます。


```
> Get-PSReadLineKeyHandler

Basic editing functions
=======================

Key              Function            Description
---              --------            -----------
Enter            AcceptLine          Accept the input or move to the next line
                                     if input is missing a closing token.
Shift+Enter      AddLine             Move the cursor to the next line without a
                                     ttempting to execute the input
：
：
```

　また、ショートカットキーの変更は「Set-PSReadlineKeyHandler」コマンドで行えます。

```
Set-PSReadlineKeyHandler -Key '＜設定するキー＞' -Function ＜割り当てる挙動＞
```

　たとえば`C:\Users\＜ユーザー名＞\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`ファイルに次のように記述すれば、カーソル移動や履歴移動、コピー＆ペーストなどをEmacs風のキーバインドで実行できるようになります。

```
Set-PSReadlineKeyHandler -Key 'Ctrl+b' -Function BackwardChar
Set-PSReadlineKeyHandler -Key 'Ctrl+f' -Function ForwardChar
Set-PSReadlineKeyHandler -Key 'Ctrl+d' -Function DeleteChar
Set-PSReadlineKeyHandler -Key 'Ctrl+h' -Function BackwardDeleteChar
Set-PSReadlineKeyHandler -Key 'Ctrl+p' -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key 'Ctrl+n' -Function HistorySearchForward
Set-PSReadlineKeyHandler -Key 'Ctrl+a' -Function BeginningOfLine
Set-PSReadlineKeyHandler -Key 'Ctrl+e' -Function EndOfLine
Set-PSReadlineKeyHandler -Key 'Ctrl+k' -Function ForwardDeleteLine
Set-PSReadlineKeyHandler -Key 'Ctrl+y' -Function Paste
Set-PSReadlineKeyHandler -Key 'Ctrl+w' -Function Cut
```

## Visual StudioのDeveloper PowerShellをバージョン7系にする

　Visual Studioをインストールしていると、Windows Terminalのプロファイルとして「Developer PowerShell for ＜Visual Studioのバージョン＞」というものが自動的に追加されます。これはその名の通り、Visual Studioの各ツールを利用するための設定がされた環境でPowerShellを起動するためのプロファイルですが、PowerShell 7系をインストールしても、デフォルトではこのプロファイルはPowerShell 5系を引き続き利用するようです。

　このプロファイルでPowerShell 7系を利用するには、まずPowerShell 7系のプロファイルから「コマンドライン」（「"C:\Users\＜ユーザー名＞\AppData\Local\Microsoft\WindowsApps\Microsoft.PowerShell_8＜ユニーク文字列＞\pwsh.exe"）文字列をコピーし、Develper PowerShell用プロファイルのコマンドライン文字列内の「powershell.exe」をこの文字列で置き換えればOKです。

![「Developer PowerShell」のコマンドライン設定](/2023/01/02/dev_sh.png "「Developer PowerShell」のコマンドライン設定")
