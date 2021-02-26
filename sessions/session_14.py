"""
Parse excel file
"""

import os
CURRENT_PATH = os.path.abspath(__file__)
DIR_PATH = os.path.dirname(os.path.dirname(CURRENT_PATH))
FILES_DIR_PATH = os.path.join(DIR_PATH, 'files')
XLS_PATH = os.path.join(FILES_DIR_PATH, 'PythonDjangoTrainingSchedule.xls')


print('-----------')

for dirname, dir, file in os.walk(DIR_PATH):
    print(dir, file)

if os.path.exists(XLS_PATH):
    print('Good to go')

TEXT_FILE = os.path.join(FILES_DIR_PATH, 'my_text_file.txt')

# file = open(TEXT_FILE, 'w')
# file.write("This is my first file I created with Python and I am writing anything.")
# file.write("\nThis is next line 01\n")
# file.write("This is next line 02\n")
# file.write("This is next line 03\n")
# file.write("This is next line 04\n")
# file.close()

# import xlrd
#
# book = xlrd.open_workbook(XLS_PATH)
# sheet_1 = book.sheet_by_index(0)
# for rx in range(sheet_1.nrows):
#     print(sheet_1.row(rx))


# with open(TEXT_FILE, 'w') as file:
#     file.write("This is my first file I created with Python and I am writing anything.")
#     file.write("\nThis is next line 01\n")
#     file.write("This is next line 02\n")
#     file.write("This is next line 03\n")
#     file.write("This is next line 04\n")
#     file.writelines(['1','2','3','4','5'])


# with open(TEXT_FILE, 'r') as file:
#     for i in file.readlines():
#         print(i, end='')


import csv

CSV_FILE_PATH = os.path.join(FILES_DIR_PATH, 'Sheet 1-Table 1.csv')
with open(CSV_FILE_PATH, 'r') as _file:
    csv_reader = csv.reader(_file)
    for i in csv_reader:
        print(i)