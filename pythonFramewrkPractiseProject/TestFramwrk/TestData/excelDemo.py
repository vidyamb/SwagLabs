import openpyxl

openpyxl.load_workbook("C:\\Users\\vidya\\Documents\\PythonDemo1.xlsx")
sheet= book.active
cell=sheet.cell(row=1,column=2)
print(cell.value)
