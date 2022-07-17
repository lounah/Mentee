from telegram.ext import CommandHandler

from logger.logger import Logger


class StartHandler(CommandHandler):
    def __init__(self, logger: Logger):
        super().__init__(['start'], self._handle)
        self._logger = logger

    def _handle(self, update, ctx):
        self._logger.debug('StartHandler', 'cmd start')
