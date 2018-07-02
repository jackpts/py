#!/usr/bin/python3

import re
import sys 
import warnings
import os
from glob import glob

# https://pypi.org/project/tabulate/
# pip3 install tabulate --user
from tabulate import tabulate

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

print('Check if tabulate module installed...'.format(), end=' ')
if 'tabulate' in sys.modules:
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

    def filter_classes(s_array):
        # filter empty classes
        flt = filter(None, s_array)

        # filter separated by space & tab classes
        # ['oem-logo img'] --> ['oem-logo', 'img']
        flt_unspaced = []
        for x in flt:
            if ' ' in x or '\t' in x:
                spaced_split = x.split(' ') if (' ' in x) else x.split('\t')
                for ss in spaced_split:
                    if ss not in flt_unspaced and ss.startswith('.'):
                        flt_unspaced.append(ss[1:])
            else:
                flt_unspaced.append(x)
        flt = flt_unspaced

        # separate classes like 'disclaimer-content.hidden'
        flt_dotted = []
        for x in flt:
            if '.' in x:
                for ds in x.split('.'):
                    if ds not in flt_dotted and ds not in flt:
                        flt_dotted.append(ds)
            else:
                flt_dotted.append(x)
        flt = flt_dotted

        # get rid from :hover/:focus.. pseudo classes
        flt = [p for p in flt if ':' not in p]

        # filter collection classes like "[class^='icon-']"
        flt = filter(lambda cl: not cl.startswith('[class'), flt)

        return flt

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

    return filter_classes(styles_array)


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
    diff_template = []
    if diff_array:
        for d in diff_array:
            if d in a:
                diff_template.append(d)
            else:
                diff_styles.append(d)
        # print('These classes exist only in Template: \n', diff_templates)
        # print('These classes exist only in Styles: \n', diff_styles)
    # else:
        # print('Congratulations! No differences found!')
    # diff_templ_string = ",".join(str(dt) for dt in diff_templates)
    # diff_styles_string = ",".join(str(ds) for ds in diff_styles)
    # return diff_templ_string, diff_styles_string
    return diff_template, diff_styles


outputContent = []
outputHeaders = ['adName/file', 'Differences']
chunkSize = 5

for s in subdirArr:
    stylesFilePath = s + stylesFile
    templateFilePath = s + templateFile
    is_file_exist(stylesFilePath, 'styles')
    stylesList = handle_styles_file(stylesFilePath)
    is_file_exist(templateFilePath, 'template')
    templateList = handle_template_file(templateFilePath)
    # print('Comparing subdir: ', s)
    d_template, d_styles = check_diff(templateList, stylesList)
    adName = s[2:]    # ./SRP/ --> SRP/
    while len(d_template) > chunkSize:
        outputContent.append([adName + 'template', d_template[:4]])
        d_template = d_template[5:]
    while len(d_styles) > chunkSize:
        outputContent.append([adName + 'styles', d_styles[:4]])
        d_styles = d_styles[5:]

outputContent.sort()
print(tabulate(outputContent, headers=outputHeaders, tablefmt="psql"))
