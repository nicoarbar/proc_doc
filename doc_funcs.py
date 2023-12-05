from pandas import *

def convert_to_pdf(doc):
    import win32com.client as win32  # pip install pywin32
    """Convert given word document to pdf"""
    word = win32.DispatchEx("Word.Application")
    new_name = doc.replace(".docx", ".pdf")
    worddoc = word.Documents.Open(doc)
    worddoc.SaveAs(new_name, FileFormat=17)
    worddoc.Close()
    return None

def create_barchart(df, barchart_output):
    """Group DataFrame by sub-category, plot barchart, save plot as PNG"""
    top_products = df.groupby(by=df["Sub-Category"]).sum()[["Sales"]]
    top_products = top_products.sort_values(by="Sales")
    plt.rcParams["figure.dpi"] = 300
    plot = top_products.plot(kind="barh")
    fig = plot.get_figure()
    fig.savefig(barchart_output, bbox_inches="tight")
    return None

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

    print(f'Eljiste modelo {opt_dict[modelo]}')
    return opt_dict[modelo]

def excel_to_json(excel_path):
    xls = ExcelFile(excel_path)
    df = xls.parse(xls.sheet_names[0])
    excel_dict = df.to_dict()
    return excel_dict

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)
    return messsage
