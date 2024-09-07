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

#Logo
st.logo("static/pd32.png", icon_image="static/pd32.png")

pages = {
    "Home": [st.Page("pages/5home.py", title="Home", icon=":material/home:")],
    "Start": [
        st.Page("pages/1format_document.py", title="Format Document", icon=":material/file_open:"),
        st.Page("pages/2ask_gpt.py", title="Ask Gpt", icon=":material/forum:"),
        st.Page("pages/3indexing_documents.py", title="Index Documents", icon=":material/folder_open:")
    ],
    "About": [
        st.Page("pages/4info.py", title="Learn about us", icon=":material/info:")
    ]
}

pg = st.navigation(pages)
pg.run()
