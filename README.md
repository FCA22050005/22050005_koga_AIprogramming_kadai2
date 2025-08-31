

# ポケモン図鑑アプリ（AIプログラミング課題2）

## 概要

このアプリは、PokeAPIを利用してポケモンの情報を検索・表示するWebアプリです。  
ユーザーがポケモン名を入力すると、以下の情報を表示します：

- ポケモンの画像
- タイプ（例：でんき）
- 基本ステータス（HP、こうげき、ぼうぎょなど）
- 検索履歴（CSVに保存）

---

### 使用API

- [PokeAPI](https://pokeapi.co/)  
  → APIキー不要で利用できる、無料のポケモン情報API

### 使用ライブラリ

- `streamlit`：WebアプリのUI構築
- `requests`：APIへのアクセス
- `pandas`：履歴のCSV表示
- `csv`：履歴保存に使用

---

## ファイル構成

├── app.py # Streamlitアプリ本体
├── logic/
│ └── poke_logic.py # API通信・CSV保存ロジック
├── data/
│ └── search_history.csv # 検索履歴（実行時に自動作成）
├── README.md # このファイル
├── requirements.txt # 必要パッケージ一覧

## システム設計図
![System Diagram](pokemon_api/images/system_diagram.png)

## コード説明図
![Code Diagram](pokemon_api/images/code_diagram.png)

## メモ　これを課題１のところに書く
- アプリURL: https://22050005kogaaiprogrammingkadai2-6xbbidsvoub5kw9bls39bc.streamlit.app/
- GitHub URL: https://github.com/FCA22050005/22050005_koga_AIprogramming_kadai2?tab=readme-ov-file
- 加点の有無: 有り（Anaconda promptからサイトを立ち上げないとCSVに保存されません。）
- その他コメント： ポケモンのAPIでポケモン検索ができることにびっくりしました。ただ、検索を英語の名前じゃないといけないのが不便です。まだ前期の授業は終わっていませんが今のところ先生に質問しまくることでギリギリついて行けていると思ってます。難しいですけど楽しいです！

## 動かすとき

1. cd C:\pokemon_api
↑　Dドライブにこのファイルがあるなら、cd D:\pokemon_api です。
2. streamlit run app.py

## 課題３　ポケモンアプリの改善案
-improvement.mdへのリンク：https://github.com/FCA22050005/22050005_koga_AIprogramming_kadai2/blob/main/improvement.md
