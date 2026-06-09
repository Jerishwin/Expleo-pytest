import logging
import Utilities.logCreator as lc

def log_generator():
    logging.basicConfig(
        filename="testLogs.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()