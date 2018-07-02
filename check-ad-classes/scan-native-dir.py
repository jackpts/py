#!/usr/bin/python3

import re
import sys 
import warnings
import os
from glob import glob
from prettytable import PrettyTable   # pip3 install PrettyTable --user

scanDir = '/home/jacky/git/libraries-adcreative-templates/units/native-ad-templates/'
stylesFile = 'style.scss'
templateFile = 'template.html'
jsFile = 'index.js'
scanImports = False
tableOutput = True

if sys.version_info[0] < 3:
    warnings.warn('You need at least Python v.3 to run this script!', RuntimeWarning)
    exit(0)

if not os.path.isdir(scanDir):
    print('Directory {0} is not exists! Please check var scanDir in the script.'.format(scanDir))
    exit(1)

# check command line params
if '--scan-imports' in sys.argv:
    scanImports = True

print('Check if prettytable module installed...'.format(), end=' ')
if 'prettytable' in sys.modules:
    print('Ok.')
else:
    print('Not. Please install PrettyTable module for better output (as a table) via: pip3 install PrettyTable --user')
    tableOutput = False

os.chdir(scanDir)
subdirArr = glob('./*/')
# ['./Build_and_Price_Wired/', './SRP/', './Article_Wired/', './Map_Mobile/', './Pricing_Module/',...]
if not subdirArr:
    print('No subdirectories found in this scanDir path! Please set other path in var.')
    exit(0)


def is_file_exist(path, filetype):
    print('Checking if file with {0} exists [{1}]...'.format(filetype, path), end=' ')
    if os.path.exists(path):
        print('Ok!')
    else:
        print('Not! Check the path inside! Program exit.')
        exit(1)


def handle_styles_file(path):
    f1 = open(path, 'r')
    styles_array = []
    found = ''

    while True:
        line = f1.readline()
        if len(line) == 0:      # Нулевая длина обозначает конец файла (EOF)
            break

        try:
            found = re.search('\.\w+(-?)(.+?)(\s?)\{', line).group(0)

        except AttributeError:
            found = ''      # .class { } not found in line

        finally:
            if found and found not in styles_array:
                found = found[:-1][1:].strip()                  # '.btn {' --> 'btn'
                styles_array.append(found)

    f1.close()
    if not styles_array:
        print('Suddenly not classes found in this styles file!')

    # print('styles_arrayUnique: ', list(set(styles_array)))
    # Additional filter to get rid from :hover/:focus.. pseudo classes
    result = [p for p in styles_array if ':' not in p]
    # And filter empty classes
    result = filter(None, result)
    return result


def handle_template_file(path):
    template_array = []

    with open(path, 'r') as f2:
        template_data = f2.read().replace('\n', '')

    f2.close()

    # class_data = re.split('class=[\"|\'](\w+(.+?)(\s?))*[\"|\']', template_data, flags=re.IGNORECASE)
    class_data = re.findall(r'class=[\"|\']([\w.(-|\s)?]+)*[\"|\'][\s+|>]', template_data)

    if not class_data:
        print('Suddenly not classes found in this template file!')

    for cl in class_data:
        inner_array = cl.split(' ')
        for ia in inner_array:
            ia and template_array.append(ia)     # ia and - filter empty classes

    # print('template_arrayUnique: ', list(set(template_array)))
    return template_array


def check_diff(a, b):
    diff_array = list(set(a).union(set(b)) - set(a).intersection(set(b)))
    diff_styles = []
    diff_templates = []
    if diff_array:
        for d in diff_array:
            if d in a:
                diff_templates.append(d)
            else:
                diff_styles.append(d)
        # print('These classes exist only in Template: \n', diff_templates)
        # print('These classes exist only in Styles: \n', diff_styles)
    # else:
        # print('Congratulations! No differences found!')
    diff_templ_string = ",".join(str(dt) for dt in diff_templates)
    diff_styles_string = ",".join(str(ds) for ds in diff_styles)
    return diff_templ_string, diff_styles_string


outputTable = PrettyTable(['adName', 'File', 'Differences'])

for s in subdirArr:
    stylesFilePath = s + stylesFile
    templateFilePath = s + templateFile
    is_file_exist(stylesFilePath, 'styles')
    stylesList = handle_styles_file(stylesFilePath)
    is_file_exist(templateFilePath, 'template')
    templateList = handle_template_file(templateFilePath)
    # print('Comparing subdir: ', s)
    d_template, d_styles = check_diff(templateList, stylesList)
    outputTable.add_row([s[2:-1], stylesFile, d_template])
    outputTable.add_row(['', templateFile, d_styles])

outputTable.align = "l"
print(outputTable)
