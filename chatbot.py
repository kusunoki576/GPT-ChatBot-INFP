import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたの性格はINFPです"}
    ]


def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("INFP-ChatBot")
st.write("GPT-3.5 / temperature==1.0")

user_input = st.text_input("メッセージを入力", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    # for message in reversed(messages[1:]):  # 直近のメッセージを上に
    for message in messages[1:]:
        speaker = "You"
        if message["role"] == "assistant":
            speaker = "GPT"

        st.write(speaker + ": " + message["content"])
