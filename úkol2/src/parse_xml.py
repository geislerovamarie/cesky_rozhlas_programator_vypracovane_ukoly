import logging
import xml.etree.ElementTree as ET
from lxml import etree


logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

def get_encoding(source):
    encoding = etree.parse(source).docinfo.encoding
    #logger.info("Encoding of the file %s is %s.", source, encoding)
    return encoding

def get_om_object_vals(om_object):
    column_names = ["ObjectID", "DirectoryID", "TemplateName"]
    values = []
    for col in column_names:
        values.append(om_object.attrib.get(col))
    return column_names, values

def get_correct_val(field):   
    for child in field:
        val = child.text
        return val if val else ""   # assuming the val should be empty string

def get_om_fields_vals(om_object):
    column_names = []
    values = []

    om_header = om_object.find("OM_HEADER")
    for field in om_header.findall("OM_FIELD"):
        column_names.append(field.attrib.get('FieldID'))
        values.append(get_correct_val(field))
        
    return column_names, values

def parse_xml(source):
    #logger.info("Parsing %s.", source)

    tree = ET.parse(source)
    root = tree.getroot()
    om_object = root.find("OM_OBJECT")

    om_object_cols, om_object_vals = get_om_object_vals(om_object)
    om_fields_cols, om_fields_vals = get_om_fields_vals(om_object)

    column_names = om_object_cols + om_fields_cols
    values = om_object_vals + om_fields_vals

    #logger.info("Column names: %s.", column_names)
    #logger.info("Values: %s.", values)
    return column_names, values
