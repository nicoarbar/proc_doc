import os
from datetime import datetime
from docx import Document
from doc_funcs import * 

# Welcome and doc choose
doc_model = doc_choose()
out_doc_name = 'test'

# Path settings of doc and excel templates
current_dir = os.getcwd()
doc_path = current_dir + "\\proc_doc\\input_docs\\cierre instruccion procedimiento.docx"
excel_path = current_dir + "\\proc_doc\\input_docs\\Excel Modelos FAB.xlsx"

# Reading Excel template
excel_dict = excel_to_json(excel_path)

# Functional transformations on the columns
tipo_a_anterior = str(int(float(excel_dict['NUMERO_A'][0])) - 1)
numero_a = str(int(float(excel_dict['NUMERO_A'][0])))
art_regla = str(int(float(excel_dict['ART_REGLA_ESCRUTINIO'][0])))
# Current date in Spanish legal format
now = datetime.now()
current_date = current_date_format(now)
# Correcting transormed values in the json dict
excel_dict['NUMERO_A'] = [numero_a]
excel_dict['TIPO_A_ANTERIOR'] = [tipo_a_anterior]
excel_dict['CURRENT_DATE'] = [current_date]
excel_dict['ART_REGLA_ESCRUTINIO'] = [art_regla]

# Opening word doc
doc = Document(doc_path)

# Cleaning the dictionary
clean_dict = {}
for field, vals in excel_dict.items():
    try:
        list_vals = list(vals.values())
    except AttributeError:
        list_vals = vals
    try:
        list_vals.remove('nan')
    except ValueError:
        pass
    clean_dict[field] = list_vals


for p in doc.paragraphs:
    if 'NUMERO_A' in p.text:
        p.text = p.text.replace('NUMERO_A', 'REEMPLAZO')

# Values for doc title
demandante = excel_dict['NOMBRE_DEMANDANTE'][0]
demandada = excel_dict['NOMBRE_DEMANDADA'][0]
tipo_a = excel_dict['TIPO_A'][0]

# Save the document
save_path = current_dir+f"\\proc_doc\\output_docs\\{numero_a+' - '+tipo_a+' - '+demandante+' V. '+demandada+' - '+current_date}.docx"
try:
    doc.save(save_path)
    print('Guardando el documento')
except:
    print('No se puede guardar el documento')