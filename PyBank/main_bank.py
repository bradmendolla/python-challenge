import os
import csv
import statistics as stat
import operator

budget_csv = os.path.join ("..", "Resources", "budget_data.csv")

# global variables
monthly_profit = []
average_profit = []
months = []
profit_dict = {}
# function for finding average change in profit
# def avg_change(monthly_profit):
#     i = 0
#     for value in range(len(monthly_profit) - 1):
#         value = (float(monthly_profit[i + 1]) - float(monthly_profit[i])) / 2
#         i += 1
#         average_profit.append(value)
#     avg = stat.mean(average_profit)
#     print(f"Change in Monthly Profit: ${avg}")
#     return monthly_profit


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
    
        


with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # skip header
    header = next(csvreader)
    profit_dict = {row[0]:int(row[1]) for row in csvreader}

# take max and min values and return a key
max_val = max(profit_dict.items(), key=operator.itemgetter(1))[0]
min_val = min(profit_dict.items(), key=operator.itemgetter(1))[0]

avg_value = stat.mean(monthly_profit)   
i = 0
for value in range(len(monthly_profit) - 1):
    value = (float(monthly_profit[i + 1]) - float(monthly_profit[i])) / 2
    i += 1
    average_profit.append(value)
avg = stat.mean(average_profit)


    # print values as text

# print to terminal
print(f"{max_val} ${profit_dict[max_val]}")
print(f"{min_val} ${profit_dict[min_val]}")    
print(f"Months: {str(len(months))}")
print(f"Total profit : ${sum(monthly_profit)}")
print(f"Average Change in Monthly Profit: ${avg}")
print(f"Average Profit: ${avg_value}")


#print to text file
f = open("analysis.txt", "w")
f.write(f"Months: {str(len(months))}\n")
f.write(f"Total profit : ${sum(monthly_profit)}\n")
f.write(f"Average Change in Monthly Profit: ${avg}\n")
f.write(f"Hightest Profit Month: {max_val} ${profit_dict[max_val]}\n")
f.write(f"Lowest Profit Month: {min_val} ${profit_dict[min_val]}\n")
f.write(f"Average Monthly Profit: ${(avg_value)}\n")
f.close



