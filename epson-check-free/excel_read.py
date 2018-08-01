import xlrd
# pip install xlrd --user
import os.path

book = 'SN_list_with_country.xlsx'

wb = xlrd.open_workbook(os.path.join(book))
wb.sheet_names()
sh = wb.sheet_by_index(0)
i = 1

try:
    # with open("Output.txt", "a") as my_file:
    while sh.cell(i, 4) and sh.cell(i, 4).value != 0:
        Load = sh.cell(i, 4).value
        # all_d = sh.col_values(i, 4, 4)
        #DB1 = Load + " " + (" ".join(all_d))
        #my_file.write(DB1 + '\n')
        # print('i: ' + str(i))
        print(Load)
        i += 1
except IndexError:
    pass

