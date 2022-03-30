import asyncio
from typing import Optional

from fastapi import FastAPI

from reddit.api import API
from telegram.command_handler import CommandHandler
from telegram.digest_sender import DigestSender

app = FastAPI()

telegram_command_handler_loop = asyncio.get_running_loop()

task = telegram_command_handler_loop.create_task(CommandHandler().run())


@app.get("/")
def read_root():
    digest_message_sender_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(digest_message_sender_loop)
    DigestSender().run()

    data = API().collect_hot_submissions_by_subreddit()

    return {"titles": data}
