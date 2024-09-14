import logging

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

def handle_arguments():
    #
    return