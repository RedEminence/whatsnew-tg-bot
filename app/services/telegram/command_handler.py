from telethon.events import NewMessage

from services.reddit.api import API
from config.settings import TELEGRAM_BOT_TOKEN
from services.telegram.bot_initializer import BotInitializer


class CommandHandler(BotInitializer):
    def __init__(self):
        super().__init__()
        self.reddit_api = API()
        self.client.add_event_handler(self.handle_message_recieval, NewMessage(pattern="(?i)what's new"))

    async def run(self):
        with await self.client.start(bot_token=TELEGRAM_BOT_TOKEN):
            self.client.run_until_disconnected()

    async def handle_message_recieval(self, event: NewMessage.Event):
        submissions = self.reddit_api.collect_hot_submissions_by_subreddit()

        markdown = self._format_as_markdown(submissions)

        await event.respond(markdown)

    def _format_as_markdown(self, submission_data: dict) -> str:
        result = ''

        for subreddit_title, subreddit_posts in submission_data.items():
            subreddit_string = f'/r/{subreddit_title}\n\n'
            for index, post in enumerate(subreddit_posts):
                subreddit_string = subreddit_string + f'{index + 1}. [{post["title"]}](https://reddit.com{post["permalink"]})\n\n'

            result = result + subreddit_string

        return result
