import os
import sys

from telegram.ext import Updater, ConversationHandler
from peewee import OperationalError

from aisarbot import logger
from aisarbot.conversation import handler_config as ch_conf
from aisarbot.command import error as error_handler
from aisarbot.db import db, create_tables

def main():
    logger.debug("Retrieving token ...")
    token = os.environ.get("AiSARB2OT_TOKEN", None)

    if token is None:
        logger.error("Environment variable 'AiSARB2OT_TOKEN' is not set.")
        sys.exit(1)

    logger.debug("Connecting to database ...")

    try:
        db.connect()
        create_tables()
    except OperationalError:
        pass

    logger.info("Database connection has established successfully.")

    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(ConversationHandler(**ch_conf))
    dp.add_error_handler(error_handler)

    updater.start_polling()

    logger.debug("Switching to idle mode ...")
    updater.idle()

    logger.debug("Closing database connection...")
    db.close()

    logger.info("Database connection has closed succesfully.")
    logger.info("Bye!")

if __name__ == '__main__':
    main()
