import streamlit as st

#Config page
menu_items={
    'About': 'https://nicoarbar.github.io/proc_doc/',
    'Report a bug': 'https://github.com/nicoarbar/proc_doc/issues'
}
st.set_page_config(page_title='Proc Doc Home', 
                   page_icon='static/pd32.png', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=menu_items)

#Title
st.title("Proc Doc")
st.sidebar.image('static/pd32.png')
st.text("Welcome to automatic document processing")
st.caption("Proc Doc allows you to input documents and automate the process of formatting them with parameters of your choice.")

#Start
st.subheader('Start')
st.page_link('pages/1_format.py', label = '     Format Documents', icon=":material/file_open:")
st.page_link('pages/2_gpt.py', label = '        Ask Gpt', icon=":material/forum:")
st.page_link('pages/3_indexing.py', label = '       Index Documents', icon=":material/folder_open:")

#About
st.subheader('About')
tab1, tab2, tab3 = st.tabs(["Developer", "Pricing", "Issues"])
with tab1:
    st.info("This app is developed here as an Open Source project:")
    tab1.write("https://nicoarbar.github.io/proc_doc/")  
with tab2:
    st.info("As an Open Source project you are welcome to contribute with donations as a Github Sponsor here:")
    st.write("https://github.com/nicoarbar/proc_doc")
with tab3:
    st.info("For any inquiries, issues, changes and feature requests please reach out here:")
    st.write("https://github.com/nicoarbar/proc_doc/issues")