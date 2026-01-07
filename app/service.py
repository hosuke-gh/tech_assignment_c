# ============================
# service.py
# ============================
import random
from models import AnimalPicture


def generate_url(animal: str) -> str:
    size = random.randint(200, 400)
    animal = animal.lower()
    if animal == "cat":
        return f"https://placekitten.com/{size}/{size}"
    if animal == "dog":
        return f"https://place.dog/{size}/{size}"
    if animal == "bear":
        return f"https://placebear.com/{size}/{size}"
    raise ValueError("Unsupported animal")
