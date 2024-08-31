import streamlit as st

sign = 'Building DataOps'
st.title("Welcome to Proc Doc")
st.header(sign)
st.image('static/nico_photo.jpg')
st.subheader(sign)
st.text(sign)
st.write(sign)
st.caption(sign)

st.button('Hit me')
data=3
#st.data_editor('Edit data', data)
st.checkbox('Check me out')
a= st.radio('Pick one:', ['nose','ear'])
st.subheader(a)
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
#st.download_button('On the dl', data)
#st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

st.image('static/favicon2.png')


# Use widgets' returned values in variables
#for i in range(int(st.number_input('Num:'))): 
#    foo()
#if st.sidebar.selectbox('I:',['f']) == 'f': b()
#my_slider_val = st.slider('Quinn Mallory', 1, 88)
#st.write(slider_val)

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
  st.radio('Select one:', [1, 2])