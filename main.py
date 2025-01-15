from fastapi import FastAPI,Request
import uvicorn


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()

app.mount("/static",StaticFiles(directory="static"), name = "static" ) 
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test", response_class=HTMLResponse)
async def test(request:Request):
    
    return templates.TemplateResponse(
        request=request, name="index.html", context={"nombre":"yehan"}

    )



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)