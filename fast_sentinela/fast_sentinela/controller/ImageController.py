from fastapi import APIRouter, HTTPException, UploadFile, File
from pathlib import Path
import shutil
import uuid
from PIL import Image
import io
import base64

from ..enum.RoutesEnum import RoutesEnum
from ..resources.models.loader import get_image_model

router = APIRouter(prefix=RoutesEnum.IMAGE.value, tags=["image"])

UPLOAD_DIR = Path("uploads/images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_TYPES = ["image/png", "image/jpeg"]

@router.post("")
async def get_now(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Formato inválido. Envie apenas PNG ou JPEG."
        )

    file_extension = "png" if file.content_type == "image/png" else "jpg"
    unique_name = f"{uuid.uuid4()}.{file_extension}"
    file_path = UPLOAD_DIR / unique_name

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro ao salvar arquivo"
        )

    try:
        image = Image.open(file_path).convert("RGB")
        model = get_image_model()

        if not model.__class__.__module__.startswith("ultralytics"):
            raise HTTPException(
                status_code=500,
                detail="Modelo carregado não é YOLO/Ultralytics."
            )

        results = model(image)
        result = results[0]

        boxes = result.boxes
        fire = 1 if boxes is not None and len(boxes) > 0 else 0

        annotated = result.plot()
        annotated_rgb = annotated[..., ::-1]
        pil_img = Image.fromarray(annotated_rgb)

        buf = io.BytesIO()
        pil_img.save(buf, format="PNG")
        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

        return {
            "insendio": fire,
            "imagem_base64": img_base64
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar o modelo: {str(e)}"
        )
