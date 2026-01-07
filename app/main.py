# ============================
# main.py
# ============================
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal, engine
from app.models import Base, AnimalPicture
from app.schemas import PictureRequest, PictureResponse
from app.service import generate_url

Base.metadata.create_all(bind=engine)

# create the app
app = FastAPI(title="Animal Picture API")

# needed to serve the web interface
from fastapi.staticfiles import StaticFiles
app.mount("/ui", StaticFiles(directory="app/static", html=True), name="ui")


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
