"""
telegram-bot-gpt
@author: JavDomGom
"""

import logging

import asyncio

from typing import NoReturn

from telegram import Bot, User
from telegram.error import Forbidden, NetworkError

from src.config import TELEGRAM_API_TOKEN
from src.chat_gpt import ChatGpt


class TelegramBot:
    """ Class TelegramBot """

    def __init__(self, log: logging.Logger, chat_gpt: ChatGpt):
        """
        Class constructor.
        :param log: The logger.
        :param chat_gpt: ChatGPT object.
        """

        self.log = log
        self.chat_gpt = chat_gpt

    async def main(self) -> NoReturn:
        """ Run the bot. """

        # Here we use the `async with` syntax to properly initialize and shutdown resources.
        async with Bot(TELEGRAM_API_TOKEN) as bot:
            # Get the first pending update_id, this is so we can skip over it in case we get a "Forbidden" exception.
            try:
                update_id = (await bot.get_updates())[0].update_id
            except IndexError:
                update_id = None

            self.log.info('Listening for new messages...')
            while True:
                try:
                    update_id = await self.get_response(bot, update_id)
                except NetworkError:
                    await asyncio.sleep(1)
                except Forbidden:
                    # The user has removed or blocked the bot.
                    update_id += 1

    async def get_response(self, bot: Bot, update_id: int) -> int:
        """ Send a response to the message the user sent. """

        # Request updates after the last update_id.
        updates = await bot.get_updates(offset=update_id, timeout=10)
        for update in updates:
            next_update_id = update.update_id + 1

            # Your bot can receive updates without messages and not all messages contain text.
            if update.message and update.message.text:
                self.log.info(f'Found message "{update.message.text}".')
                self.log.debug(update.effective_user.to_dict())

                if update.message.text == '/start':
                    response = f'Welcome {update.effective_user.first_name}!'
                else:
                    response = self.chat_gpt.get_response(update.message.text)

                self.log.debug(f'response: {response}')

                # Reply to the message
                await update.message.reply_text(response)
            return next_update_id
        return update_id
