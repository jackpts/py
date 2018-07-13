import xmltodict
import csv

file_in = 'account.xml'
file_out = 'account.csv'
xml_main_section = 'account'
xml_target_section = 'person'
counter = 0

with open(file_in) as fi:
    doc = xmltodict.parse(fi.read())

person = doc[xml_main_section][xml_target_section]

with open(file_out, 'w') as fo:         # Just use 'w' mode in 3.x
    for p in person:
        p_dict = dict(p)                # OrderedDict to dict
        print('Target section found: ', p_dict)

        counter = counter + 1
        w = csv.DictWriter(fo, p_dict.keys())

        if counter == 1:
            w.writeheader()             # write header once if needed

        w.writerow(p_dict)
