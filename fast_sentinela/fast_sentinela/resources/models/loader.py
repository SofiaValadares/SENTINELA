from functools import lru_cache
from pathlib import Path
import joblib
import torch

MODELS_DIR = Path(__file__).resolve().parent


# ============================
# 🌧️ MODELOS TABULARES (Joblib)
# ============================

@lru_cache(maxsize=1)
def get_model_with_dry_days():
    """Modelo que utiliza número de dias sem chuva."""
    return joblib.load(MODELS_DIR / "modelo_com_dias_sem_chuva.pkl")


@lru_cache(maxsize=1)
def get_model_without_dry_days():
    """Modelo sem uso de dias sem chuva."""
    return joblib.load(MODELS_DIR / "modelo_sem_dias_sem_chuva.pkl")


# ============================
# 🔥 MODELO DE IMAGEM (best_v6.pt)
# ============================

# Cache do modelo de imagem
_image_model = None


def get_image_model():
    """
    Carrega o modelo de visão computacional (best_v6) apenas uma vez.
    Suporte a PyTorch padrão e YOLO Ultralytics.
    """
    global _image_model

    if _image_model is None:
        model_path = MODELS_DIR / "best_v6.pt"

        try:
            # Tentativa de carregar como YOLO Ultralytics
            from ultralytics import YOLO
            _image_model = YOLO(str(model_path))
            return _image_model

        except Exception:
            # Caso NÃO seja YOLO, tenta PyTorch padrão
            _image_model = torch.load(model_path, map_location="cpu")
            if hasattr(_image_model, "eval"):
                _image_model.eval()

    return _image_model
