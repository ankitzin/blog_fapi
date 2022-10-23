from fastapi import APIRouter

router = APIRouter(
    tags=['blogs'],
    prefix='/blogs'
)


@router.get("/")
def get_all_blog():
    return {
        "data": "All Blogs"
    }