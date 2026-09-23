"""
this code stores object shapes for fast api.
"""

from pydantic import BaseModel
from fastapi import Query

class Question(BaseModel):
    text: str

class FilterParams(BaseModel):
    limit: int = 10
    offset: int = 0
    genre: list[str] = Query([])
    category: list[str] = Query([])
    release_before: str = Query()
    release_after: str = Query()
    price: int | float = Query()
