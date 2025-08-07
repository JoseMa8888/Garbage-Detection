from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from service.api.api import main_router
import onnxruntime as rt



app = FastAPI(project_name="Garbage Detection")
app.include_router(main_router)
templates = Jinja2Templates(directory="service/templates")
app.mount("/static", StaticFiles(directory="service/static"), name="static")


class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
mn_onnx_path = "service/MN_model_onnx.onnx"
vit_quantized_path = "service/VIT_model_quantized.onnx"
mn_output_name = ["dense_2"]
vit_output_name = ["dense_10"]
providers = ["CUDAExecutionProvider"]
mn = rt.InferenceSession(mn_onnx_path, providers=providers)
vit = rt.InferenceSession(vit_quantized_path, providers=providers)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

