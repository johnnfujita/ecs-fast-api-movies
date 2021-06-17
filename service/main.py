from models.movie_model import MovieModel
from fastapi import FastAPI
import fastapi
import uvicorn
import movie_data

app = FastAPI()

@app.get("/")
def index():
    return { "message": "HEllo world" }

@app.get("/api/movie/{title}", response_model=MovieModel)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND)
    return movie.dict()


if __name__ == "__main__":
    app.run()