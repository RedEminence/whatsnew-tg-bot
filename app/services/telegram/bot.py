import time

from telethon import TelegramClient
from telethon.sessions import SQLiteSession

from config.settings import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_USERNAME
from services.reddit import API


class Bot():
    def __init__(self, api_id: int = TELEGRAM_API_ID, api_hash: str = TELEGRAM_API_HASH):
        session = SQLiteSession(session_id=f'{self.__class__.__name__}')
        self.client = TelegramClient(session, api_id, api_hash)
        self.telegram_username = TELEGRAM_USERNAME
        self.reddit_api = API()

    def _format_as_markdown(self, submission_data: dict) -> str:
        result = ''

        for subreddit_title, subreddit_posts in submission_data.items():
            subreddit_string = f'/r/{subreddit_title}\n\n'
            for index, post in enumerate(subreddit_posts):
                subreddit_string = subreddit_string + f'{index + 1}. [{post["title"]}](https://reddit.com{post["permalink"]})\n\n'

            result = result + subreddit_string

        return result
