

import openpyxl

workbook = openpyxl.load_workbook("testdata/data.xlsx")
sheet = workbook.worksheets[0]

for x,y,z in sheet.iter_rows(min_row =2,values_only = True):
    print(x,y,z)