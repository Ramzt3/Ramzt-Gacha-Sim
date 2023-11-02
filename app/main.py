from .router import characters, elements, paths, light_cones
from fastapi import FastAPI
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(characters.router)
app.include_router(elements.router)
app.include_router(paths.router)
app.include_router(light_cones.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
