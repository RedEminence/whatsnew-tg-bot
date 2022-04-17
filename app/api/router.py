from fastapi import APIRouter

from api.endpoints import subreddit

router = APIRouter()
router.include_router(subreddit.router, prefix='/subreddits', tags=["subreddit"])
