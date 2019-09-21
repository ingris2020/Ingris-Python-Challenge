# this is the main.py in PyBank
import os
import csv

#Type in File Name (e.g., Financial Analisys)
filename = input("Please enter the file name you would like to review:")
# Define the variables 
total_revenue = 0
month_count = 0
current_month_revenue = 0
prior_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

# set the path
budget_data_csv = os.path.join("budget_data.csv")

# open the budget_data.csv and read rows
with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # loop to obtain monthly changes in revenue
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        current_month_revenue = int(row[1])
        total_revenue = total_revenue + current_month_revenue
        if month_count > 1 :
            revenue_change = current_month_revenue - prior_month_revenue
            revenue_changes.append(revenue_change)
        prior_month_revenue = current_month_revenue 

# Month by month analysis
sum_revenue_changes = sum(revenue_changes)
average_change = round(sum_revenue_changes/(month_count - 1), 2)#find out how to round out this number
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change) + 1
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index ]
min_month = months[min_month_index ]


# print the finanacial analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {month_count} ")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in profits: {max_month} (${max_change})")
print(f"Greatest Decrease in profits: {min_month} (${min_change})")


# write it to a text file
save_file = filename.strip(".csv") + "_result_txt"
filepath = os.path.join("..", "PyBank_output.txt")

# open the file and write rows with description
with open(filepath, 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: ${total_revenue}" + "\n")
    text.write(f"Average Revenue Change: ${average_change}" + "\n")
    text.write(
        f"Greatest increase in profits: {max_month} (${max_change})" + "\n")
    text.write(
        f"Greatest decrease in profits: {min_month} (${min_change})" + "\n")
