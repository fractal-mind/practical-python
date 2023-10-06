# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # If a column selector is provided, find indices of specified columns
        # and filter selection for headers used for resulting dictionaries
        if select:
            headers = next(rows)
        records = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)
    
    return records