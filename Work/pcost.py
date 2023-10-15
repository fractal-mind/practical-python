# pcost.py
#
# Exercise 1.27

import csv
from report import read_portfolio
from icecream import ic

def print_portfolio_cost(portfolio):

    total_cost = 0
    portfolio = read_portfolio(portfolio)

    # Read dictionaries
    for stock in portfolio:
        try:
            ticker = stock['name']
            nshares = stock['shares']
            price = stock['price']

            # Calculate cost to purchase all shares in portfolio
            total_cost_ea = nshares * price
            total_cost = total_cost + total_cost_ea

            print(f'Total cost for {ticker}: ${total_cost_ea:.2f}')

        except ValueError:
            print(f"Couldn't parse: {stock}")

    print('-'*15)
    print(f'Total cost for portfolio: ${total_cost}')

def main(argv):
    
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' '<portfile>')
    
    portfile = argv[1]

    print_portfolio_cost(portfile)

        
if __name__ == '__main__':
    import sys
    main(sys.argv)