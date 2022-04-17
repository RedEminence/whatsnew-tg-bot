from telethon.tl.custom import Message

from settings import TELEGRAM_BOT_TOKEN
from services.telegram.bot_initializer import BotInitializer


class DigestSender(BotInitializer):
    def run(self):
        with self.client.start(bot_token=TELEGRAM_BOT_TOKEN):
            self.client.loop.run_until_complete(self._send_message())

    async def _send_message(self):
        # Getting information about yourself
        me = await self.client.get_me()

        # You can send messages to yourself...
        message: Message = await self.client.send_message(self.telegram_username, 'Hello, myself!')

        # Sending a message returns the sent message object, which you can use
        print(message.raw_text)
