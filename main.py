from fastapi import FastAPI
from routes import blog_route
from models import post
from db.database import engine

app = FastAPI()
app.include_router(blog_route.router)


post.Base.metadata.create_all(engine)
