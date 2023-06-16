import inject
import json
import os

from infra.http_client.httpx.http_client import HttpClient
from settings.data.dataSettings import DataSettings

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
            


class DataService:
    @staticmethod
    async def get_data():
        http_adapter: HttpClient = inject.instance(HttpClient)
        offset = 0
        f = open("DataServiceIsRunning.txt", "a")
        f.truncate(0)
        f.write("true")
        f.close()
        while offset < 4000:
            response = await http_adapter.get(
                f"{DataSettings.URL}&limit=2&offset={0 if offset == 0 else offset}",
                headers={
                }
            )
            offset = offset + 2000
            for i in response.payload['result']['records']:
                write_json(i)
        f = open("DataServiceIsRunning.txt", "a")
        f.truncate(0)
        f.write("false")
        f.close()