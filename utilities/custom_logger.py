import logging
from datetime import datetime


# basic logging configuration
class LogGeneration:
    @staticmethod
    def log_generation():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            filename=f"./Logs/automation-{datetime.now().strftime('%m_%d_%Y')}.log",
            format="%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%m-%d-%Y %I:%M:%S %p"
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
