from telegram import ParseMode
from telegram.ext import CallbackQueryHandler

from bot.resources.resources_manager import ResourcesManager
from logger.logger import Logger


class FindAMenteeHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, logger: Logger):
        super().__init__(self._handle, pattern='^find_a_mentee$')
        self._resources = resources
        self._logger = logger
        self._tag = 'FindAMenteeHandler'

    def _handle(self, update, ctx):
        self._logger.debug(self._tag, f'find a mentee clicked: {update.callback_query.message.chat_id}')
        update.callback_query.edit_message_text(
            self._resources.message('find_a_mentee'),
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('find_a_mentee')
        )


class FindAMenteeBackHandler(CallbackQueryHandler):
    def __init__(self, resources: ResourcesManager, logger: Logger):
        super().__init__(self._handle, pattern='^find_a_mentee_back$')
        self._resources = resources
        self._logger = logger
        self._tag = 'FindAMenteeBackHandler'

    def _handle(self, update, ctx):
        self._logger.debug(self._tag, f'find a mentee back clicked: {update.callback_query.message.chat_id}')
        update.callback_query.edit_message_text(
            self._resources.message('start'),
            parse_mode=ParseMode.HTML,
            reply_markup=self._resources.keyboard('start')
        )
