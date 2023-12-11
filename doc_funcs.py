from pandas import *
import colorama

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
    # Changing the color of the cmd shell of the executable file
    colorama.init()
    modelo = input(message)
    try:
        modelo_choose = opt_dict[modelo]
        print(f'Eljiste modelo {modelo_choose}')
    except KeyError:
        modelo_choose = modelo
        print(f'No existe el modelo {modelo}')
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
                par.text = par.text.replace(field, vals.pop(0))
                for val in vals:
                    new_par = doc.add_paragraph()
                    new_par.add_run(val)
            else:
                par.text = par.text.replace(field, vals[0])
    return doc
