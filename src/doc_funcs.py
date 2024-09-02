from pandas import *
import colorama
from colorama import Fore
import os
import time
import csv
from docx import Document
import streamlit as st

# Changing the color of the cmd shell of the executable file
colorama.init()

def model_choose(message):
    opt_dict = {
        '1': 'A1',
        '2': 'A2',
        '3': 'A3',
        '4': 'A4',
        '5': 'A5',
        '6': 'A6',
        '10': 'Todos los modelos'
    }
    for k, v in opt_dict.items():
        print(v, ': ', k)

    modelo = input(message)
    try:
        modelo_choose = opt_dict[modelo]
        print(f'Eljiste modelo {modelo_choose}')
    except KeyError:
        print(f'No existe el modelo {modelo}')
        modelo_choose = model_choose(message)
    return modelo_choose

def input_choose(message):
    input_choose = input(message)
    return input_choose

def excel_to_json(excel_path):
    xls = ExcelFile(excel_path)
    df = xls.parse(xls.sheet_names[0]).astype(str)
    excel_dict = df.to_dict()
    return excel_dict

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} de {}".format(day, month, year)
    return messsage

def iterate_paragraphs_and_headers(doc, paragraphs, field, vals):
    for par in paragraphs:
        if field in par.text:
            if len(vals) > 1:
                par.text = par.text.replace(field, '\n'.join(vals))
                #par.text = par.text.replace(field, vals.pop(0))
                #for val in vals:
                #    new_par = doc.add_paragraph()
                #    new_par.add_run(val)
            else:
                par.text = par.text.replace(field, vals[0])
    return doc

def doc_choose(current_dir, doc_name, doc_type):
    base_words = input_choose(Fore.GREEN + f'Dime el nombre del {doc_type} de base a usar. Pulsa Si para "{doc_name}"')
    if base_words in ['Si', 'S', 'si', 's', 'sI']:
        base_words = doc_name
    return current_dir + f"\\{base_words}"

def open_doc(current_dir, doc_name, doc_type, doc_func):
    # Path settings and reading Word template
    try:
        # Setting the path of the chosen doc
        doc_path = doc_choose(current_dir, doc_name, doc_type)
        # Checking if the doc exists
        if not os.path.isfile(doc_path):
            raise FileNotFoundError
        doc_object = doc_func(doc_path)
    except FileNotFoundError:
        print(f'No se encuentra el archivo Word que dices en la ruta: {doc_path}')
        doc_object = open_doc(current_dir, doc_name, doc_type, doc_func)
    except PermissionError:
        print(f'Primero cierra el documento que lo tienes abierto: {doc_path}')
        doc_object = open_doc(current_dir, doc_name, doc_type, doc_func)
    return doc_object

def raise_exception(message):
    print(message)
    time.sleep(5)
    raise Exception(message)

def num_to_str_fields(numeric_field):
    try:
        str_field = int(float(numeric_field))
    except Exception as e:
        raise_exception(f'Falla la limpieza del excel por el error: {e}')
    return str_field

def read_csv_as_rows(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

def read_docx(file):
    doc = Document(file)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return '\n'.join(content)

def streamlit_button(button_name, sleep, on_click=None, type='secondary', disabled=False):
    press_process = st.button(button_name, on_click=on_click, type=type, disabled=disabled)
    if press_process:
        with st.spinner(text='In progress'):
            time.sleep(sleep)
            st.success('Done')

def on_button_click():
    return True

def streamlit_upload(label, success, doc_func):
    doc_content =None
    doc = st.file_uploader(label)
    if doc is not None:
        doc_content = doc_func(doc)
        st.success(success)
    return doc_content