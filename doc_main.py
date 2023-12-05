from pathlib import Path  
from pandas import *
#from docxtpl import DocxTemplate
import aspose.words as aw
from doc_funcs import *

# Welcome and doc choose
#doc_model = doc_choose()
out_doc_name = 'test'

# Path settings of doc and excel templates
current_dir = Path(__file__).parent
doc_path = current_dir / "input_docs/cierre instruccion procedimiento.docx"
excel_path = current_dir / "input_docs/Excel Modelos FAB.xlsx"

# Reading Excel template
excel_dict = excel_to_json(excel_path)

# Opening word doc
doc = aw.Document(doc_path)
doc.range.replace("Aspose.Words", "Hello",aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

# Save the document
doc.save(f"output_docs/{out_doc_name}.docx")

#
## Initialize template
#doc = DocxTemplate(str(template_path))
#
## -- Render & Save Word Document
#output_name = current_dir / f'Sales_Report_{context["month"]}.docx'
#doc.render(t)
#doc.save(output_name)
#

