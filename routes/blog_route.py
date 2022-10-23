import random
import shutil
import string
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.post_schema import PostBase, PostDisplay
from services.blog_service import create_post, get_post, delete_post

router = APIRouter(
    tags=['blogs'],
    prefix='/blogs'
)


@router.get("/")
def get_all_blog(db: Session= Depends(get_db)):
    return get_post(db)


@router.post("/")
def create_post_api(request: PostBase, db: Session = Depends(get_db)):
    return create_post(db, request)


@router.delete("/{post_id}")
def delete_post_api(post_id: int, db: Session= Depends(get_db)):
    return delete_post(post_id, db)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_string = ''.join(random.choice(letter) for i in range(6))
    new = f'_{rand_string}.'
    filename = new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}
