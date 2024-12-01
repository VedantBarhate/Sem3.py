import logging

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def log_messages():
    logging.debug("This is a DEBUG message (lowest level).")
    logging.info("This is an INFO message.")
    logging.warning("This is a WARNING message.")
    logging.error("This is an ERROR message.")
    logging.critical("This is a CRITICAL message (highest level).")

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    setup_logging()
    log_messages()
