import datetime
from sqlalchemy.orm import Session
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
