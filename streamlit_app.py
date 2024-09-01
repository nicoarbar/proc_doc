import streamlit as st

#Title
st.title("Proc Doc")
st.subheader("Welcome to automatic document processing")
st.caption('Proc Doc allows you to input documents and automate the process of formatting them with parameters')

# Selection of inputs
st.info('What do you want to do?')
action = st.radio('Select your action:', 
                  ['Format docs with input parameters', 
                  'Ask GPT to verify statements', 
                  'Indexing documents for information retrieval'])

#Actions
if action == 'Ask GPT to verify statements':
    st.error('Feature under construction')

elif action == 'Indexing documents for information retrieval':
    st.error('Feature under construction')

elif action == 'Format docs with input parameters':
    st.file_uploader('File uploader')
    st.success('File processed correctly')


    st.button('Hit me')
    #st.data_editor('Edit data', data)
    st.multiselect('Multiselect', [1,2,3])
    st.text_input('Enter some text')
    st.date_input('Date input')

#Ending
tab1, tab2 = st.tabs(["Pricing", "About"])
with tab1:
    st.warning("This is an Open Source project, however you are welcome to contribute with donations as a Github Sponsor here:")
    st.write("https://github.com/nicoarbar/proc_doc")
with tab2:
    st.warning("""Proc Doc is under construction.
              For any inquiries, changes and requests please reach out here:""")
    tab2.write("https://nicoarbar.github.io/proc_doc/")  