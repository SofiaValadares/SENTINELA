from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .enum.RoutesEnum import RoutesEnum
from .controller.PredictController import router as predict_router
from .controller.ImageController import router as image_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get(RoutesEnum.PING.value)
def read_root():
    return {'pong'}

app.include_router(predict_router)
app.include_router(image_router)