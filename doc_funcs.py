from pandas import *

def doc_choose():
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

    modelo = input('Elije el numero de modelo a procesar')
    try:
        modelo_choose = opt_dict[modelo]
        print(f'Eljiste modelo {modelo_choose}')
    except KeyError:
        modelo_choose = modelo
        print(f'No existe el modelo {modelo}')
    return modelo_choose

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
