from config.settings import TELEGRAM_BOT_TOKEN
from services.telegram.bot import Bot


class DigestSender(Bot):
    def run(self):
        with self.client.start(bot_token=TELEGRAM_BOT_TOKEN):
            self.client.loop.run_until_complete(self._send_digest())

    async def _send_digest(self):
        submissions = self.reddit_api.collect_hot_submissions_by_subreddit()

        if submissions:
            markdown = self._format_as_markdown(submissions)
            await self.client.send_message(self.telegram_username, markdown)
