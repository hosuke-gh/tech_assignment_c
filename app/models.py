# ============================
# models.py
# ============================
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class AnimalPicture(Base):
    __tablename__ = "animal_pictures"

    id = Column(Integer, primary_key=True, index=True)
    animal_type = Column(String, index=True)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
