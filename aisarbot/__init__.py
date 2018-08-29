import logging

from aisarbot import settings

log_level = logging.INFO

if settings.DEBUG:
    log_level = logging.DEBUG

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=log_level
)

logger = logging.getLogger("aisarb20t")

logger.info("AHHHHHH !!!")
logger.info("I AM ALIVE !!!")
