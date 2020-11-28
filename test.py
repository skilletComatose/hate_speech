from docx import Document
import csv

doc = Document()

with open('data.csv', newline='') as f:
    csv_reader = csv.reader(f) 

    csv_headers = next(csv_reader)
    csv_cols = len(csv_headers)

    table = doc.add_table(rows=2, cols=csv_cols)
    hdr_cells = table.rows[0].cells

    for i in range(csv_cols):
        hdr_cells[i].text = csv_headers[i]

    for row in csv_reader:
        row_cells = table.add_row().cells
        for i in range(csv_cols):
            row_cells[i].text = row[i]

doc.add_page_break()
doc.save("data.docx")