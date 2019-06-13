import os
import csv

budget_csv = os.path.join ("..", "Resources", "budget_data.csv")

monthly_profit = []
average_profit = []


def avg_change(monthly_profit):
    i = 0
    for x in range(len(monthly_profit) - 1):
        x = (int(monthly_profit[i + 1]) - int(monthly_profit[i])) / 2
        i += 1
        average_profit.append(x)
    return monthly_profit


with open(budget_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)
    total = 0
    
    for row in csvreader:
        months = len(row[0])
        total += int(row[1])
        
        monthly_profit.append(row[1])

    
    #avg_change(monthly_profit)
    
    print(months)
    print(total)
    