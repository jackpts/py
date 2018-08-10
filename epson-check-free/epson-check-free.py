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

regex_response = 'status\":\"(.*)\",\"epson\":'
regex_min = '--scan-range:(\d+)'
regex_max = '--scan-range:\d+-(\d+)'
min_scan = 1
max_scan = 20
column_w_serials = 4
infinite = 9999
log_to_file = False
sn_array = []


def get_request(url):
    # print('\nperforming GET request for URL: ' + url)
    r = requests.get(url)
    return r.text


def check_book(min=None, max=None):
    global book, log_to_file, sn_array
    if not os.path.exists(book):
        print('Excel-file not found!')
        return
    if min is None and max is None:
        min = 1
        max = infinite      # aka Infinite

    print('Excel file exists - start scanning with Range: (' + str(min) + ' - ' + str(max) + ')')
    wb = xlrd.open_workbook(os.path.join(book))
    wb.sheet_names()
    sh = wb.sheet_by_index(0)

    try:
        while sh.cell(min, column_w_serials).value != 0 and min < max + 1:
            if max != infinite:
                load = sh.cell(min, column_w_serials).value
                check_response(load)
            min += 1
    except IndexError:
        pass

    if max == infinite:
        print('Total number of serials in Excel-file: ' + str(min))

    if log_to_file is True and len(sn_array) > 0:
        with open("epson_serials.log", "w") as log_file:
            for sn in sn_array:
                log_file.write(sn + '\n')
        print('\nLOG file epson_serials.log has been updated with ' + str(len(sn_array)) + ' records')


def check_response(sn):
    global sn_array
    # responses:
    # {"status":"ALREADY_USED","epson":false,"rootChannelLogoUrl":"http://ee-qa2.softeq.net/service/rest/api/up/logo"}
    # {"status":"SUCCESSFUL","epson":true,"channelName":"Epson IRS", ...
    checked_url = qa_api + sn + '/GB/en'
    response = get_request(checked_url)
    # print('resp: ' + response)
    if response:
        found = re.findall(regex_response, response)
        if found[0]:
            out_str = sn + '\t' + found[0]
            print(out_str)
            sn_array.append(out_str)
        else:
            print(sn + '\t !!wrong response!!')


arguments = sys.argv[1:]
print('Please specify Epson serial numbers as a parameters')
print('OR download and put the ' + book[2:] + ' file close to this script.')
print('Examples:')
print('\t python epson-check-free.py S9VY082652 X2MX039192')
print('\t python epson-check-free.py --scan-range:200-250')
print('\t python epson-check-free.py --count-records')
print('\t python epson-check-free.py --log')
# print('\t Please specify the scanning records min-max (1-1300) as a parameter:')
# print('\t (There are 1-20 records to scan by default)')
print('-'*9)


def set_number(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return None


if arguments.__len__() > 0:
    # print('Arguments found: ' + str(arguments))
    try:
        if arguments.index('--log') > -1:
            log_to_file = True
    except ValueError:
        pass

    if arguments.__len__() == 1 and log_to_file is True:
        check_book(min_scan, max_scan)
    else:
        for a in arguments:
            arg_len = len(a)
            if a == '--count-records':
                check_book()
            if a[:13] == '--scan-range:':
                min_s = re.findall(regex_min, a)
                max_s = re.findall(regex_max, a)
                check_book(set_number(min_s[0]), set_number(max_s[0]))
            if arg_len == 10:
                check_response(a)
else:
    check_book(min_scan, max_scan)

