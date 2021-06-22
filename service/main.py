from typing import List
from .models.movie_model import MovieModel, ItemModel
from fastapi import FastAPI
import fastapi
import uvicorn
from . import movie_data

app = FastAPI()

items: List[ItemModel] = [{"title": "Johnnie", "description": "a pair of old sock"}]

@app.get("/")
async def index():
    
    return {"johnnie": "fujita"}

@app.get("/api/movie/{title}", response_model=MovieModel)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND)
    return movie.dict()

@app.get("/api/items", response_model=List[ItemModel])
async def get_items():
    list_items = items
    return list_items

@app.get("/api/items/{id:int}", response_model=ItemModel)
async def get_items(id):
    item = items[id]
    return item

@app.post("/api/items", response_model=ItemModel)
async def create_item(item: ItemModel):
    items.append(item)
    return item 

if __name__ == "__main__":
    uvicorn.run(app)

