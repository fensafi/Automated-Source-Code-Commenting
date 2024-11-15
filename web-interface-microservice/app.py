# web-interface-microservice/app.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files like HTML
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_html_form():
    return FileResponse("static/index.html")
