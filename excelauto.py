import xlrd

Excelsheet1 = "IMMUNIZATION1.xlsx"
Excelsheet2 = "IMMUNIZATION2.xlsx"
Excelsheet3 = "IMMUNIZATION3.xlsx"

Book1 = xlrd.open_workbook(Excelsheet1)
Book2 = xlrd.open_workbook(Excelsheet2)
Book3 = xlrd.open_workbook(Excelsheet3)

first_sheet = Book1.sheet_by_index(0)
second_sheet = Book2.sheet_by_index(1)
third_sheet = Book3.sheet_by_index(2)

Headings = first_sheet.row_values(0)
InfluenzaHeading = Headings[13]

print(InfluenzaHeading)

i = 0
flu = 0
total = 0

#for loop for total number of kids
for row in range(first_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "X":
        i = i + 1
        total = total + 1
    else:
        pass

for row in range(second_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "X":
        i = i + 1
        total = total + 1
    else:
        pass

for row in range(third_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "X":
        i = i + 1
        total = total + 1
    else:
        pass

#for loop for total number of flu shots
for row in range(first_sheet.nrows):
    if str(first_sheet.cell(row, 13).value) == "X":
        i = i + 1
        flu = flu + 1
    else:
        pass

for row in range(second_sheet.nrows):
    if str(first_sheet.cell(row, 13).value) == "X":
        i = i + 1
        flu = flu + 1
    else:
        pass

for row in range(third_sheet.nrows):
    if str(first_sheet.cell(row, 13).value) == "X":
        i = i + 1
        flu = flu + 1
    else:
        pass

flushotpercent = flu/total
print(flushotpercent)