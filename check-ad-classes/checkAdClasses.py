import re
from pathlib import Path
import sys

stylesFilePath = '/home/jacky/git/libraries-adcreative-templates/units/native-ad-templates/Build_and_Price_Mobile/style.scss'
templateFilePath = '/home/jacky/git/libraries-adcreative-templates/units/native-ad-templates/Build_and_Price_Mobile/template.html'
stylesArray = []
templateArray = []
templateData = ''

if not sys.version.startswith('3'):
    print('Sorry, you need at least python version 3 to run this script!')
    exit(0)


def isFileExist(path, filetype):
    checkingfile = Path(path)
    print('Checking if file with {0} exists [{1}]...'.format(filetype, path))
    if checkingfile.is_file():
        print('...Ok!')
    else:
        print('...Not! Check the path inside! Program exit.')
        exit(1)


isFileExist(stylesFilePath, 'styles')
isFileExist(templateFilePath, 'template')

f1 = open(stylesFilePath, 'r')
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
        if found and found not in stylesArray:
            found = found[:-1][1:].strip()                  # '.btn {' --> 'btn'
            stylesArray.append(found)

f1.close()
if not stylesArray:
    print('Suddenly not classes found in this styles file!')
    exit(1)

# print('stylesArrayUnique: ', list(set(stylesArray)))

with open(templateFilePath, 'r') as f2:
    templateData = f2.read().replace('\n', '')
f2.close()

# classData = re.split('class=[\"|\'](\w+(.+?)(\s?))*[\"|\']', templateData, flags=re.IGNORECASE)
classData = re.findall(r'class=[\"|\']([\w.(-|\s)?]+)*[\"|\'][\s+|>]', templateData)

if not classData:
    print('Suddenly not classes found in this template file!')
    exit(1)

# print('classData=', classData)
for cl in classData:
    innerArray = cl.split(' ')
    for ia in innerArray:
        templateArray.append(ia)

# print('templateArrayUnique: ', list(set(templateArray)))


def checkDiff(a, b):
    diffArray = list(set(a).union(set(b)) - set(a).intersection(set(b)))
    diffStyles = []
    diffTemplates = []
    if diffArray:
        for d in diffArray:
            if d in a:
                diffTemplates.append(d)
            else:
                diffStyles.append(d)
        print('These classes exist only in Template: \n', diffTemplates)
        print('These classes exist only in Styles: \n', diffStyles)
    else:
        print('Congratulations! No differences found!')


checkDiff(templateArray, stylesArray)



