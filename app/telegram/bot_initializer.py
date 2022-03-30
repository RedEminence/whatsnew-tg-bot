import time

from telethon import TelegramClient
from telethon.sessions import SQLiteSession

from settings import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_USERNAME


class BotInitializer():
    def __init__(self, api_id: int = TELEGRAM_API_ID, api_hash: str = TELEGRAM_API_HASH):
        session = SQLiteSession(session_id=f'{self.__class__.__name__}')
        self.client = TelegramClient(session, api_id, api_hash)
        self.telegram_username = TELEGRAM_USERNAME
