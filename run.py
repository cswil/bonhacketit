import uvicorn
from fastapi import FastAPI
from endpoints import create_new_recipe, auth_router
from db.base import engine
from models import db_models

db_models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(
    create_new_recipe.router,
    responses={404:{"description":"not found"}}
)

app.include_router(
    auth_router.router,
    responses={404:{"description":"not found"}}
)

uvicorn.run(app)