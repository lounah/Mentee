import os
from typing import List

from telegram.ext import Handler

from bot.mentee_bot import MenteeBot
from bot.config import DebugConfig, ReleaseConfig
from bot.controller import BotController, DebugBotController, ReleaseBotController
from bot.handlers.start_handler import StartHandler
from logger.logger import LoggerImpl, SystemOutTarget, FileTarget, Logger

LOGS_PATH = 'outputs/logs.txt'


class Di:
    def __init__(self, token: str, port: str = "", url: str = "", cert: str = "", key: str = ""):
        self._token = token
        self._port = port
        self._url = url
        self._cert = cert
        self._key = key
        self._init_logs()

    def bot(self) -> MenteeBot:
        logger = LoggerImpl([SystemOutTarget(), FileTarget(LOGS_PATH)])
        controller = self._create_controller(logger)
        return MenteeBot(controller, logger)

    def _create_controller(self, logger) -> BotController:
        if not self._port and not self._url and not self._cert and not self._key:
            return DebugBotController(DebugConfig(self._token), self._handlers(logger), logger)
        else:
            config = ReleaseConfig(self._token, int(self._port), self._url, self._cert, self._key)
            return ReleaseBotController(config, self._handlers(logger), logger)

    @staticmethod
    def _init_logs():
        os.makedirs(os.path.dirname(LOGS_PATH), exist_ok=True)

    @staticmethod
    def _handlers(logger: Logger) -> List[Handler]:
        return [
            StartHandler(logger)
        ]
