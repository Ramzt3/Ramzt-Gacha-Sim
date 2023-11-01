from .router import characters, elements, paths
from fastapi import FastAPI
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(characters.router)
app.include_router(elements.router)
app.include_router(paths.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
