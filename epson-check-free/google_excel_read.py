import gspread
# pip install gspread
# https://github.com/burnash/gspread

credentials = ''

gc = gspread.authorize(credentials)
# http://gspread.readthedocs.io/en/latest/oauth2.html
# pip install --upgrade oauth2client
# pip install PyOpenSSL

wks = gc.open_by_key('xxxxxxxxx').sheet1

# Or, if you feel really lazy to extract that key, paste the entire url
# wks = gc.open_by_url('https://docs.google.com/spreadsheets/d/xxxxxg/edit#gid=0')

# wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = wks.range('E2:E14')

print('cell list:' + cell_list)
