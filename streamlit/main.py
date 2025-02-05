import streamlit as st

import vertex

def main():
    st.title("💬 健康管理アプリ")
    st.caption("🚀 今日の活動量を評価してもらおう！")

    with st.form(key="input_form"):
        water = st.number_input(
            "水分摂取量(ml)",
            min_value=0,
            max_value=10000,
            value=0
        )

        weight = st.number_input(
            "体重(kg)",
            min_value=0,
            max_value=150,
            value=0
        )

        steps = st.number_input(
            "歩数",
            min_value=0,
            max_value=100000,
            value=0
        )

        submit_button = st.form_submit_button("評価する")

    if submit_button:
        if water and steps:
            response = vertex.ask_ai(steps, water, weight)
            st.text(response.text)
        else:
            st.error("水分摂取量と歩数を入力してください")

if __name__ == '__main__':
    main()
