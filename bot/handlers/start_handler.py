from telegram import ParseMode
from telegram.ext import CommandHandler

from bot.resources.resources_manager import ResourcesManager
from logger.logger import Logger


class StartHandler(CommandHandler):
    def __init__(self, resources: ResourcesManager, logger: Logger):
        super().__init__(['start'], self._handle)
        self._resources = resources
        self._logger = logger
        self._tag = 'StartHandler'

    def _handle(self, update, ctx):
        self._logger.debug(self._tag, f'user start: {update.message.chat_id}')
        update.message.reply_text(
            self._resources.message('start'),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('start')
        )
