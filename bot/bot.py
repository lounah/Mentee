import threading

from controller import BotController
from logger.logger import Logger


class MenteeBot:
    def __init__(self, controller: BotController, logger: Logger):
        self._controller = controller
        self._logger = logger

    def start(self):
        try:
            self._logger.debug("Mentee", "bot started")
            threading.Thread(target=self._controller.start).start()
        except Exception as e:
            self._logger.error("Mentee", f"{str(e)}")
