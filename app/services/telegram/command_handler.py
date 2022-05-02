from telethon.events import NewMessage

from config.settings import TELEGRAM_BOT_TOKEN
from services.telegram.bot import Bot


class CommandHandler(Bot):
    def __init__(self):
        super().__init__()
        self.client.add_event_handler(self._handle_message_recieval, NewMessage(pattern="(?i)what's new"))

    async def run(self):
        with await self.client.start(bot_token=TELEGRAM_BOT_TOKEN):
            self.client.run_until_disconnected()

    async def _handle_message_recieval(self, event: NewMessage.Event):
        submissions = self.reddit_api.collect_hot_submissions_by_subreddit()

        if submissions:
            markdown = self._format_as_markdown(submissions)
            await event.respond(markdown)
