from fastapi import FastAPI
from routes import blog_route
from models import post
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(blog_route.router)


post.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
