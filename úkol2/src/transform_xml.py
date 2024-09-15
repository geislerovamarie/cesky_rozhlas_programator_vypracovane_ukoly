import logging
import csv
import json
import sys

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

def export_to_csv_or_tsv(column_names, values, target, delimiter, encoding):
    with open(target, mode='w', newline='', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(column_names)
        writer.writerow(values)

def export_to_json(column_names, values, target, encoding):
    data = dict(zip(column_names, values))
    with open(target, mode='w', encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def transform_xml(column_names, values, target, ext, encoding):
    #logger.info("Transforming to %s.", target)

    if ext == 'csv':
        export_to_csv_or_tsv(column_names, values, target, ',', encoding)
    elif ext == 'tsv':
        export_to_csv_or_tsv(column_names, values, target, '\t', encoding)
    elif ext == 'json':
        export_to_json(column_names, values, target, encoding)
    else:
        logger.error("The transformation for type %s is not implemented.", ext)
        sys.exit(1)
