"""
telegram-bot-gpt
@author: JavDomGom
"""

import logging

import openai

from src.config import OPENAI_API_KEY, OPENAI_ENGINE, OPENAI_TEMPERATURE, OPENAI_MAX_TOKENS, OPENAI_TOP_P,\
    OPENAI_FREQUENCY_PENALTY, OPENAI_PRESENCE_PENALTY, OPENAI_FORMAT


class ChatGpt:
    """ Class ChatGpt """

    def __init__(self, log: logging.Logger):
        """
        Class constructor.
        :param log: The logger.
        """

        self.log = log
        self.engine = OPENAI_ENGINE
        self.temperature = OPENAI_TEMPERATURE
        self.max_tokens = OPENAI_MAX_TOKENS
        self.top_p = OPENAI_TOP_P
        self.frequency_penalty = OPENAI_FREQUENCY_PENALTY
        self.presence_penalty = OPENAI_PRESENCE_PENALTY
        self.format = OPENAI_FORMAT

    def get_response(self, message: str) -> str:
        """
        Send some message to AI and returns some response.
        :param message: Message to talk with the AI.
        """

        openai.api_key = OPENAI_API_KEY
        response = openai.Completion.create(
            engine=self.engine,
            prompt=message,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            format=self.format
        )

        return response['choices'][0].text
