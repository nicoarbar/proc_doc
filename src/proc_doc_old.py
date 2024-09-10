import time
import os
from datetime import datetime
from docx import Document
from doc_funcs_old import * 

# Set the current path
current_dir = os.getcwd()

# Welcome and doc choose
doc_model = model_choose(Fore.GREEN + 'Elije el numero de modelo a procesar')

# Path settings and reading Word and Excel template
print('Recuerda cerrar las plantillas de los documentos primero')
doc = open_doc(current_dir, 'cierre instruccion procedimiento.docx', 'Word', Document)
print('Abriendo la plantilla Word')
excel_dict = open_doc(current_dir, 'Excel Modelos FAB.xlsx', 'Excel', excel_to_json)
print('Abriendo la plantilla Excel')

# Functional transformations on the columns
print('Haciendo las transformaciones de datos')
numero_a = str(num_to_str_fields(excel_dict['NUMERO_A'][0]))
art_regla = str(num_to_str_fields(excel_dict['ART_REGLA_ESCRUTINIO'][0]))
tipo_a_anterior = str(num_to_str_fields(excel_dict['NUMERO_A'][0]) - 1)

# Current date in Spanish legal format
now = datetime.now()
current_date = current_date_format(now)

# Correcting transormed values in the json dict
excel_dict['NUMERO_A'] = [numero_a]
excel_dict['A_ANTERIOR'] = [tipo_a_anterior]
excel_dict['CURRENT_DATE'] = [current_date]
excel_dict['ART_REGLA_ESCRUTINIO'] = [art_regla]

# Cleaning the dictionary
try:
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
except Exception as e:
    raise_exception(f'Falla la limpieza del excel por el error: {e}')

# Replacing the words in the doc
try:
    header = doc.sections[0].header
    for field, vals in clean_dict.items():
        doc = iterate_paragraphs_and_headers(doc, doc.paragraphs, field, vals)
        doc = iterate_paragraphs_and_headers(doc, header.paragraphs, field, vals)
except Exception as e:
    raise_exception(f'El documento esta mal formateado por el error: {e}')

# Save the document
save_path = current_dir + f"\\{doc_model + ' - ' + excel_dict['TIPO_A'][0] + ' - ' + excel_dict['NOMBRE_DEMANDANTE'][0] + ' - ' + excel_dict['NOMBRE_DEMANDADA'][0] + ' - ' + current_date}.docx"

try:
    doc.save(save_path)
    print(f'Guardando el documento. Lo veras en la carpeta {current_dir}')
except Exception as e:
    raise_exception(f'No se puede guardar el documento por el error: {e}')

# Sleeping app to make user see the interface and final message
time.sleep(3)
