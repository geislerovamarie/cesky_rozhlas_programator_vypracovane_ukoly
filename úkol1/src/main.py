import sys
import logging
from clean_data import clean_data

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

if __name__ == "__main__":
    logger.info("Program started.")
    try:
        file = sys.argv[1]
    except:
        logger.error("No valid filename as an argument.")
        sys.exit(1)
    
    print(clean_data(file))
    logger.info("Program finished.")