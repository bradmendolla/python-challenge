import os
import csv

budget_csv = os.path.join ("..", "Resources", "budget_data.csv")

# global variables
monthly_profit = []
average_profit = []
months = []
profit_dict = {}
# function for finding average change in profit
def avg_change(monthly_profit):
    i = 0
    for value in range(len(monthly_profit) - 1):
        value = (int(monthly_profit[i + 1]) - int(monthly_profit[i])) / 2
        i += 1
        average_profit.append(value)
    avg = float((sum(average_profit)) / len(average_profit))
    print(avg)
    return monthly_profit

def highest_profit(profit_dict):

    return

# open and read csv
with open(budget_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    # skip header

    header = next(csvreader)

    # define total

    total = 0
    
    for row in csvreader:
        #total profit value of positive and negative profit and append to list
        total += float(row[1])
        
        monthly_profit.append(row[1])
        
        # create list of months 

        months.append(row[0])
    

    # write directly to dictionary
    
with open(budget_csv, "r") as dictfile:
    
    # csvreader define
    
    csvreader = csv.reader(dictfile, delimiter = ",")
    header = next(csvreader)
    
    profit_dict = dict((row[0], row[1]) for row in csvreader)
        
        

    
    # print values as text
    
    
    print(f"Months: " + str(len(months)))
    print(f"Total Profit: " + str(total))
    
   
    #avg_change(monthly_profit)

