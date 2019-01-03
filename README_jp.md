# Maya_CustomObjectViewer  

目次
-----------------

  * [Description](#description)  
  * [Requirement](#requirement)  
  * [Infomation about Python Script](#infomation-about-python-script)  
  * [Install](#install)  
  * [Usage](#usage)  
  * [License](#license)  
  * [Author](#author)  

Description  
------------  
## 解説
このツールはMaya用のカスタム オブジェクト ビュアーです。  

![custom_objectviewer](https://user-images.githubusercontent.com/29208747/50638515-5f07aa80-0fa1-11e9-80cb-6391467b83df.jpg)  

Requirement  
------------  
## 必要条件
 Maya 2015 以上  


Infomation about Python Script
------------
## スクリプトについて
このツールはSoftimage XSIに実装されていた Object View のMaya版を真似ており、  
最初に選択したオブジェクトをずっと表示しているWindowを作成してくれるものです。  


Install  
------------  
## インストール  

1,  
ri_custom_objectviewer.py をMayaのスクリプトエディターにドラッグ＆ドロップし、  
```py
object_view_menu()   
```
を最後の行に追加し、全てを選択して、Maya のシェルフボタンをPythonの種類で作成します。  

あるいは  

2,  
Maya のパスが通ったディレクトリーに ri_custom_objectviewer.py をコピーし、  

最後の行に  

```py
object_view_menu()  
```
を用いて起動します。  


Usage  
------------  
## 使い方  

### SUITE USERS NOTE　のWebサイトをご覧ください。
  https://www.comtec.daikin.co.jp/DC/UsersNotes/Ritaro/tutorial/maya_13/index.html  


Licence  
------------  
## ライセンス  
[MIT] (https://github.com/O-Ritaro/Maya_CustomObjectViewer/blob/master/LICENSE)  

Author  
------------  
## 記載者  
Ritaro (https://github.com/O-Ritaro)  