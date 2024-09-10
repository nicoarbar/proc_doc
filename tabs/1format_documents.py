from datetime import datetime
from src.doc_funcs import *
from io import StringIO, BytesIO

#Logo
st.logo("static/pd32.png", icon_image="static/pd32.png")

#Title
st.title("Proc Doc")
st.header("Format Document")
    
#Params doc
st.subheader('1. Choose parameters from a template or input them')
st.info('The parameters are the variables in your document')
action_params = st.radio('', ['Input parameters manually', 'Upload csv file with parameters'],
                            label_visibility= 'collapsed')

if action_params == 'Input parameters manually':
    updf = pd.DataFrame(columns=['Parameters', 'Value'])
    updf = st.data_editor(data=updf, hide_index=True, num_rows="dynamic")
    # Download template
    disabled = True
    if len(updf) > 1:
        disabled = False

    csv_buffer = StringIO()
    updf.to_csv(csv_buffer, index=False)
    csv_string = csv_buffer.getvalue()

    st.download_button('Download template', csv_string, file_name='proc_doc_template.csv', disabled = disabled)

else:
    updf = streamlit_upload_csv('Upload csv file', 'Update the parameters if needed', header_cols_list=["Parameters","Value"])
    if updf is not None:
        updf = st.data_editor(data=updf, hide_index=True, num_rows="dynamic")

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
    date_doc = str(st.date_input('Date'))
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

doc_list = st.file_uploader('Upload document', accept_multiple_files=True)
disabled_process = True
if len(doc_list) > 0:
    disabled_process = False
    st.success('Files uploaded correctly')

#Press Process
st.subheader('4. Process the documents')
st.info('Ready to process the documents when you upload them')

#Actual Doc processing
for doc in doc_list:
    # Button disabled with doc_list upload
    press_process = st.button(f'Process {doc.name}', disabled=disabled_process)
    if press_process:
        #Add Date
        if date_doc is not None:
            date_row = {'Parameters': 'DATE', 'Value': date_doc}
            updf = pd.concat([updf, pd.DataFrame([date_row])], ignore_index=True)

        #Trim the parameters
        updf['Parameters'] = updf['Parameters'].str.strip()
        updf['Value'] = updf['Value'].str.strip()
        
        #Dataframe to dictionary
        up_dict = updf.to_dict()

        # Actual replace and doc processing
        # Read the doc from the list
        doc_content = Document(doc)

        # Processing
        output_content = proc_doc_replace(doc_content, up_dict)

        #Converting bytes to string
        target_stream = BytesIO()
        output_content.save(target_stream)
        output_content = target_stream.getvalue()
        # Reset the buffer's file-pointer to the beginning of the file
        target_stream.seek(0)
        st.info(f'Now you can download {doc.name}')

        #Downloading of the document
        st.download_button(f'Download {doc.name}', output_content, file_name=f'{doc.name}.docx')