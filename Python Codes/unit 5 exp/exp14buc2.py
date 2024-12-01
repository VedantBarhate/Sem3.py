import logging
import threading
import time

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('threaded_app.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def log_messages(thread_id):
    for _ in range(5):
        logging.debug(f"Thread-{thread_id}: This is a DEBUG message.")
        logging.info(f"Thread-{thread_id}: This is an INFO message.")
        logging.warning(f"Thread-{thread_id}: This is a WARNING message.")
        logging.error(f"Thread-{thread_id}: This is an ERROR message.")
        logging.critical(f"Thread-{thread_id}: This is a CRITICAL message.")
        time.sleep(1)  # Simulate some work

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    setup_logging()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=log_messages, args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Logging from all threads completed.")
