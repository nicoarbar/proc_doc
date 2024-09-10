import pandas as pd
from docx import Document
import streamlit as st

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} de {}".format(day, month, year)
    return messsage

def streamlit_upload_csv(label, success, header_cols_list):
    doc_content = None
    doc = st.file_uploader(label)
    if doc is not None:
        doc_content = pd.read_csv(doc, names=header_cols_list)
        st.success(success)
    return doc_content

def proc_doc_replace(doc, param):
    try:
        n_params = len(param["Parameters"])
        for i in range(0, n_params):
            doc = iterate_paragraphs(doc, param["Parameters"][i], param["Value"][i])
            doc = iterate_headers(doc, param["Parameters"][i], param["Value"][i])
    except Exception as e:
        print(f'Doc is bad formatted by: {e}')
    return doc

def iterate_paragraphs(doc, field, vals):
    for par in doc.paragraphs:
        if field in par.text:
            par.text = par.text.replace(field, vals)
    return doc

def iterate_headers(doc, field, vals):
    header = doc.sections[0].header
    for par in header.paragraphs:
        if field in par.text:
            par.text = par.text.replace(field, vals)
    return doc