---
title: Windows Azureメモその2：Azure Drive
author: hylom
type: post
date: 2012-03-16T13:17:31+00:00
url: /2012/03/16/windows-azureメモその2：azure-drive/
categories:
  - Hacks
tags:
  - azure
  - programming
  - windowsazure

---
　Azure Driveを利用するコード例がいくつかWebにあるのだが、「[Windows Azure アプリケーション開発入門: 第 5 回 Azure ストレージ &#038; Storage Client API を極める][1]」は間違っているので注意。これで1日潰れた。

　全体としては内容はほぼ正しいのだが、最後に紹介されているドライブを作成するコードは現状（Azure SDK 1.6）では正しく動かない。問題の個所は、PageBlobを作成している部分。CloudDrive

<pre>//PageBlobの作成
   pgAzure.Create(nDriveSize * 1024 * 1024);
</pre>

「[Windows Azure 実環境上で CloudDrive の Mount メソッドが Unknown Error を発生させる][2]」で述べられているが、CloudDriveのCreateメソッドを呼ぶ前に利用するBlobを作成していてはダメ。CloudDriveのCreateメソッドではBlobのフォーマット（VHD作成）も行っているため、CloudPageBlobのCreateメソッドでBlobを作成してしまうとマウントできなくなる模様。

 [1]: http://code.msdn.microsoft.com/windowsazure/5-Azure-Storage-Client-API-5710f880
 [2]: http://social.msdn.microsoft.com/Forums/ja-JP/windowsazureja/thread/050a9876-00b2-4df1-9027-3fa56ebfcdb5/
