# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    '''
    Reads a given CSV file into a dictionary
    '''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for row in rows:
            record = dict(zip(headers, row))
            try:
                name = record['name']
                shares = int(record['shares'])
                price = float(record['price'])
                port_row = {'name': name, 'shares': shares, 'price': price}
                portfolio.append(port_row)
            except ValueError:
                print("Couldn't parse", row)
    return portfolio

def read_prices(filename):
    '''
    Reads a given CSV file of ticker/price sets into a dictionary
    '''

    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    prices = { }
    for row in rows:
        try:
            if row == []:
                pass
            else:
                name = row[0]
                price = float(row[1])
                prices[name] = price
        except IndexError:
            print("Couldn't parse", row)
    return(prices)

def make_report(portfolio, prices):
    '''
    Calculate total value of portfolio and
    For each row of portfolio calculate gain/loss compared to price file
    '''
    total = 0.0
    total_change = 0.0
    table_data = [ ]
    headers = ('Name', 'Shares', 'Price', 'Change', '$')
    portfolio = read_portfolio('./Data/portfolio.csv')
    prices = read_prices('./Data/prices.csv')
    for index, row in enumerate(portfolio):
        total += row['shares'] * row['price']
        if row['name'] in prices:
            total_change += row['shares'] * prices[row['name']] - row['shares'] * row['price']
            change = prices[row['name']] - row['price']
            new_tuple = (row['name'], row['shares'], prices[row['name']], change)
            table_data.append(new_tuple)
    
    print(f'%10s %10s %10s %10s' % (headers[0], headers[1], headers[2], headers[3]))
    print(f'---------- '*4)
    for name, shares, price, change in table_data:
        print(f'{name:>10s} {shares:>10d} {headers[4]:>5s} {price:<-1.2f} {change:>10.2f}')
    
    return table_data
    print(f'----------')

    print(f'Portfolio Total Value: ${total}')
    print(f'Portfolio Gain/Loss Amount: ${total_change:.2f}')

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)