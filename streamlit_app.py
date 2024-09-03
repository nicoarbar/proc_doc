import pandas as pd
from datetime import datetime
from src.doc_funcs import *

#Config page
menu_items={
    'About': 'https://nicoarbar.github.io/proc_doc/',
    'Report a bug': 'https://github.com/nicoarbar/proc_doc/issues'
}
st.set_page_config(page_title='Proc Doc', 
                   page_icon='static/proc_doc.png', 
                   layout="wide", 
                   initial_sidebar_state="expanded", 
                   menu_items=menu_items)

#Title
st.title("Proc Doc")
st.text("Welcome to simple automatic document processing")
st.caption("Proc Doc allows you to input documents and automate the process of formatting them with parameters of your choice.")

#Selection of Action
with st.sidebar:
    st.title('What do you want to do?')
    action = st.radio('', 
                      ['Format docs with parameters', 
                      'Ask GPT', 
                      'Index docs for info retrieval'],
                      label_visibility= 'collapsed')
#About
with st.sidebar:
    st.title('About')
    tab1, tab2, tab3, tab4 = st.tabs(["Developer", "Pricing", "Issues", "Beta"])
    with tab1:
        st.info("This app is developed here as an Open Source project:")
        tab1.write("https://nicoarbar.github.io/proc_doc/")  
    with tab2:
        st.info("As an Open Source project you are welcome to contribute with donations as a Github Sponsor here:")
        st.write("https://github.com/nicoarbar/proc_doc")
    with tab3:
        st.info("For any inquiries, issues, changes and feature requests please reach out here:")
        st.write("https://github.com/nicoarbar/proc_doc/issues")
    with tab4:
        st.info("""Proc Doc is under construction""")
        st.markdown("""
        **Features under construction:**
        - Ask GPT
        - Indexing docs for info retrieval
        - varias filas insertarlas en el documento
        - linkar con otros documentos
        - estrategia para standarizar automatizacion para cualquier documento legal
        - Setting pricing in Github Sponsor and Buy me a Coffee page
        - Allow user to add issues, feature request on Github Issues
        """) 

#Show selection
st.info(action)

#Actions
if action == 'Index docs for info retrieval':
    st.error('Feature under construction')

elif action == 'Ask GPT':
    with st.chat_message("user"):
        st.write("Ask GPT")
        prompt = st.chat_input("Say something")
        if prompt is not None:
            st.error(f"Feature under construction. Get back to you soon with: {prompt}")
        else:
            st.error(f"Feature under construction.")

elif action == 'Format docs with parameters':
    
    #Params doc
    st.subheader('Choose parameters from a template or input them')
    action_params = st.radio('', ['Input parameters manually', 'Upload csv file with parameters'],
                             label_visibility= 'collapsed')

    if action_params == 'Input parameters manually':
        st.warning('Update the parameters (autosave)')
        df = pd.DataFrame(columns=['Parameters', 'Value'])
        updf = st.data_editor(data=df, hide_index=True, num_rows="dynamic")
    else:
        df = streamlit_upload('Upload csv file', 'Update the parameters', pd.read_csv)
        if df is not None:
            updf = st.data_editor(data=df, hide_index=True, num_rows="dynamic")

    #Date
    st.subheader('Choose a date')
    date_doc = current_date_format(datetime.now())
    action_date = st.radio('', 
                           [f'Choose current date in spanish: **{date_doc}**', 
                            'Input date from calendar', 
                            'Input your own date format'], 
                            label_visibility= 'collapsed')
    if action_date == 'Input date from calendar':
        date_doc = st.date_input('Date')
    elif action_date == 'Input your own date format':
        date_doc = st.text_input('Input your own date format')
    else:
        date_doc = current_date_format(datetime.now())

    #Template doc
    st.subheader('Upload your document to format')
    doc_content = streamlit_upload('Upload document', 'File uploaded correctly', read_docx)

    #Press Process
    #TODO
    st.subheader('Process the documents')
    streamlit_button('Format the documents', 1, on_click=None)
    

    #Finish
    st.subheader('Finish')
    tab1, tab2 = st.tabs(['Download processed document','Display processed document'])
    proc_doc_file = 'TODO'
    with tab1:
        #Press download
        proc_doc_filename = st.text_input('Enter name of the file to be downloaded')
        if proc_doc_file is not None:
            st.download_button('Download document', proc_doc_file, file_name=proc_doc_filename)
    with tab2:
        #Display document
        if proc_doc_file is not None:
            st.text(proc_doc_file)