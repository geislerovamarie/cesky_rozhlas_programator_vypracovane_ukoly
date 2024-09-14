import logging
from transform_xml import transform_xml

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

if __name__ == "__main__":
    logger.info("Program started.")
    
    # handle arguments -> get file names atd..
    # do something - for cycle if more files (have to deal with directories)

    source, target, type = "úkol2/obecnа_osoba.xml", "úkol2/obecnа_osoba.csv", "csv"
    #source, target, type = handle_arguments() # predat argumenty
    transform_xml(source, target, type)
    logger.info("Program finished.")