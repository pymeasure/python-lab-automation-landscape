"""Take a markdown table and distribute it into a bunch of YAML files keyed by columns"""

import csv

OUTPUT_FOLDER = 'output'
HEADER_LINES = 3


def convert_to_yaml_bool(value):
    valuemap = {'': '', 'y': 'true', 'n': 'false', 'yes': 'true', 'no': 'false', 'none': 'false'}
    try:
        return valuemap[value.strip().lower()]
    except KeyError:
        try:  # split off an added comment
            return valuemap[value.split('(')[0].strip().lower()]
        except KeyError:
            pass
        return 'INVALID'


with open('converted_table.md', 'r', newline='') as infile:
    for i in range(HEADER_LINES):
        next(infile, None)
    tablereader = csv.DictReader(
        infile,
        delimiter='|',
        skipinitialspace=True,
    )

    for row in tablereader:
        if row['Name '] == '--- ':  # skip the MD table alignment row
            continue
        # print(row)
        with open(OUTPUT_FOLDER + '/' + row['Name '].lower().strip() + '.yml', 'w') as outfile:
            outfile.write('name: ' + row['Name '].strip() + '\n')
            outfile.write('description: ' + row['Description '].strip() + '\n')
            outfile.write('repo_url: ' + row['Repo URL '].removeprefix('[repo](').removesuffix(') ') + '\n')
            outfile.write('docs_url: ' + row['Docs URL '].removeprefix('[docs](').removesuffix(') ') + '\n')
            outfile.write('license: ' + row['License '].strip() + '\n')
            outfile.write('project_focus: ' + row['Application focus (if any) '].strip() + '\n')
            outfile.write('test_framework: ' + row['Test framework(nr tests) '].strip() + '\n')
            outfile.write('has_hardware_communication: ' + convert_to_yaml_bool(row['instrument/hardware communication? ']) + '\n')
            outfile.write('communication_types: ' + row['Instrument types (messagebased, register map, DLL, COM,..) '].strip() + '\n')
            outfile.write('transport_layers: ' + row['Transport layers '].strip() + '\n')
            outfile.write('has_procedures: ' + convert_to_yaml_bool(row['running predefined procedures? ']) + '\n')
            outfile.write('has_gui: ' + convert_to_yaml_bool(row['GUI/presentation layer? ']) + '\n')
            outfile.write('gui_technology: ' + row['GUI technology '].strip() + '\n')
            outfile.write('has_unit_support: ' + convert_to_yaml_bool(row['Units ']) + '\n')
            unit_lib = row['Units '].strip() if (convert_to_yaml_bool(row['Units ']) != 'false') else ''
            outfile.write('unit_library: ' + unit_lib + '\n')
            outfile.write('instrument_categories: ' + row['Abstract instrument classes '].strip() + '\n')
            remark = '"' + row['Remarks '].strip() + '"' if row['Remarks '].strip() else ''
            outfile.write('remarks: ' + remark + '\n')
            collected = '"' + row['Collected by'].strip() + '"' if row['Collected by'].strip() else ''
            outfile.write('collected_by: ' + collected + '\n')
        # break
