import streamlit as st

#Logo
st.logo("static/pd32.png", icon_image="static/pd32.png")

#Title
st.title("Proc Doc")
st.text("Welcome to automatic document processing")
st.caption("Proc Doc allows you to input documents and automate the process of formatting them with parameters of your choice.")

#Start
st.subheader('Start')
st.page_link('tabs/1format_document.py', label = '     Format Document', icon=":material/file_open:")
st.page_link('tabs/2ask_gpt.py', label = '        Ask Gpt', icon=":material/forum:")
st.page_link('tabs/3indexing_documents.py', label = '       Index Documents', icon=":material/folder_open:")

#About
st.subheader('About')
st.page_link('tabs/4info.py', label = '       Info', icon=":material/info:")