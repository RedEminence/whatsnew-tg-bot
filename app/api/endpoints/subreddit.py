from typing import List

from fastapi import APIRouter
from fastapi import Depends, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT

from db.repositories import SubredditRepository
from db.utils import get_db
from schemas.subreddit import SubredditCreate, Subreddit

router = APIRouter()


@router.get("/", response_model=List[Subreddit])
def list_subreddits(db: Session = Depends(get_db)):
    result = SubredditRepository(db).list()

    return result


@router.post("/", response_model=SubredditCreate)
def create_subreddit(subreddit: SubredditCreate, db: Session = Depends(get_db)):
    result = SubredditRepository(db).create(subreddit)

    return result


@router.delete("/{id}")
def delete_subreddit(id: int, db: Session = Depends(get_db)):
    SubredditRepository(db).delete(id)

    return Response(status_code=HTTP_204_NO_CONTENT)