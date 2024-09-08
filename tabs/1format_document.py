import pandas as pd
from datetime import datetime
from src.doc_funcs import *
from io import StringIO

#Logo
st.logo("static/pd32.png", icon_image="static/pd32.png")

#Title
st.title("Proc Doc")
st.header("Format Document")
    
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