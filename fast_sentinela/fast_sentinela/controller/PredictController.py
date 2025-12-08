from datetime import datetime
import pandas as pd

from fastapi import APIRouter, Depends, HTTPException

from ..dto.PredictRequestDTO import PredictRequestDTO
from ..enum.RoutesEnum import RoutesEnum
from ..resources.maps.MapsFuncs import find_state_full_name
from ..resources.models.loader import (
    get_model_with_dry_days, 
    get_model_without_dry_days
    )

router = APIRouter(prefix=RoutesEnum.PREDICT.value, tags=["predict"])

def _period_of_day(hour: int) -> str:
    if 5 <= hour < 12:
        return "manha"
    elif 12 <= hour < 17:
        return "tarde"
    elif 17 <= hour < 21:
        return "noite"
    else:
        return "madrugada"


def _build_datetime_features(timestamp: str) -> dict:
    dt = pd.to_datetime(timestamp)
    return {
        "mes": dt.month,
        "dia": dt.day,
        "dia_semana": dt.weekday(),
        "hora": dt.hour,
        "periodo_dia": _period_of_day(dt.hour)
    }

def _rain_free_day_range(days_without_rain: int) -> str:
    if days_without_rain <= 10:
        return '0-10'
    elif days_without_rain <= 20:
        return '11-20'
    elif days_without_rain <= 30:
        return '21-30'
    else:
        return '30+'
    

@router.get("")
async def get_now(params: PredictRequestDTO = Depends()):
    if params.data_pas is None:
        params.data_pas = datetime.now().isoformat(timespec="seconds")

    state = find_state_full_name(params.latitude, params.longitude)

    if state is None:
        raise HTTPException(status_code=400, detail="Coordinates outside coverage area")
    
    payload = {
        "latitude": params.latitude,
        "longitude": params.longitude,
        "estado": state,
        **_build_datetime_features(params.data_pas)
    }

    if params.days_without_rain is not None:
        payload["numero_dias_sem_chuva"] = params.days_without_rain
        payload["faixa_dias_sem_chuva"] = _rain_free_day_range(params.days_without_rain)
        model = get_model_with_dry_days()
    else:
        model = get_model_without_dry_days()

    df = pd.DataFrame([payload])
    return {"risco": int(model.predict(df)[0])}
