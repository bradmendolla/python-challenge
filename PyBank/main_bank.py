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
    profit_dict = dict((int(rows[1]),rows[0]) for rows in csvreader)

max_value = max(profit_dict)
min_value = min(profit_dict)



avg_value = stat.mean(monthly_profit)   
i = 0
for value in range(len(monthly_profit) - 1):
    value = (float(monthly_profit[i + 1]) - float(monthly_profit[i])) / 2
    i += 1
    average_profit.append(value)
avg = stat.mean(average_profit)


    # print values as text
    
print(f"Months: {str(len(months))}")
print(f"Total profit : ${sum(monthly_profit)}")
print(f"Average Change in Monthly Profit: ${avg}")
print(f"Average Profit: ${avg_value}")
print(f"Highest Profit Month: {profit_dict[max_value]} ${max_value}")
print(f"Lowest Profit Month: {profit_dict[min_value]} ${min_value}")


f = open("output.txt", "w")
f.write(f"Months: {str(len(months))}\n")
f.write(f"Total profit : ${sum(monthly_profit)}\n")
f.write(f"Average Change in Monthly Profit: ${avg}\n")
f.write(f"Average Monthly Profit: ${str(avg_value)}\n")
f.write(f"Highest Profit Month: {profit_dict[max_value]} ${max_value}\n")
f.write(f"Lowest Profit Month: {profit_dict[min_value]} ${min_value}\n")


f.close



