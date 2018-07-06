#!/usr/bin/python3

import re
import sys
import warnings
import os
from glob import glob
import logging

# https://pypi.org/project/tabulate/
# pip3 install tabulate

try:
    from tabulate import tabulate
except ImportError:
    logging.debug('tabulate module failed to import', exc_info=True)
    pass

scanDir = '/home/jacky/git/libraries-adcreative-templates/units/native-ad-templates/'
styles_assets_path = '/assets/scss/'
stylesFile = 'style.scss'
templateFile = 'template.html'
jsFile = 'index.js'
styles_regex = '(\s|\t)*\.(\w+((-)?\w+)*)(\s|\t)*{'
template_regex = r'class=[\"|\']([\w.(-|\s)?]+)*[\"|\'][\s+|>]'
js_regex = '[\'|\"]\.?(\w+((-)?\w+)*)[\'|\"]'
import_regex = '@import (.*)\/(.*)$'
scanImports = False
scanJS = False
tableOutput = True
outLOG = False
onlyTable = False
subdir_arr = []
scan_js_array = []
outputContent = []
outputHeaders = ['adName/file', 'Differences']
chunkSize = 4


def ready_steady():
    global scanImports, scanJS, outLOG, tableOutput, subdir_arr, scanDir, chunkSize, onlyTable

    if sys.version_info[0] < 3:
        warnings.warn('You need at least Python v.3 to run this script!', RuntimeWarning)
        exit(0)

    # check command line params
    arguments = sys.argv[1:]

    if '--only-table' in arguments:
        onlyTable = True

    if '--out-log' in arguments:
        outLOG = True
        logging.basicConfig(filename='scan-classes.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        check_log('log to file scan-classes.log is turning on')

    if '--scan-imports' in arguments:
        scanImports = True
        check_log('--scan-imports is turning on')

    if '--scan-js' in arguments:
        scanJS = True
        check_log('--scan-js is turning on')

    if '--chunk-size' in arguments:
        custom_chunk_index = arguments.index('--chunk-size') + 1
        custom_chunk = arguments[custom_chunk_index]
        if custom_chunk:
            check_log('Custom chunk size parameter is defined as: ' + custom_chunk)
            chunkSize = int(custom_chunk) or chunkSize

    if '--custom-path' in arguments:
        check_log('--custom-path parameter is defined')
        custom_path_index = arguments.index('--custom-path') + 1
        custom_path = arguments[custom_path_index]
        if custom_path:
            if not os.path.isdir(custom_path):
                check_log('Directory {0} is not exists! \nPlease check var scanDir in the script.'.format(custom_path))
            else:
                scanDir = custom_path

    if not os.path.isdir(scanDir):
        check_log('Directory {0} is not exists! \n Please check var scanDir in the script.'.format(scanDir))
        check_log('Or set custom path as command line parameter like this:')
        check_log('python scan-classes.py --custom-path ./units/leaderboard')
        exit(1)

    not onlyTable and print('Check if tabulate module is installed...'.format(), end=' ')
    # check_log('Check if tabulate module is installed...')
    if 'tabulate' in sys.modules:
        check_log('Ok.')
    else:
        check_log('Not! \nPlease install tabulate module for better output (as a table) via: pip3 install tabulate\n')
        tableOutput = False

    subdir_arr = glob(scanDir + './*/')
    # ['./Build_and_Price_Wired/', './SRP/', './Article_Wired/', './Map_Mobile/', './Pricing_Module/',...]

    if not subdir_arr:
        check_log('No subdirectories found in scanDir [{0}] path! Please set proper path in var.'.format(scanDir))
        exit(0)


def check_log(text):
    if not onlyTable:
        print(text)
    outLOG and logging.info(text)


def is_file_exist(path, file_type):
    global scanDir, onlyTable

    not onlyTable and print('Checking if file with {0} exists [{1}]...'.format(file_type, path), end=' ')
    outLOG and logging.info('Checking if file with ' + file_type + 'exists [' + path + ']')
    if os.path.exists(path):
        check_log('Ok.')
        return True
    else:
        not onlyTable and print('Error! \n\t Please check the path: ', scanDir + path[2:])
        check_log('Error! \n\t Please check the path' + scanDir + path[2:])
        return False


def handle_styles_file(path):
    global styles_regex, import_regex, scan_js_array

    f1 = open(path, 'r')
    styles_array = []
    styles_imports_array = []
    found = ''
    found_imports = ''

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

        # get rid of :hover/:focus.. pseudo classes
        flt = [p for p in flt if ':' not in p]

        # get rid of such classes: &:not(.small) {
        flt_x = []
        for x in flt:
            flt_x.append(re.sub('(\(|\))', '', x))
        flt = flt_x

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

        # filter collection classes like "[class^='icon-']"
        flt = filter(lambda cl: not cl.startswith('[class'), flt)

        return flt

    while True:
        line = f1.readline()
        if len(line) == 0:
            break

        try:
            found = re.search(styles_regex, line).group(0)
        except AttributeError:
            found = ''      # .class { } not found in line
        finally:
            if found:
                found = found.strip()[:-1][1:].strip()                  # '     .btn {' --> 'btn'
                if found not in styles_array:
                    styles_array.append(found)

        if scanImports:
            try:
                line_without_quotes = re.sub('(\'|\")', '', line)
                found_imports = re.search(import_regex, line_without_quotes).group(2)
                # "@import '../../../assets/scss/native.scss'" --> native(.scss)
            except AttributeError:
                found_imports = ''
            finally:
                if found_imports and found_imports not in styles_imports_array:
                    styles_imports_array.append(re.sub(';', '', found_imports))     # common-mixins; --> common-mixins

    f1.close()
    if not styles_array:
        check_log('\tSuddenly no classes found in this styles file!')

    styles_array = filter_classes(styles_array)
    styles_imports_array_path_checked = []
    if styles_imports_array:
        for si in styles_imports_array:
            if not (si.endswith('scss')):
                si += '.scss'
            full_path = os.getcwd() + styles_assets_path + si
            if os.path.exists(full_path):
                styles_imports_array_path_checked.append(full_path)
            else:
                check_log('import path doesn\'t exists: ' + full_path)

    scan_js_array = []
    if scanJS:
        path_js = path.replace(stylesFile, jsFile)
        if is_file_exist(path_js, 'js'):
            with open(path_js, 'r') as f3:
                js_data = f3.read().replace('\n', '')
            f3.close()
            found_js = re.findall(js_regex, js_data)
            if found_js:
                my_ind = [0]
                for j in found_js:
                    scan_js_array = [j[i] for i in my_ind]

                check_log('\tFound such array of classes in js-file: ' + str(scan_js_array))

    return list(set(styles_array)), styles_imports_array_path_checked


def handle_template_file(path):
    global template_regex
    template_array = []

    with open(path, 'r') as f2:
        template_data = f2.read().replace('\n', '')

    f2.close()

    class_data = re.findall(template_regex, template_data)

    if not class_data:
        check_log('Suddenly no classes found in this template file!')

    for cl in class_data:
        inner_array = cl.split(' ')
        for ia in inner_array:
            ia and template_array.append(ia)     # ia and - filter empty classes

    return list(set(template_array))


def check_imports(templs, imports):
    for i in imports:
        check_log('\tLookup for import: ' + i)
        with open(i, 'r') as im:
            im_data = im.read().replace('\n', '')
        im.close()

        for st in templs:
            current_regex = '(\s|\t)*\.' + st + '(\s|\t)*{'
            found_class = re.findall(current_regex, im_data)
            current_regex = '@mixin ' + st + '\(\)(\s|\t)*{'
            found_mixin = re.findall(current_regex, im_data)
            if found_class:
                templs.remove(st)
                check_log('\t...Found common class [' + st + '] in import, removed from the comparison.')
            if found_mixin:
                templs.remove(st)
                check_log('\t...Found common class as mixin [' + st + '] in import, removed from the comparison.')

    return templs


def check_js(templs):
    global scan_js_array

    for t in templs:
        if t in scan_js_array:
            templs.remove(t)
            check_log('\t...Found common class [' + t + '] in js-file, removed from the comparison.')

    return templs


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
        outputContent.append([ad_name, '--- no differences ---'])


def do_output():
    global tableOutput, outputContent, outputHeaders, onlyTable

    check_log('')
    tabulate_output_run = tabulate(outputContent, headers=outputHeaders, tablefmt="psql")
    if tableOutput:
        check_log(tabulate_output_run)
        if onlyTable:
            print(tabulate_output_run)

    else:
        for oc in outputContent:
            if bool(''.join(oc[:1])):
                check_log(oc[:1])
            check_log('\t\t' + oc[1:])


def init_main():
    global subdir_arr, stylesFile, templateFile, scanJS, scan_js_array

    for s in subdir_arr:
        # s = s.replace('/./', '/')
        current_dir = s.replace(scanDir, '')[:-1]
        check_log('-------[ ' + current_dir + ' ]-------')
        styles_file_path = s + stylesFile
        template_file_path = s + templateFile
        f_template_exist = is_file_exist(template_file_path, 'template')
        f_styles_exist = is_file_exist(styles_file_path, 'styles')
        ad_name = s.replace(scanDir, '')[2:]        # .../SRP/ --> SRP/
        if f_styles_exist and f_template_exist:
            styles_list, styles_imports = handle_styles_file(styles_file_path)
            template_list = handle_template_file(template_file_path)
            d_template, d_styles = check_diff(template_list, styles_list)
            if styles_imports and d_template:
                d_template = check_imports(d_template, styles_imports)
            if scanJS and scan_js_array:
                d_template = check_js(d_template)
            format_output(ad_name, d_template, 'template')
            format_output(ad_name, d_styles, 'styles')
        else:
            not f_template_exist and format_output(ad_name, ['--- nothing to compare, file not exists ---'], 'template')
            not f_styles_exist and format_output(ad_name, ['--- nothing to compare, file not exists ---'], 'styles')

    do_output()


ready_steady()
init_main()


