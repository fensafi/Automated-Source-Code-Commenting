from fastapi import FastAPI, HTTPException
from generate_comments import generate_comment

app = FastAPI()

@app.post("/generate-comments/")
async def generate_comments_endpoint(parsed_data: dict):
    try:
        comments = generate_comment(parsed_data)
        return {"comments": comments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
