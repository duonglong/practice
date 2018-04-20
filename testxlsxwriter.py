import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})
for i in range(0, 1000000):
    for j in range(0, 50):
        worksheet.write(i, j, 'Hello chirp chirp chirp chirp')

workbook.close()
