import streamlit as st
#st.set_page_config(page_title='Proc Doc GPT', 
#                   page_icon='static/pd32.png', 
#                   layout="wide")

st.logo("static/pd32.png", icon_image="static/pd32.png")
st.title("Proc Doc")
st.header('GPT')
with st.chat_message("user"):
    st.write("Ask GPT")
    prompt = st.chat_input("Say something")
    if prompt is not None:
        st.error(f"Feature under construction. Get back to you soon with: {prompt}")
    else:
        st.error(f"Feature under construction.")