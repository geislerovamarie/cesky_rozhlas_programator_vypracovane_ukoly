import logging
import xml.etree.ElementTree as ET
import csv
import json
import argparse

logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)


def transform_xml(source, target, type):
    print(source)