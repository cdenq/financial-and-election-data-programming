#Storage variables
total_months = 0
net_profit = 0
average_step_profit = 0
max_step_profit = 0
max_step_profit_month = ""
min_step_profit = 0
min_step_profit_month = ""

#Temporary storage variables
previous_profit = 0
current_profit = 0
step_profit = 0
step_profit_list = []

#Import modules
import os
import csv

#Get data from file
budget_file_path = os.path.join("Resources", "budget_data.csv").replace("\\","/")
with open(budget_file_path,'r') as budget_file_memory_location:
    budget_file_read_content = csv.reader(budget_file_memory_location, delimiter = ",")
    next(budget_file_read_content) #skips the header, within the same WITH
    for row in budget_file_read_content:
        #Calculate total months
        total_months += 1

        #Calculate net profit
        net_profit = net_profit + int(row[1])

        #Calculate step profit
        current_profit = int(row[1])
        step_profit = current_profit - previous_profit
        step_profit_list.append(step_profit)
        previous_profit = int(row[1])

        #Calculate max/min and month on a rolling basis
        max_step_profit = max(step_profit_list)
        if (max_step_profit == step_profit):
            max_step_profit_month = row[0]
        min_step_profit = min(step_profit_list)
        if (min_step_profit == step_profit):
            min_step_profit_month = row[0]

#Post data-reading calculations
step_profit_list.pop(0) #removes the first value, which from the loop is just the first step profit - 0.
average_step_profit = round(sum(step_profit_list) / len(step_profit_list),2)

#Print answers
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_step_profit}")
print(f"Greatest Increase in Profits: {max_step_profit_month} $({max_step_profit})")
print(f"Greatest Decrease in Profits: {min_step_profit_month} $({min_step_profit})")

#Export file
export_file_path = os.path.join("Analysis","export.txt").replace("\\","/")
with open(export_file_path,'w') as export_file_memory_location:
    export_file_created = csv.writer(export_file_memory_location, lineterminator = '\n')
    
    export_file_created.writerow(["Financial Analysis"])
    export_file_created.writerow(["----------------------------"])
    export_file_created.writerow([f"Total Months: {total_months}"])
    export_file_created.writerow([f"Total: ${net_profit}"])
    export_file_created.writerow([f"Average Change: ${average_step_profit}"])
    export_file_created.writerow([f"Greatest Increase in Profits: {max_step_profit_month} $({max_step_profit})"])
    export_file_created.writerow([f"Greatest Decrease in Profits: {min_step_profit_month} $({min_step_profit})"])