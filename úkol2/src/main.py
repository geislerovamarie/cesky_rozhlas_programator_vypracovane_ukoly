import logging
from transform_xml import transform_xml
from parse_xml import parse_xml, get_encoding

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

if __name__ == "__main__":
    logger.info("Program started.")
    
    # handle arguments -> get file names atd..
    # do something - for cycle if more files (have to deal with directories)

    source, target, type = "../úkol2/obecnа_osoba.xml", "../úkol2/obecnа_osoba.tsv", "tsv"
    #source, target, type = handle_arguments() # predat argumenty
    encoding = get_encoding(source)
    column_names, values = parse_xml(source)
    transform_xml(column_names, values, target, type, encoding)
    logger.info("Program finished.")