from telegram import ParseMode
from telegram.ext import CallbackQueryHandler

from bot.resources.resources_manager import ResourcesManager
from logger.logger import Logger


class AboutUsHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, logger: Logger):
        super().__init__(self._handle, pattern='^about$')
        self._resources = resources
        self._logger = logger
        self._tag = 'AboutUsHandler'

    def _handle(self, update, ctx):
        self._logger.debug(self._tag, f'about us clicked: {update.callback_query.message.chat_id}')
        update.callback_query.edit_message_text(
            self._resources.message('about'),
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('about')
        )


class AboutUsBackHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, logger: Logger):
        super().__init__(self._handle, pattern='^about_back$')
        self._resources = resources
        self._logger = logger
        self._tag = 'AboutUsBackHandler'

    def _handle(self, update, ctx):
        self._logger.debug(self._tag, f'about us back clicked: {update.callback_query.message.chat_id}')
        update.callback_query.edit_message_text(
            self._resources.message('start'),
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('start')
        )
