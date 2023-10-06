# pcost.py
#
# Exercise 1.27

import os
import csv

def portfolio_cost(filename):

    #open file
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0

    #read lines
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            ticker = row[0]
            nshares = int(record['shares'])
            price = float(record['price'])

            #calculate cost to purchase all shares in portfolio
            total_cost_ea = nshares * price
            total_cost = total_cost + total_cost_ea

            print(f'Total cost for {ticker}: ${total_cost_ea:.2f}')

        except ValueError:
            print(f"Row {rowno}: Couldn't parse: {row}")
        

    print('-'*15)
    print(f'Total cost for portfolio: ${total_cost}')
    f.close()