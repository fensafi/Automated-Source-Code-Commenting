from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import os

app = FastAPI()

# Serve static files (like index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Microservice URL for comment generation
COMMENT_GENERATION_SERVICE_URL = "http://comment-generation-service:8002/generate_comments"

@app.get("/")
async def get_html_form():
    return FileResponse("static/index.html")

@app.post("/submit_code")
async def submit_code(code: str = Form(...)):
    # Send the code to the comment-generation microservice
    response = requests.post(COMMENT_GENERATION_SERVICE_URL, json={"code": code})
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error generating comments")
    
    # Save the commented code to a file
    commented_code = response.py
    output_filename = "commented_code.py"
    with open(output_filename, "w") as f:
        f.write(commented_code)

@app.get("/download")
async def download_file():
    file_path = "commented_code.py"
    if os.path.exists(file_path):
        return FileResponse(file_path, filename="commented_code.py", media_type="text/plain")
    raise HTTPException(status_code=404, detail="File not found")
