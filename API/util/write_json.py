import json
import os

def write_json(new_data, filename='data.json'):
    if os.path.isfile(filename):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data['records'].append(new_data)
            file.seek(0)
            # file.truncate()  # limpar o conteúdo do arquivo
            json.dump(file_data, file, indent=4)
    else:
        with open(filename, 'w') as file:
            json.dump(new_data, file, indent=4)