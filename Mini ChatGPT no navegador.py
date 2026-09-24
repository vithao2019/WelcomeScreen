import streamlit as st

st.title("ChatGPT do Victor")

pergunta = st.text_input("Pergunte algo")

if pergunta:
    st.write(f"Você perguntou: {pergunta}")

