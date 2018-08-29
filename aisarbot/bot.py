import os
import sys

from telegram.ext import Updater, ConversationHandler

from aisarbot import logger
from aisarbot.conversation import handler_config as ch_conf
from aisarbot.command import error as error_handler

def main():
    token = os.environ.get("AiSARB2OT_TOKEN", None)
    if token is None:
        logger.error("Environment variable 'AiSARB2OT_TOKEN' is not set.")
        sys.exit(1)

    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(ConversationHandler(**ch_conf))

    dp.add_error_handler(error_handler)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
