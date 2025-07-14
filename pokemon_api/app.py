import streamlit as st
from logic.poke_logic import get_pokemon_info, save_search_history

st.title("ポケモン図鑑アプリ")
st.write("ポケモンの名前を入力すると、情報を表示します。")

pokemon_name = st.text_input("ポケモン名（例: pikachu）")

if st.button("検索"):
    if pokemon_name:
        data = get_pokemon_info(pokemon_name.lower())
        if data:
            st.image(data["image_url"], width=200)
            st.markdown(f"### 名前: {data['name'].title()}")
            st.markdown(f"**タイプ:** {', '.join(data['types'])}")
            st.markdown("**基本ステータス**")
            st.json(data["stats"])
            save_search_history(data['name'])  # 加点用
        else:
            st.error("ポケモンが見つかりませんでした。")
    else:
        st.warning("名前を入力してください。")
