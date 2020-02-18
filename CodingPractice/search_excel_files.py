""" Python_version: 3.7.4
    1. Install the xlrd module using
        pip install xlrd """

""" SCRIPT IS NOT TESTED , MIGHT HAVE TO DEBUG """

import xlrd

files_list = [ # PUT ALL THE FILE PATHS SEPARATED BY COMMAS
                ]
# Put in the search criteria                
value_to_locate = ""
row_val = 1 # to start from the 1st data row, considering 0th row to be headers
col_val = 0 # change as per need

# Cycle through each file
for file in files_list:
    # Open the workbook
    work_book = xlrd.open_workbook(file)
    # Put a reference to sheet 
    active_sheet = work_book.sheet_by_index(0) # 0 is the index of the first sheet

    # Put the reference of the column whose value is to be used
    active_sheet.cell_value(row_val,col_val) # (Row, Column) value ,change as per reference

    for row in range(active_sheet.nrows):
        if value_to_locate == active_sheet.cell_value(row,col_val):
            # Print the whole row
            print(active_sheet.row_values(row))


          
