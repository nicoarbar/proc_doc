import streamlit as st

#Config page
menu_items={
    'About': 'https://nicoarbar.github.io/proc_doc/',
    'Report a bug': 'https://github.com/nicoarbar/proc_doc/issues'
}
st.set_page_config(page_title='Proc Doc Home', 
                   page_icon='static/pd32.png', 
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   menu_items=menu_items)

#st.session_state.
st.logo("static/pd32.png", icon_image="static/pd32.png")

#Title
st.title("Proc Doc")
st.text("Welcome to automatic document processing")
st.caption("Proc Doc allows you to input documents and automate the process of formatting them with parameters of your choice.")

#Start
st.subheader('Start')
st.page_link('pages/1format_document.py', label = '     Format Document', icon=":material/file_open:")
st.page_link('pages/2ask_gpt.py', label = '        Ask Gpt', icon=":material/forum:")
st.page_link('pages/3indexing_documents.py', label = '       Index Documents', icon=":material/folder_open:")

#About
st.subheader('About')
st.page_link('pages/4info.py', label = '       Info', icon=":material/info:")
