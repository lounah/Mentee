from typing import List

from telegram.ext import Updater, Handler

from bot.config import Config
from logger.logger import Logger


class BotController:
    def __init__(self, config: Config, handlers: List[Handler], logger: Logger):
        self._config = config
        self._handlers = handlers
        self._logger = logger
        self._updater = Updater(config.token)

    def start(self):
        self._updater.start_polling()
        for handler in self._handlers:
            self._updater.dispatcher.add_handler(handler)
