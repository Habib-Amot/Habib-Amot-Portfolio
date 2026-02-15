# in this lesson, I am going to learn how to extract tables from pdf file using pdfplumber library

import pdfplumber
from pathlib import Path
data_path = Path(__file__).parent / 'data/Data-Inventory-Template.pdf'

with pdfplumber.open(data_path) as pdf_obj:
    for page in pdf_obj.pages:
        text = page.extract_text()

        print(text)
        table = page.extract_table()
        if table:
            for row in table:
                print(row)

