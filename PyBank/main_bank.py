import os
import csv

budget_csv = os.path.join ("..", "Resources", "budget_data.csv")

monthly_profit = []

def average_change(monthly_profit):
    return



with open(budget_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)
    total = 0
    
    for row in csvreader:
        total += int(row[1])
        
        monthly_profit.append(row[1])

        
    
    
    print(total)
    print(monthly_profit)