import inject
import json
import os
import pandas as pd
import random

from infra.http_client.httpx.http_client import HttpClient
from settings.data.dataSettings import DataSettings

def write_json(new_data, filename):
    if os.path.isfile(filename):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data['records'].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        with open(filename, 'w') as file:
            json.dump(new_data, file, indent=4)
            


class DataService:
    @staticmethod
    async def get_data():
        try:
            http_adapter: HttpClient = inject.instance(HttpClient)
            offset = 24407
            f = open('DataServiceIsRunning.txt', 'a')
            f.truncate(0)
            f.write('true')
            f.close()
            while offset < 60000:
                response = await http_adapter.get(
                    f'{DataSettings.URL}&limit=2000&offset={0 if offset == 0 else offset}',
                    headers={
                    }
                )
                offset = offset + 2000

                # json_file_data_frame = pd.read_json('records_data.json')
                # response_data_frame = pd.json_normalize(response.payload['result']['records'])
                # new_data_frame = pd.concat([json_file_data_frame, pd.DataFrame([response_data_frame])], ignore_index=True)
                # print(new_data_frame)


                for i in response.payload['result']['records']:
                    write_json(i, 'records_data.json')
            
            f = open('DataServiceIsRunning.txt', 'a')
            f.truncate(0)
            f.write('false')
            f.close()
        except NameError:
            print(NameError)
            f = open('DataServiceIsRunning.txt', 'a')
            f.truncate(0)
            f.write('false')
            f.close()

    @staticmethod
    async def generateStatesData():
        try:
             with open('records_data.json','r') as f:
                data = json.loads(f.read())
                df_nested_list = pd.json_normalize(data, record_path =['records'])

                #transformando datas do dataframe para conseguir gerar os gráficos
                ufs_df = df_nested_list.sort_values(['SigUF'])
                ufs_df = ufs_df.reset_index()
                random_dates = ['06/2023', '07/2023', '08/2023', '09/2023', '10/2023']
                for row in ufs_df.itertuples(index=True):
                    ufs_df.loc[row.Index, 'AnmPeriodoReferencia'] = random.choice(random_dates)
                
                # transformando strings em float
                ufs_df['MdaPotenciaInstaladaKW'] = ufs_df['MdaPotenciaInstaladaKW'].str.replace(',','.').astype('float')

                # Potência instalada por estado e classe de empreendimento
                count_potency_by_state_and_class = ufs_df.groupby(['SigUF','DscClasseConsumo', 'AnmPeriodoReferencia'], as_index=False)['MdaPotenciaInstaladaKW'].count()
                count_potency_by_state_and_class.to_csv('potency_by_uf_and_class.csv')
                count_potency_by_state_and_class.to_json('potency_by_uf_and_class.json')

                # Potência instalada por estado
                count_potency_by_state_and_time_range = ufs_df.groupby(['SigUF', 'AnmPeriodoReferencia'], as_index=False)['MdaPotenciaInstaladaKW'].count()
                count_potency_by_state_and_time_range.to_csv('potency_by_state_and_time_range.csv')
                count_potency_by_state_and_time_range.to_json('potency_by_state_and_time_range.json')

        except NameError:
            print(NameError)