from fastapi import BackgroundTasks, FastAPI
import inject

from services.data_service import DataService
from settings import adapter_binders


app = FastAPI()

@app.get("/")
async def read_root(background_tasks: BackgroundTasks):
    with open('DataServiceIsRunning.txt', 'r') as file:
        data = file.read().rstrip()
    if data == 'true':
        return {"error": "Está rodando"}
    else:
        data_service: DataService = inject.instance(DataService)
        background_tasks.add_task(data_service.get_data)
        return {"message": "Notification sent in the background"}


def configure(binder):
    for config in adapter_binders:
        config(binder, app)


inject.configure_once(configure, bind_in_runtime=False)