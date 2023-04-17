"""
telegram-bot-gpt
@authors: JavDomGom
"""

import asyncio

from src import app_logger
from src.chat_gpt import ChatGpt
from src.telegram_bot import TelegramBot

log = app_logger.get_logger(__name__)

if __name__ == '__main__':
    log.info('Starting program.')

    chat_gpt = ChatGpt(log)
    telegram_bot = TelegramBot(log, chat_gpt)

    try:
        asyncio.run(telegram_bot.main())
    except KeyboardInterrupt:
        pass

    log.info('Finish program.')
