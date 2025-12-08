from typing import Optional
from pydantic import BaseModel

class PredictRequestDTO(BaseModel):
    latitude: float
    longitude: float
    data_pas: Optional[str] = None
