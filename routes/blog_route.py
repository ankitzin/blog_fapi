from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.post_schema import PostBase
from services.blog_service import create_post

router = APIRouter(
    tags=['blogs'],
    prefix='/blogs'
)


@router.get("/")
def get_all_blog():
    return {
        "data": "All Blogs"
    }


@router.post("/")
def create_post_api(request: PostBase, db: Session = Depends(get_db)):
    return create_post(db, request)
