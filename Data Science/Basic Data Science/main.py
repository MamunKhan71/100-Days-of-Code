import pandas as pd
file = pd.ExcelFile("F:/100 Days of Python - Angela/100-Days-of-Code/Data Science/Basic Data Science/sales.xlsx")
print(file.sheet_names)
sheet = file.parse('sales')
print(sheet.loc[0])