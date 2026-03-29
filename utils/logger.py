import logging
import os

os.makedirs("logs", exist_ok=True)

def get_logger(name, log_file="logs/test.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Remove old handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

   
    logger.propagate = False

    return logger