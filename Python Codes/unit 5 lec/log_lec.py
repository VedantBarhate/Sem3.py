import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs.log", encoding='utf-8', level=logging.INFO, format="%(levelname)s and %(message)s")

logger.debug("using debug")
logger.info("using info")
logger.warning("using info")
logger.error("using error")
logger.critical("using critical")
