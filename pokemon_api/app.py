import streamlit as st
from logic.poke_logic import get_pokemon_info, save_search_history
import pandas as pd

st.title("ポケモン図鑑アプリ")
st.write("ポケモンの名前を入力すると、情報を表示します。")

pokemon_name = st.text_input("ポケモン名（英語）\n 例: pikachu")

if st.button("検索"):
    if pokemon_name:
        data = get_pokemon_info(pokemon_name.lower())
        if data:
            if data["image_url"]:
                st.image(data["image_url"], width=200)
            else:
                st.warning("画像が見つかりませんでした。")
            st.markdown(f"### 名前: {data['name'].title()}")
            st.markdown(f"**タイプ:** {', '.join(data['types'])}")
            st.markdown("**基本ステータス**")
            st.json(data["stats"])
            save_search_history(data['name'])
        else:
            st.error("ポケモンが見つかりませんでした。")
    else:
        st.warning("名前を入力してください。")

st.markdown("---")
st.markdown("### 🔎 最近の検索履歴")

try:
    history_df = pd.read_csv("data/search_history.csv", header=None, names=["名前"])
    # 🔽 ここで重複を除く処理（後ろの方を優先して残す）
    history_df.drop_duplicates(subset="名前", keep="last", inplace=True)
    st.dataframe(history_df.tail(10))  # 最新の10件（重複なし）
except FileNotFoundError:
    st.info("まだ検索履歴はありません。")
