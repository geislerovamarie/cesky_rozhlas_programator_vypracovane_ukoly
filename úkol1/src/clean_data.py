import os.path
import pandas as pd
import numpy as np
import logging


logger = logging.getLogger(__name__)
format = "%(levelname)s: %(filename)s %(funcName)s() line: %(lineno)s %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG)


all_rows_to_delete = [] # vysledek - radky k odstraneni
sequences_nonempty_name = set() # mnozina prvku "ObjectID" s alespon 1 radkem s neprazdnym "Name"
backup = {} # zaloha - cislo prvniho radku s prazdnym "Name" (dictionary s "ObjectID":"index prvniho radku")


def process_filename(file):
    #logger.info("File to be processed: " + file)
    extension = os.path.splitext(file)[1]
    separator = ',' if extension==".csv" else '\t'
    return separator

def count_nonempty_rows_in_chunk(chunk):
    """Spočítá se, kolik je neprázdných položek v "Name" sloupci pro každou sekvenci se stejným ObjectID"""
    #logger.info("Counting rows with nonempty Name in a chunk.")
    chunk["Name_nonempty"] = np.where(chunk['Name'].isnull() , 0, 1)
    group_counts = chunk.groupby("ObjectID").sum("Name_nonempty")
    return chunk, group_counts

def make_backup(chunk, group_counts):
    """Pro každou sekvenci, kde je každé jméno prázdné, se najde index prvního řádku"""
    #logger.info("Making backup for a chunk.")
    zero_groups = group_counts[group_counts["Name_nonempty"] == 0].index.tolist()
    for group in zero_groups:
        row_id = chunk[chunk["ObjectID"] == group].index[0]
        if group not in backup:
            backup[group] = row_id

def add_to_seqs_with_nonempty_name(group_counts):
    """" Pokud je pro ObjectID alespoň 1 Name, přidat do sequences_nonempty_name"""
    #logger.info("Adding sequences in the chunk with nonempty names into the set.")
    groups_with_name = group_counts[group_counts["Name_nonempty"] > 0].index.tolist()
    sequences_nonempty_name.update(groups_with_name)

def add_rows_to_delete(chunk):
    #logger.info("Adding row indexes with empty names in the chunk into list of rows to be deleted.")    
    rows_to_delete = chunk[chunk["Name_nonempty"] == 0].index.tolist()
    all_rows_to_delete.extend(rows_to_delete)

def check_if_rows_can_be_deleted():
    """Projde se backup a pokud se ObjectID nenachazi v sequences_nonempty_name (takze zadny radek nema jmeno), tak nebude odstranovan"""
    #logger.info("Check if all the rows in the final list can be deleted")
    for key,value in backup.items():
        if key not in sequences_nonempty_name:
            all_rows_to_delete.remove(value)


def clean_data(file):
    #logger.info("Cleaning data.")
    separator = process_filename(file)
    chunk_size = 1000

    for chunk in pd.read_csv(file, sep=separator,chunksize=chunk_size):
        chunk, group_counts = count_nonempty_rows_in_chunk(chunk)
        make_backup(chunk, group_counts) 
        add_to_seqs_with_nonempty_name(group_counts)
        add_rows_to_delete(chunk)

    check_if_rows_can_be_deleted()

    #logger.info("Sequences with non empty names: " + str(sequences_nonempty_name))
    #logger.info("Backup: " + str(backup))
    #logger.info("Rows to be deleted: " + str(all_rows_to_delete))

    return all_rows_to_delete