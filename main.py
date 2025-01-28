from fastapi import FastAPI,Request,Form
from data.database import database

from typing import Annotated
from data.dao.dao_games import DaoJuegos

from data.database import database

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"), name = "static") 
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






@app.get("/juegos")
def get_juegos(request: Request,nombre : str = "pepe", otro: int  = 1):
    juegos =  DaoJuegos().get_all(database)
    return templates.TemplateResponse(
    request=request, name="game.html", context={"juegos": juegos,"nombre": nombre} )
   

@app.get("/formaddgames")
def form_add_juegos(request: Request):
    return templates.TemplateResponse(
    request=request, name="formaddGames.html"
    )


@app.post("/addjuegos")
def add_game(request: Request, Juego_nombre: Annotated[str, Form()] = None):
    if Juego_nombre is None:
        return templates.TemplateResponse(
            request=request, name="game.html", context={"nombre": "pepe"}
        )
    
    dao = DaoJuegos()
    dao.insert(database, Juego_nombre)
    
    juegos = dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="formaddGames.html", context={"juegos": juegos}
)


@app.post("/delgames")
def del_games(request: Request,juego_id:Annotated[str, Form()] ):
    print("hlhl")
    dao = DaoJuegos()
    dao.delete(database, juego_id)
    
    juegos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="game.html", context={"juegos": juegos} )

@app.post("/delgame/{juego_id}")
def del_game(request: Request, juego_id: Annotated[str, Form()]):
    dao = DaoJuegos()
    dao.delete(database, juego_id)
    
    juegos = dao.get_all(database)
    return templates.TemplateResponse(
        request=request, name="game.html", context={"juegos": juegos}
    )

