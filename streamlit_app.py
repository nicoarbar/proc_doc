import pandas as pd
from src.doc_funcs import *

#Title
st.title("Proc Doc")
st.text("Welcome to simple automatic document processing")
st.caption("""Proc Doc allows you to input documents and 
           automate the process of formatting them with parameters of your choice.""")

#Selection of Action
with st.sidebar:
    st.title('What do you want to do?')
    action = st.radio('Choose:', 
                      ['Format docs with parameters', 
                      'Ask GPT', 
                      'Index docs for info retrieval', 
                      'Other'])
#About
with st.sidebar:
    st.title('About')
    tab1, tab2, tab3, tab4 = st.tabs(["Developer", "Pricing", "Issues", "Beta"])
    with tab1:
        st.warning("This app is developed here as an Open Source project:")
        tab1.write("https://nicoarbar.github.io/proc_doc/")  
    with tab2:
        st.warning("Being an Open Source project you are welcome to contribute with donations as a Github Sponsor here:")
        st.write("https://github.com/nicoarbar/proc_doc")
        st.warning("Or you can buy me a coffee here:")
        st.write("https://buymeacoffee.com/")
        st.warning("Or thank me here:")
        st.write("https://thanks.dev/home")
    with tab3:
        st.warning("For any inquiries, issues, changes and feature requests please reach out here:")
        st.write("https://github.com/nicoarbar/proc_doc/issues")
    with tab4:
        st.warning("""Proc Doc is under construction""")
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

elif action == 'Other':
    st.multiselect('Multiselect', [1,2,3])
    st.text_input('Enter some text')
    st.date_input('Date input')

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
    action_params = st.radio('Choose:', ['Input parameters manually', 'Upload csv file with parameters'])

    if action_params == 'Input parameters manually':
        st.info('Update the parameters')
        df = pd.DataFrame(columns=['Parameters', 'Value'])
        updf = st.data_editor(data=df, hide_index=True, num_rows="dynamic")
    else:
        df = streamlit_upload('Upload csv file', 'Update the parameters', pd.read_csv)
        if df is not None:
            updf = st.data_editor(data=df, hide_index=True, num_rows="dynamic")
    
    #Press saving parameters
    streamlit_button('Save parameters', 1, on_click=None)

    #Template doc
    st.subheader('Upload your document to format')
    doc_content = streamlit_upload('Upload document', 'File uploaded correctly', read_docx)
    
    #Press Process
    st.subheader('Process the documents')
    streamlit_button('Format the documents', 1, on_click=None)

    #Finish
    st.subheader('Finish')
    tab1, tab2 = st.tabs(['Download processed document','Display processed document'])
    with tab1:
        #Press download
        streamlit_button('Download document', 1, on_click=None)
    with tab2:
        #Display document
        if doc_content is not None:
            st.text(doc_content)