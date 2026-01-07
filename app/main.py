# ============================
# main.py
# ============================
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, AnimalPicture
from schemas import PictureRequest, PictureResponse
from service import generate_url
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Animal Picture API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/pictures", response_model=List[PictureResponse])
def fetch_pictures(req: PictureRequest, db: Session = Depends(get_db)):
    pictures = []
    try:
        for _ in range(req.count):
            pic = AnimalPicture(
                animal_type=req.animal,
                image_url=generate_url(req.animal)
            )
        db.add(pic)
        db.commit()
        db.refresh(pic)
        pictures.append(pic)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return pictures


@app.get("/pictures/{animal}/last", response_model=PictureResponse)
def last_picture(animal: str, db: Session = Depends(get_db)):
    pic = (
        db.query(AnimalPicture)
        .filter(AnimalPicture.animal_type == animal)
        .order_by(AnimalPicture.created_at.desc())
        .first()
    )
    if not pic:
        raise HTTPException(status_code=404, detail="No picture found")
    return pic
