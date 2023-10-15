# report.py
#
# Exercise 2.4

import csv
from pprint import pprint
import fileparse
from icecream import ic

def read_portfolio(filename) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    return fileparse.parse_csv(filename, has_headers=True, select=['name', 'shares', 'price'], types=[str,int,float])
    
def read_prices(filename) -> dict:
    '''
    Reads a given CSV file of ticker/price sets into a dictionary
    '''
    return dict(fileparse.parse_csv(filename, has_headers=False, types=[str,float]))

def make_report_data(portfolio: list, prices: dict) -> list:
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    total_value = 0.0
    total_change = 0.0

    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        total_value += total_value + current_price
        total_change += total_change + change
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    
    return rows, total_value, total_change

def print_report(reportdata: list):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change', '$')
    print(f'%10s %10s %10s %10s' % (headers[0], headers[1], headers[2], headers[3]))
    print(f'---------- '*4)
    for row in reportdata[0]:
        print('%10s %10d %10.2f %10.2f' % row)    
    print(f'----------')
    print(f'Portfolio Total Value: ${reportdata[1]:.2f}')
    print(f'Portfolio Gain/Loss Amount: ${reportdata[2]:.2f}')

def portfolio_report(portfoliofile: list, pricefile: dict):
    '''
    Take portfolio and stock prices CSVs and print out report with current prices,
    gain/loss for each stock, and total portfolio value and gain/loss.
    '''
    # Read portfolio and price files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    
    # Create report data list
    report_data = make_report_data(portfolio, prices)
    
    # Print report to terminal
    print_report(report_data)

def main(argv):
    
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' '<portfile> <pricefile>')
    
    portfile = argv[1]
    pricefile = argv[2]
    
    
    portfolio = read_portfolio(portfile)
    prices = read_prices(pricefile)
    report_data = make_report_data(portfolio, prices)
    print_report(report_data)
    
    
if __name__ == '__main__':
    import sys
    main(sys.argv)