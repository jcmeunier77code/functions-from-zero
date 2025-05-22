import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.bot import scrape

app = FastAPI()

class Wiki(BaseModel):
    name: str

@app.post("/wiki")
async def scrape_story(wiki: Wiki):
    result = scrape(name = wiki.name)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    # This is a simple root endpoint
    return {"message": "Hello Functions"}

@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    # This is a simple addition function
    return {"result": a + b}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)




