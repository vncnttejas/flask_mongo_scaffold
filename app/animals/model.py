from typing import Optional
from pydantic import BaseModel


class Animal(BaseModel):
    name: str
    type: str
    weight: Optional[int]
    height: Optional[int]
    description: Optional[str]
