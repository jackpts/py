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
styles_regex = '(\s|\t)*\.\w+(-?)(.+?)(\s?)\{'
template_regex = r'class=[\"|\']([\w.(-|\s)?]+)*[\"|\'][\s+|>]'
scanImports = False
scanJS = False
tableOutput = True
outLOG = False
subdir_arr = []
outputContent = []
outputHeaders = ['adName/file', 'Differences']
chunkSize = 4


def ready_steady():
    global scanImports, scanJS, outLOG, tableOutput, subdir_arr

    if sys.version_info[0] < 3:
        warnings.warn('You need at least Python v.3 to run this script!', RuntimeWarning)
        exit(0)

    if not os.path.isdir(scanDir):
        print('Directory {0} is not exists! Please check var scanDir in the script.'.format(scanDir))
        exit(1)

    # check command line params
    if '--scan-imports' in sys.argv:
        scanImports = True
    if '--scan-js' in sys.argv:
        scanJS = True
    if '--out-log' in sys.argv:
        outLOG = True

    print('Check if tabulate module installed...'.format(), end=' ')
    if 'tabulate' in sys.modules:
        print('Ok.')
    else:
        print('Not! Please install tabulate module for better output (as a table) via: pip3 install tabulate --user')
        tableOutput = False

    os.chdir(scanDir)
    subdir_arr = glob('./*/')
    # ['./Build_and_Price_Wired/', './SRP/', './Article_Wired/', './Map_Mobile/', './Pricing_Module/',...]

    if not subdir_arr:
        print('No subdirectories found in scanDir [{0}] path! Please set proper path in var.'.format(scanDir))
        exit(0)


def is_file_exist(path, file_type):
    print('Checking if file with {0} exists [{1}]...'.format(file_type, path), end=' ')
    if os.path.exists(path):
        print('Ok.')
    else:
        print('Error! Please check the path: ', path)


def handle_styles_file(path):
    global styles_regex
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
            found = re.search(styles_regex, line).group(0)

        except AttributeError:
            found = ''      # .class { } not found in line

        finally:
            if found and found not in styles_array:
                found = found.strip()[:-1][1:].strip()                  # '     .btn {' --> 'btn'
                styles_array.append(found)

    f1.close()
    if not styles_array:
        print('Suddenly not classes found in this styles file!')

    styles_array = filter_classes(styles_array)
    return list(set(styles_array))


def handle_template_file(path):
    global template_regex
    template_array = []

    with open(path, 'r') as f2:
        template_data = f2.read().replace('\n', '')

    f2.close()

    # class_data = re.split('class=[\"|\'](\w+(.+?)(\s?))*[\"|\']', template_data, flags=re.IGNORECASE)
    class_data = re.findall(template_regex, template_data)

    if not class_data:
        print('Suddenly not classes found in this template file!')

    for cl in class_data:
        inner_array = cl.split(' ')
        for ia in inner_array:
            ia and template_array.append(ia)     # ia and - filter empty classes

    return list(set(template_array))


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


def format_output(name, array, file_type):
    global chunkSize, outputContent

    ad_name = name + file_type
    line_counter = 0

    while len(array) > chunkSize:
        line_counter += 1
        if line_counter > 1:
            ad_name = ''
        outputContent.append([ad_name, ', '.join(array[:chunkSize])])
        array = array[chunkSize:]

    line_counter += 1
    if line_counter > 1:
        ad_name = ''

    if array:
        outputContent.append([ad_name, ', '.join(array)])
    else:
        outputContent.append([ad_name, '---== no differences ==---'])


def do_output():
    global tableOutput, outputContent, outputHeaders

    print()                         # just empty line
    if tableOutput:
        print(tabulate(outputContent, headers=outputHeaders, tablefmt="psql"))
    else:
        for oc in outputContent:
            if bool(''.join(oc[:1])):
                print(oc[:1])
            print('\t\t', oc[1:])


def init_main():
    global subdir_arr, stylesFile, templateFile
    
    for s in subdir_arr:
        styles_file_path = s + stylesFile
        template_file_path = s + templateFile
        is_file_exist(styles_file_path, 'styles')
        styles_list = handle_styles_file(styles_file_path)
        is_file_exist(template_file_path, 'template')
        template_list = handle_template_file(template_file_path)
        d_template, d_styles = check_diff(template_list, styles_list)

        ad_name = s[2:]  # ./SRP/ --> SRP
        format_output(ad_name, d_template, 'template')
        format_output(ad_name, d_styles, 'styles')

    do_output()


ready_steady()
init_main()


