#!/bin/python3
# stock.py

class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
        self.cost_basis = []
        self.fifo_cb = []
        self.avg_cb = []


    def cost(self):
        return self.shares * self.price

    def sell(self, shares_sold: int, price_sold: float):
        self.shares = self.shares - shares_sold
        self.income = self.shares * price_sold
        self.last_gl = (shares_sold * price_sold) - (self.shares * self.price)
