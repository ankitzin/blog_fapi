import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from schemas.post_schema import PostBase
from models.post import DbPost


def create_post(db: Session, request: PostBase):
    new_post = DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_post(db: Session):
    return db.query(DbPost).all()


def delete_post(post_id, db: Session):
    post = db.query(DbPost).filter(DbPost.id == post_id).first()
    if not post:
        raise HTTPException(detail= 'Post not available to delete',
                            status_code=status.HTTP_404_NOT_FOUND)
    db.delete(post)
    db.commit()
    return 'Deleted Successfully'
