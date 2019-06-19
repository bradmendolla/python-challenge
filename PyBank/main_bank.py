import os
import csv
import statistics as stat

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
        value = (float(monthly_profit[i + 1]) - float(monthly_profit[i])) / 2
        i += 1
        average_profit.append(value)
    avg = stat.mean(average_profit)
    print(avg)
    return monthly_profit


# open and read csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # skip header
    header = next(csvreader)
    
    for row in csvreader:
        #create list in 
        monthly_profit.append(int(row[1]))
        #create list of months 
        months.append(row[0])
        
    max_value = max(monthly_profit)
    min_value = min(monthly_profit)
    

avg_value = stat.mean(monthly_profit)   

    
    # print values as text
    
print(months)    
print("Months: " + str(len(months)))
print(f"Total profit : ${sum(monthly_profit)}")

print(avg_value)
print(max_value)
print(min_value)
avg_change(monthly_profit)

