import asyncio
from typing import List

from fastapi import FastAPI, Depends, Response
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from starlette.responses import PlainTextResponse
from starlette.status import HTTP_204_NO_CONTENT

from database import Base, engine, SessionLocal
from db.repositories import SubredditRepository
from services.reddit.api import API
from schemas.subreddit import SubredditCreate, Subreddit
from services.telegram.command_handler import CommandHandler
from services.telegram.digest_sender import DigestSender

app = FastAPI()

Base.metadata.create_all(bind=engine)

telegram_command_handler_loop = asyncio.get_running_loop()

task = telegram_command_handler_loop.create_task(CommandHandler().run())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    digest_message_sender_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(digest_message_sender_loop)
    DigestSender().run()

    data = API().collect_hot_submissions_by_subreddit()

    return {"titles": data}


@app.get("/subreddits", response_model=List[Subreddit])
def list_subreddits(db: Session = Depends(get_db)):
    result = SubredditRepository(db).list()

    return result


@app.post("/subreddits", response_model=SubredditCreate)
def create_subreddit(subreddit: SubredditCreate, db: Session = Depends(get_db)):
    result = SubredditRepository(db).create(subreddit)

    return result


@app.delete("/subreddits/{id}")
def delete_subreddit(id: int, db: Session = Depends(get_db)):
    SubredditRepository(db).delete(id)

    return Response(status_code=HTTP_204_NO_CONTENT)