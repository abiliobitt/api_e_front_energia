from decouple import config


class DataSettings:
    URL = config('URL', default='https://dadosabertos.aneel.gov.br/api/3/action/datastore_search?resource_id=b1bd71e7-d0ad-4214-9053-cbd58e9564a7&limit=2')