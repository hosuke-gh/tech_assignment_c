# ============================
# schemas.py
# ============================
from pydantic import BaseModel
from datetime import datetime

class PictureRequest(BaseModel):
    animal: str
    count: int

class PictureResponse(BaseModel):
    id: int
    animal_type: str
    image_url: str
    created_at: datetime

class Config:
    orm_mode = True
