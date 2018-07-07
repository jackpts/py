#!/usr/bin/python3

import requests         # pip install requests
import re

techno_doc_url = 'https://technodocbox.com/Unix/66519152-Learn-bash-the-hard-way.html'
converter_url = 'http://pdftoword-converter.online'
regex1 = '<a title=\"PDF to Word free online converter\" href=\"(.*)\" target='
regex2 = '<embed class=\"kv-preview-data file-preview-pdf\" src=\"(.*)\" type='
min_url_len = 46
link = ''

# going thru:
# 1. https://technodocbox.com/Unix/66519152-Learn-bash-the-hard-way.html
# 2. http://pdftoword-converter.online/enter/?url=https://technodocbox.com/66519152-Unix/Learn-bash-the-hard-way.html
# 3. storage: http://pdftoword-converter.online/storage/documents/be9ba10b52cf0dede47251fb89cf0ae1.pdf


def get_request(url):
    print('\nperforming GET request for URL: ' + url)
    # r = requests.post(url, dict(Body='This is a test'), auth=('foo', 'bar'))
    r = requests.get(url)
    print('with headers: ' + str(r.headers))
    # print('r.text', r.text)
    # print('r.json==', r.json)
    return r.text


# 1. find string:  <a title="PDF to Word free online converter" href="http://pdftoword-converter.online/enter/?url=https://technodocbox.com/66519152-Unix/Learn-bash-the-hard-way.html" target="_blank" class="btn btn-default save_as_button">
# 2. find string:  <embed class="kv-preview-data file-preview-pdf" src="/storage/documents/be9ba10b52cf0dede47251fb89cf0ae1.pdf" type="application/pdf" style=

def find_string(data, regex, name):
    print('finding link to ' + name + ' ...')
    found = re.findall(regex, data)
    if found:
        print('link found: ', found[0])
        return found[0]
    else:
        return False


response = get_request(techno_doc_url)
if response:
    link = find_string(response, regex1, 'pdftoword-converter')

    if len(link) > min_url_len:
        response = get_request(link)
        if response:
            link = find_string(response, regex2, 'converter storage')
            # ['/storage/documents/be9ba10b52cf0dede47251fb89cf0ae1.pdf']
            if len(link) > min_url_len:
                link = converter_url + link
                print('Download link to PDF: ' + link)
