import streamlit as st
from openai import OpenAI

# حط مفتاح OpenAI بتاعك هنا
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.set_page_config(page_title="X Assistant", page_icon="🤖")

st.title("🤖 X Assistant")
st.write("اسأل أي حاجة...")

# حفظ المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل القديمة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# إدخال المستخدم
user_input = st.chat_input("اكتب رسالتك هنا...")

if user_input:
    # عرض رسالة المستخدم
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # رد الذكاء الاصطناعي
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
