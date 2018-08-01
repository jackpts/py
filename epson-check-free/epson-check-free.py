#!/usr/bin/python3

import requests         # pip install requests
import re
import os
import sys
import xlrd

# url = https://ee-qa2.softeq.net/rest/api/sncheck/S9VY082652/GB/en
qa_api = 'https://ee-qa2.softeq.net/rest/api/sncheck/'
# sn = 'S9VY082652'
# url_api = qa_api + sn + '/GB/en'
book = './SN_list_with_country.xlsx'

regex = 'status\":\"(.*)\",\"epson\":'


def get_request(url):
    # print('\nperforming GET request for URL: ' + url)
    r = requests.get(url)
    return r.text


def check_response(sn):
    # responses:
    # {"status":"ALREADY_USED","epson":false,"rootChannelLogoUrl":"http://ee-qa2.softeq.net/service/rest/api/up/logo"}
    # {"status":"SUCCESSFUL","epson":true,"channelName":"Epson IRS", ...
    checked_url = qa_api + sn + '/GB/en'
    response = get_request(checked_url)
    # print('resp: ' + response)
    if response:
        found = re.findall(regex, response)
        if found[0]:
            print(sn + '\t' + found[0])
        else:
            print(sn + '\t !!wrong response!!')


arguments = sys.argv[1:]
print('Please specify Epson serial numbers as a parameters')
print('\tExample: python epson-check-free.py S9VY082652 X2MX039192')
print('OR download and put the ' + book[2:] + ' file near this script!')
print('-------------------------')

if arguments.__len__() > 0:
    # print('Arguments found: ' + str(arguments))
    for a in arguments:
        if len(a) == 10:
            check_response(a)

elif os.path.exists(book):
    # print('xls File exists - start scanning...')
    wb = xlrd.open_workbook(os.path.join(book))
    wb.sheet_names()
    sh = wb.sheet_by_index(0)
    i = 1
    j = 20

    try:
        while sh.cell(i, 4).value != 0 and i < j:
            Load = sh.cell(i, 4).value
            check_response(Load)
            i += 1
    except IndexError:
        pass
else:
    print('No parameters specified and Excel-file not found!')
