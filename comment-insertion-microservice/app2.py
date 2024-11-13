from fastapi import FastAPI, HTTPException
from insert_comments import insert_comments

app = FastAPI()

@app.post("/insert-comments/")
async def insert_comments_endpoint(source_code: str, comments: dict):
    try:
        final_code = insert_comments(source_code, comments)
        return {"final_code": final_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
