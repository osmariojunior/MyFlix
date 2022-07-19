from tkinter.tix import Tree
from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
    id: Optional[int] = None
    title: str
    year: str
    gender: str
    qtd_temp: int

    class Config:
        orm_mode = True