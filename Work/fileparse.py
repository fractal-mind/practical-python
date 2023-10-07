# fileparse.py
#
# Exercise 3.3

import csv
from typing import Optional
from icecream import ic

def parse_csv(filename: str, has_headers: True, select: Optional[list]= None,
              types: Optional[list]= None) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read file headers
        if has_headers == False:
            pass
        else:
            headers = next(rows)
        
        # If a column selector is provided, find indices of specified columns
        # and filter selection for headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue
            
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices]
            
            # If available, map the types to values
            if types == None:
                pass
            elif types:
                row = [func(val) for func, val in zip(types, row)]
                
                # Make a dictionary
                #If there are no headers, create list of tuples instead of dict
                if has_headers == False:
                    row = (row[0], row[1])
                    ic(row)
                    ic(has_headers)
                    #record = zip(row[0], row[1])
                    records.append(row)
                else:
                    record = dict(zip(headers, row))
                    ic(row)
                    ic(has_headers)
                    records.append(record)
            else:
                print("ERROR: Too many or too few types listed")
        
        return records