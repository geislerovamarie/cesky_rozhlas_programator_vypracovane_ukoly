import logging
import sys
import os
import argparse


logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_file', required=True, help='Path to the XML file')
    parser.add_argument('--output_file', required=False, help='Path to the output file')
    parser.add_argument('--otype', required=False, choices=['csv', 'tsv', 'json'], help='Output type: csv, tsv, json')
    args = parser.parse_args()
    return args

def source_file_check(file):
    """Kontrola, jestli zdrojový soubor existuje."""
    if os.path.exists(file):
        return file
    else:
        logger.error("Cannot access the source file %s.", file)
        sys.exit(1)

def check_valid_extension(extension):
    ext = extension.strip('.')
    if(ext not in ['csv', 'tsv', 'json']):
        logger.error("The transformation for type %s is not implemented.", ext)
        sys.exit(1)
    return ext

def check_output_file_and_no_type_defined(file_extension):
    """Kontrola - je dán výstupní soubor, ale není definován typ."""
    if(file_extension == ""):
        #output file is without extension and no type is set - lets export it to csv:
        extension = "csv"
    else: 
        # output file has an extension in its name:
        extension = check_valid_extension(file_extension)
    return extension

def check_args(args):
    """Kontrola, že jsou načtené argumenty v pořádku."""
    checked_args = {}

    # check if source file exists
    checked_args["source_file"] = source_file_check(args.source_file)

    # if there is no output file AND no type defined, lets export it to csv:
    if(args.output_file is None and args.otype is None):
        checked_args["output_file"], file_extension = os.path.splitext(args.source_file)
        checked_args["otype"] = "csv"

    #if there is output file and no type defined - continue to check_output_file_and_no_type_defined():
    elif(args.output_file is not None and args.otype is None):
        _, file_extension = os.path.splitext(args.output_file)
        checked_args["otype"] = check_output_file_and_no_type_defined(file_extension)
        checked_args["output_file"] = args.output_file

    # if there is type but no output file - create new output file from source file without extension
    elif(args.output_file is None and args.otype is not None):
        checked_args["output_file"], file_extension = os.path.splitext(args.source_file)
        checked_args["otype"] = args.otype

    # all params are set
    else:
        checked_args["output_file"] = args.output_file
        checked_args["otype"] = args.otype

    return checked_args

def handle_arguments():
    #logger.info("Parsing arguments")
    args = parse_args()
    checked_args = check_args(args)
    return checked_args["source_file"], checked_args["output_file"], checked_args["otype"]