from fastapi import FastAPI
import inject

from services.data_service import DataService
from settings import adapter_binders


app = FastAPI()


@app.get("/")
async def read_root():
        data_service: DataService = inject.instance(DataService)
        response = await data_service.get_data()
        return response

def configure(binder):
    for config in adapter_binders:
        config(binder, app)


inject.configure_once(configure, bind_in_runtime=False)