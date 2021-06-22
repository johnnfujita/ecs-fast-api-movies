from pydantic import BaseModel
from typing import List

class MovieModel(BaseModel):
    title: str
    keywords: List[str] = []
    director: str
    year: int

class ItemModel(BaseModel):
    title: str
    description: str