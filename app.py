import streamlit as st

st.title("Chatbot Saya")

user = st.text_input("Masukkan pertanyaan")

if user:
    st.write("Halo,", user)
