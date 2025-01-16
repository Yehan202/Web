from fastapi import FastAPI,Request
import uvicorn


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()

app.mount("/static",StaticFiles(directory="static"), name = "static" ) 
templates = Jinja2Templates(directory="templates")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/")
async def inicio(request:Request):
    return templates.TemplateResponse(
         request=request, name="index.html"
    )

@app.get("/antiguosaños")
async def antiguo(request:Request):
    return templates.TemplateResponse(
         request=request, name="antiguos_años.html"
)

@app.get("/predicciones")
async def predicciones(request:Request):
    return templates.TemplateResponse(
         request=request, name="predicciones.html"
)

@app.get("/desarrollador")
async def desarrollador(request:Request):
    return templates.TemplateResponse(
         request=request, name="desarrollador.html"
)

@app.get("/empresas")
async def empresa(request:Request):
    return templates.TemplateResponse(
         request=request, name="empresa.html"
)