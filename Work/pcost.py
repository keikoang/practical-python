# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    total_cost = 0
    file = open(filename)
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        try:
            total_cost += int(row[1]) * float(row[2])
        except: 
            print('Couldn\'t parse', row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/missing.csv')
print(f'Total cost {cost:0.2f}')
