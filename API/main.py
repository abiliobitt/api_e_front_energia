from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware

import inject
import os
import json

from services.data_service import DataService
from settings import adapter_binders


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/fetch_data_to_file')
async def read_root(background_tasks: BackgroundTasks):
    with open('DataServiceIsRunning.txt', 'r') as file:
        data = file.read().rstrip()
    if data == 'true':
        return {'isRunning': 'true' }
    else:
        data_service: DataService = inject.instance(DataService)
        background_tasks.add_task(data_service.get_data)
        return {'isRunning': 'false'}

@app.get('/generate_data')
async def read_root():
    data_service: DataService = inject.instance(DataService)
    await data_service.generateStatesData()
    return {'status': 'done'}

@app.get('/potency_by_state_and_time_range')
async def read_root():
    if (os.path.exists('potency_by_state_and_time_range.json')):
        with open('potency_by_state_and_time_range.json') as f:
            data = json.load(f)
        return data
    else:
        return {}

@app.get('/potency_by_uf_and_class')
async def read_root():
    if (os.path.exists('potency_by_uf_and_class.json')):
        with open('potency_by_uf_and_class.json') as f:
            data = json.load(f)
        return data
    else:
        return {}

def configure(binder):
    for config in adapter_binders:
        config(binder, app)


inject.configure_once(configure, bind_in_runtime=False)