import logging
import sys

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

def handle_type(type):
    if type == 'csv':
        print()
    elif type == 'tsv':
        print()
    elif type == 'json':
        print()
    else:
        logger.error("The transformation for type %s is not implemented.", type)
        sys.exit(1)

def handle_arguments():
    
    return