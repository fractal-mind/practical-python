# fileparse.py
#
# Exercise 3.3

from typing import Optional
import csv
from icecream import ic
import gzip

def parse_csv(lines, has_headers: Optional[bool]= True, select: 
              Optional[list]= None, types: Optional[list]= None, delimiter: Optional[str]= ',', silence_errors: Optional[bool]= False) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    # Save original state of lines for non-gzipped files
    lines_state = lines

    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    # If str contains 'gz', unzip file. Otherwise str, open file and parse. If list, move to further parsing. Outputs list of strings with commas.
    if '.gz' in lines:
        with gzip.open(lines, 'rt') as file:
            lines = []
            try:
                for rowno, row in enumerate(file, 1):
                    lines.append(row.rstrip('\n'))
            except gzip.BadGzipFile as e:
                ic("ERROR:", e)
    elif isinstance(lines, str):
        with open(lines_state) as file:
            lines = []
            for rowno, row in enumerate(file, 1):
                lines.append(row.rstrip('\n'))
    else:
        pass

    # Create comma-separated list of strings
    read = csv.reader(lines, delimiter=',')

    # Read the headers (if any)
    headers = next(read) if has_headers else []

    # If specific columns have been selected, make indices for filtering
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = [] # Create list for dictionaries or tuples, depending on \
                # data having headers.

    # Iterate through rows
    for rowno, row in enumerate(read, 1):
        
        # Skip rows with no data
        if not row:
            continue
        
        # Apply type conversion to the row
        if types == None:
            pass
        elif types:
            row = [func(val) for func, val in zip(types, row)]
        
        # Make a dictionary or tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
                
    return records