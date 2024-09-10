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
st.info('Update the parameters (autosave)')
action_params = st.radio('', ['Input parameters manually', 'Upload csv file with parameters'],
                            label_visibility= 'collapsed')

if action_params == 'Input parameters manually':
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
    df = streamlit_upload_csv('Upload csv file', 'Update the parameters', header_cols_list=["Parameters","Value"])
    if df is not None:
        updf = st.data_editor(data=df, hide_index=True, num_rows="dynamic")

#Date
st.subheader('2. Choose a date')
st.info('This is the date to be displayed in your document')
date_doc = current_date_format(datetime.now())
action_date = st.radio('', 
                        [f'Choose current date in spanish: **{date_doc}**', 
                        'Input date from calendar', 
                        'Input your own date format',
                        'No date'], 
                        label_visibility= 'collapsed')
if action_date == 'Input date from calendar':
    date_doc = st.date_input('Date')
elif action_date == 'Input your own date format':
    date_doc = st.text_input('Input your own date format')
elif action_date == 'No date':
    date_doc = None
else:
    date_doc = current_date_format(datetime.now())

if date_doc is None:
    disable_date = True
else:
    disable_date = False

press_date = st.button('Commit date', disabled=disable_date)
if press_date:
    #Add date column
    date_row = {'Parameters': 'DATE', 'Value': date_doc}
    updf = pd.concat([updf, pd.DataFrame([date_row])], ignore_index=True)
if updf is not None:
    st.dataframe(updf, hide_index = True)

#Template doc
st.subheader('3. Upload your document to format')
st.info('This will be your working document')
doc_content = streamlit_upload_docx('Upload document', 'File uploaded correctly')

#Press Process
st.subheader('4. Process the documents')
st.info('Documents are ready to be processed')
disabled_process = True
if doc_content is not None:
    disabled_process = False
press_process = st.button('Process the documents', disabled=disabled_process)

#Actual Doc processing
if date_doc is not None:
    date_row = {'Parameters': 'DATE', 'Value': date_doc}
    updf = pd.concat([updf, pd.DataFrame([date_row])], ignore_index=True)
if press_process:
    updf['Parameters'] = updf['Parameters'].str.strip()
    updf['Value'] = updf['Value'].str.strip()
    up_dict = updf.to_dict()
    output_content = proc_doc_replace(doc_content, up_dict)
    #target_stream = StringIO()
    #output_content.save(target_stream)
    output_content.save('new-file-name.docx')
else:
    output_content = 'Click to process the documents'

#Finish
st.subheader('5. Finish')
st.info('You can download the document or display it')

# Download document
disabled_down = True
proc_doc_filename = st.text_input('Enter name of the file to be downloaded')
if len(proc_doc_filename) > 1:
    disabled_down = False
st.download_button('Download document', output_content, file_name=proc_doc_filename, disabled = disabled_down)

# Display document
press_display = st.button('Display document', disabled=disabled_process)
if press_display:
    st.success(output_content)