import asyncio

from fastapi import FastAPI

from api.router import router
from db.session import engine
from db.setup import Base
from services.reddit.api import API
from services.telegram.command_handler import CommandHandler
from services.telegram.digest_sender import DigestSender

app = FastAPI()

Base.metadata.create_all(bind=engine)

telegram_command_handler_loop = asyncio.get_running_loop()

task = telegram_command_handler_loop.create_task(CommandHandler().run())


@app.get("/")
def read_root():
    digest_message_sender_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(digest_message_sender_loop)
    DigestSender().run()

    data = API().collect_hot_submissions_by_subreddit()

    return {"titles": data}


app.include_router(router, prefix='/api/v1')
