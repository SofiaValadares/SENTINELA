from functools import lru_cache
from pathlib import Path
import joblib  

MODELS_DIR = Path(__file__).resolve().parent

@lru_cache(maxsize=1)
def get_model_with_dry_days():
    return joblib.load(MODELS_DIR / "modelo_com_dias_sem_chuva.pkl")

@lru_cache(maxsize=1)
def get_model_without_dry_days():
    return joblib.load(MODELS_DIR / "modelo_sem_dias_sem_chuva.pkl")
