from fastapi import FastAPI, HTTPException
from parser import parse_code

app = FastAPI()

@app.post("/parse/")
async def parse_endpoint(source_code: str):
    try:
        parsed_data = parse_code(source_code)
        return {"parsed_data": parsed_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
