# fileparse.py
#
# Exercise 3.3

import csv
from typing import Optional
from icecream import ic

def parse_csv(filename: str, select: Optional[list]= None, types: Optional[list]= None) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read file headers
        headers = next(rows)
        ic(headers)
        total_headers = headers
        total_header_count = len(total_headers)

        # If a column selector is provided, find indices of specified columns
        # and filter selection for headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        
        if types:
            type_indices = [types.index(type) for type in types]
            ic(type_indices)
        else:
            type_indices = []

        records = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices]
            
            # If available, map the types to values
            if types:
                row = [func(val) for func, val in zip(types, row)]
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
            else:
                print("ERROR: Too many or too few types listed")
                    
        return records