import streamlit as st
st.header('About')
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