"""
telegram-bot-gpt
@author: JavDomGom
"""

import os

TRACE_LEVEL = os.getenv('TRACE_LEVEL', 'INFO')
LOG_PATH = os.getenv('LOG_PATH', 'log')
LOG_MAX_MEGABYTES = int(os.getenv('LOG_MAX_BYTES', '5'))
LOG_MAX_FILES = int(os.getenv('LOG_MAX_FILES', '3'))
LOG_FORMATTER = '{"time":"%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'

TELEGRAM_API_TOKEN = 'put-here-your-telegram-api-token'
OPENAI_API_KEY = 'put-here-your-openai-api-key'
OPENAI_ENGINE = 'text-davinci-002'
OPENAI_TEMPERATURE = 0.3
OPENAI_MAX_TOKENS = 256
OPENAI_TOP_P = 1
OPENAI_FREQUENCY_PENALTY = 0
OPENAI_PRESENCE_PENALTY = 0
OPENAI_FORMAT = 'text'
