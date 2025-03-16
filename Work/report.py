# report.py
#
# Exercise 2.4

import sys
import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    
    file = open(filename)
    rows = csv.reader(file)
    headers = next(rows)
    types = [str, int, float]
    select = ['name', 'shares', 'price']
    indices = [ headers.index(colname) for colname in select ]
    for row in rows:
        selected_row = [row[index] for index in indices]
        record = { name: func(val) for name, func, val in zip(select, types, selected_row) }
        portfolio.append(record)

    file.close()
    return portfolio

def read_prices(filename): 
    dict = {}
    file = open(filename, 'r')
    rows = csv.reader(file)
    for row in rows: 
        if len(row) == 0:
            continue
        dict[row[0]] = float(row[1])

    file.close()
    return dict

def print_report(report): 
    print('      Name     Shares      Price      Change')
    print('---------- ---------- ---------- -----------')
    for each_portfolio in report: {
        print(f'{each_portfolio['Name']:>10s} {each_portfolio['Shares']:>10d} {each_portfolio['Price']:>10.2f} {each_portfolio['Change']:10.2f}')
    }

def portfolio_report(portfolio_filename, price_filename):
    portfolios = read_portfolio(portfolio_filename)
    prices = read_prices(price_filename)
    
    portfolio_with_new_prices = [{**s, **{'new_price': float(prices[s['name']])}} for s in portfolios]
    portfolio_updated = [{'Name': p['name'], 'Shares': p['shares'], 'Price': p['new_price'],'Change': p['shares'] * (p['new_price'] - p['price'])} for p in portfolio_with_new_prices]
    
    print_report(portfolio_updated)
  

## Main
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio_report(filename, 'Data/prices.csv')