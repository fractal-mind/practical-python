#!/bin/python3

# tableformat.py

from icecream import ic

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
    

class StockTable(TableFormatter):
    def __init__(self, headers, rowdata) -> None:
        super().__init__()
        self.headers = headers
        self.rowdata = rowdata
    
    def headings(self):
        ic(self.headers)
        column_indices = list(range(len(self.headers)))
        print_column_count = len(column_indices)
        header_indices = tuple(self.headers)
        print(f'%10s ' * print_column_count % (header_indices))
        print(f'---------- ' * print_column_count)