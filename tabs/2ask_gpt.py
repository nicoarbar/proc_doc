import streamlit as st
from transformers import pipeline

st.logo("static/pd32.png", icon_image="static/pd32.png")

st.title("Proc Doc")
st.header('Ask GPT')
with st.chat_message("user"):
    st.write("Ask GPT")
    question = st.chat_input("Ask something")
    if question is not None:
        question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
        result_ask = question_answerer(question=question, context="Office documents")
        if result_ask is not None:
            st.write(result_ask['answer'])


with st.chat_message("user"):
    st.write("Summarize")
    summa = st.chat_input("Write anything")
    if summa is not None:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        result_sum = summarizer(summa)
        if result_sum is not None:
            st.text(result_sum['answer'])