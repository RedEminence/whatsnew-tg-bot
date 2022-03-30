from telethon.events import NewMessage

from reddit.api import API
from settings import TELEGRAM_BOT_TOKEN
from telegram.bot_initializer import BotInitializer


class CommandHandler(BotInitializer):
    def __init__(self):
        super().__init__()
        self.reddit_api = API()
        self.client.add_event_handler(self.handle_message_recieval, NewMessage(pattern="(?i)what's new"))

    async def run(self):
        with await self.client.start(bot_token=TELEGRAM_BOT_TOKEN):
            self.client.run_until_disconnected()

    async def handle_message_recieval(self, event):
        submissions = self.reddit_api.collect_hot_submissions_by_subreddit()

        markdown = self._format_in_markdown(submissions)

        await event.respond(markdown)

    def _format_in_markdown(self, submission_data: dict) -> str:

        resulting_string = ''.join(
            f'[{post["title"]}](https://reddit.com{post["permalink"]})\n\n'
            for subreddit_title, subreddit_posts in submission_data.items()
            for post in subreddit_posts
        )

        return resulting_string
