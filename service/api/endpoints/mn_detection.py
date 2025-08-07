from fastapi import APIRouter, UploadFile, HTTPException
from fastapi import FastAPI, Request, Form, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from PIL import Image
from io import BytesIO
import numpy as np
from sympy import det
from service.core.schemas.output import APIOutput
from service.core.logic.onnx_inference import detector


mn_router = APIRouter()
templates = Jinja2Templates(directory="service/templates")


@mn_router.get("/mn_detection", response_class=HTMLResponse)
async def mn_detection_page(request: Request):
    return templates.TemplateResponse("mn_detection.html", {"request": request})


@mn_router.post("/mn_detection", response_model=APIOutput)
async def mn_detection(file: UploadFile = File(...)):
    if file.filename.split(".")[-1] not in ("jpg", "jpeg", "png", "JPG"):
        raise HTTPException(status_code=415, detail="Not an image")
    
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    image = np.array(image)
    try:
        return detector(image, is_vit=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")