from .router import characters, elements, paths, light_cones
from fastapi import FastAPI
from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "13.228.225.19",
    "18.142.128.26",
    "54.254.162.138",
    "183.182.99.48"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(characters.router)
app.include_router(elements.router)
app.include_router(paths.router)
app.include_router(light_cones.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
