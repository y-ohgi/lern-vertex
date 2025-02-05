import streamlit as st

import vertex

def main():
    st.title("💬 健康管理アプリ")
    st.caption("🚀 今日の活動量を評価してもらおう！")

    with st.form(key="input_form"):
        water = st.number_input(
            "水分摂取量",
            min_value=0,
            max_value=10000,
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
            response = vertex.ask_ai(steps, water)
            st.text(response.text)
        else:
            st.error("水分摂取量と歩数を入力してください")

if __name__ == '__main__':
    main()


# # ユーザー入力の取得
# prompt = st.text_input("Your message:")

# if prompt:
#     # ユーザー入力をセッション状態に追加
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     # Gemini APIを使って応答を生成
#     response = vertex.ask_ai(1000, 2000)

#     # 応答をテキストとして取得（ここではresponse.textと仮定）
#     assistant_response = response.text

#     # 応答をセッション状態に追加し、表示
#     st.session_state.messages.append({"role": "assistant", "content": assistant_response})
#     st.text(f"Assistant: {assistant_response}")
