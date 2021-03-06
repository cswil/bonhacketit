from db.base import SessionLocal
from models.db_models import Recipe, User
from random import randint, randrange
from random import random, choice
db = SessionLocal()

for i in range(0,100):
    new_recipe = Recipe(rid=randint(1111111111,9999999999),
                        created_by="cswil",
                        title=f"test{i}",
                        calories=randint(1,300),
                        fat=randrange(1,10),
                        sugar=randrange(1,20),
                        salt=randrange(1,15),
                        vegetarian=False,
                        likes=randint(1,100),
                        dislikes=randint(1,50),
                        image_path="324234.jgp")
    db.add(new_recipe)
    db.commit()
