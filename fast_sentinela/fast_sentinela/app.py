from fastapi import FastAPI

from .enum.RoutesEnum import RoutesEnum
from .controller.PredictController import router as predict_router

app = FastAPI()

@app.get(RoutesEnum.PING.value)
def read_root():
    return {'pong'}

app.include_router(predict_router)