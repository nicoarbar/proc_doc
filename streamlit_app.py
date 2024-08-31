import streamlit as st 
import streamlit.components.v1 as components

#st.title("Welcome to Proc Doc")

# Read the HTML file
with open("templates/index.html", 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Render the HTML file in Streamlit
st.title("Welcome to Proc Doc")
components.html(html_content, height=1600)