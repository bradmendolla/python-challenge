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

# open and read csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # skip header
    header = next(csvreader)
    
    for row in csvreader:
        #create list of monthly profits
        monthly_profit.append(int(row[1]))
        #create list of months 
        months.append(row[0])
    
total_profit = sum(monthly_profit)  
avg_value = stat.mean(monthly_profit)
# zip lists into dictionary
profit_dict = dict(zip(months, monthly_profit))
# take max and min values and return a key
max_val = max(profit_dict.items(), key=operator.itemgetter(1))[0]
min_val = min(profit_dict.items(), key=operator.itemgetter(1))[0]


i = 0
for value in range(len(monthly_profit) - 1):
    value = (float(monthly_profit[i + 1]) - float(monthly_profit[i])) / 2
    i += 1
    average_profit.append(value)

avg = stat.mean(average_profit)


# print to terminal 
print(f"Months: {len(months)}")
print(f"{max_val} ${profit_dict[max_val]}")
print(f"{min_val} ${profit_dict[min_val]}")    
print(f"Total profit : ${total_profit}")
print(f"Average Change in Monthly Profit: ${avg}")
print(f"Average Profit: ${avg_value}")


#print to text file
f = open("analysis.txt", "w")
f.write(f"Months: {len(months)}\n")
f.write(f"Total profit : ${total_profit}\n")
f.write(f"Average Change in Monthly Profit: ${avg}\n")
f.write(f"Hightest Profit Month: {max_val} ${profit_dict[max_val]}\n")
f.write(f"Lowest Profit Month: {min_val} ${profit_dict[min_val]}\n")
f.write(f"Average Monthly Profit: ${(avg_value)}\n")
f.close



