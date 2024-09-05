import pandas as pd
from datetime import datetime
from src.doc_funcs import *
from io import StringIO

#Config page
menu_items={
    'About': 'https://nicoarbar.github.io/proc_doc/',
    'Report a bug': 'https://github.com/nicoarbar/proc_doc/issues'
}
st.set_page_config(page_title='Proc Doc', 
                   page_icon='static/pd32.png', 
                   layout="wide", 
                   initial_sidebar_state="expanded", 
                   menu_items=menu_items)

#Title
st.title("Proc Doc")
st.caption("Proc Doc allows you to input documents and automate the process of formatting them with parameters of your choice.")
st.header("Start")

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
tab11, tab12, tab13= st.tabs(["Format docs with parameters", "Ask GPT", "Index docs for info retrieval"])

#Actions
with tab13:
    st.error('Feature under construction')

with tab12:
    with st.chat_message("user"):
        st.write("Ask GPT")
        prompt = st.chat_input("Say something")
        if prompt is not None:
            st.error(f"Feature under construction. Get back to you soon with: {prompt}")
        else:
            st.error(f"Feature under construction.")

with tab11:
    
    #Params doc
    st.subheader('1. Choose parameters from a template or input them')
    action_params = st.radio('', ['Input parameters manually', 'Upload csv file with parameters'],
                             label_visibility= 'collapsed')

    if action_params == 'Input parameters manually':
        st.warning('Update the parameters (autosave)')
        df = pd.DataFrame(columns=['Parameters', 'Value'])
        updf = st.data_editor(data=df, hide_index=True, num_rows="dynamic")
    
        # Download template
        disabled = True
        if len(updf) > 1:
            disabled = False

        csv_buffer = StringIO()
        updf.to_csv(csv_buffer, index=False)
        csv_string = csv_buffer.getvalue()

        st.download_button('Download template', csv_string, file_name='proc_doc_template.csv', disabled = disabled)

    else:
        df = streamlit_upload('Upload csv file', 'Update the parameters', pd.read_csv)
        if df is not None:
            updf = st.data_editor(data=df, hide_index=True, num_rows="dynamic")

    #Date
    st.subheader('2. Choose a date')
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
    st.subheader('3. Upload your document to format')
    doc_content = streamlit_upload('Upload document', 'File uploaded correctly', read_docx)

    #Press Process
    st.subheader('4. Process the documents')
    disabled_process = True
    if doc_content is not None:
        disabled_process = False
    press_process = st.button('Process the documents', disabled=disabled_process)

    #TODO
    if press_process:
        doc_content1 = 'test'
    else:
        doc_content1 = 'error'


    #Finish
    st.subheader('5. Finish')
    # Display document
    press_display = st.button('Display document', disabled=disabled_process)
    if press_display:
        st.success(doc_content1)

    # Download document
    disabled_down = True
    proc_doc_filename = st.text_input('Enter name of the file to be downloaded')
    if len(proc_doc_filename) > 1:
        disabled_down = False
    if doc_content1 is not None:
        st.download_button('Download document', doc_content1, file_name=proc_doc_filename, disabled = disabled_down)