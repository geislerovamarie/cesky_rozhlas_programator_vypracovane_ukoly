import logging
from transform_xml import transform_xml
from parse_xml import parse_xml, get_encoding
from handle_arguments import handle_arguments

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

if __name__ == "__main__":
    logger.info("Program started.")
    
    source, target, ext = handle_arguments()
    encoding = get_encoding(source)
    column_names, values = parse_xml(source)
    transform_xml(column_names, values, target, ext, encoding)

    logger.info("Program finished.")
