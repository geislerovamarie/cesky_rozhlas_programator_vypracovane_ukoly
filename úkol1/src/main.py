import sys
import os
import logging
from clean_data import clean_data


logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

def file_check(file):
    """Kontrola, jestli zdrojový soubor existuje."""
    if os.path.exists(file):
        print("yo")
        return file
    else:
        logger.error("Cannot access the source file %s.", file)
        sys.exit(1)

if __name__ == "__main__":
    logger.info("Program started.")

    file = file_check(sys.argv[1])
    rows_to_delete = clean_data(file)
    print("Rows to delete")
    print("---------------")
    print("1) counting starts at 0, 0th row would already be value:")
    print(rows_to_delete)
    print("")
    print("2) counting starts at 1 and 1st row would be column names:")
    print([num+2 for num in rows_to_delete])
    
    logger.info("Program finished.")

    