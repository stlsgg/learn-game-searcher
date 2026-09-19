"""
this code stores object shapes for fast api.
"""

from pydantic import BaseModel

class Question(BaseModel):
    text: str
