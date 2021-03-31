# Bring in the modules

import os
import csv
import sys

# Connect to csv file

bank_path = os.path.join('PyBank/Resources/Budget_data.csv')

# Create variables

months_total = 0
month_change_list = []
net_change_list_month = []
total_net = 0

greatest_increase = ["",0]
greatest_decrease = ["",9999999]


# Read data from csv file

with open(bank_path) as csvfile:

    bank_reader = csv.reader(csvfile, delimiter=',')
    next(bank_reader)

    # establish first row, values for total months, net, and previous net to calculate average net
    first_row = next(bank_reader)
    months_total += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # loop to read all rows
    for row in bank_reader:

        # calculate month count
        months_total += 1
        
        # calculate total profit/loss
        total_net += int(row[1])

        # values for month-to-month changes to calculate average change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list_month += [net_change]
        month_change_list += [row[0]]

        # calculate average change
        avg_chg = round(sum(net_change_list_month)/len(net_change_list_month),2)

        # conditions for greatest increase/decrease
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Print final results

results = (f" Total Months: {months_total} \n Total Profit/Loss: ${total_net} \n Average Change: ${avg_chg} \n Greatest Increase in Profits: {greatest_increase} \n Greatest Decrease in Profits: {greatest_decrease}")

print("Financial Analysis")
print("-----------------------------------------------------------------")
print(results)

sys.stdout = open('FinAnalysis.txt', 'w')

print("Financial Analysis")
print("-----------------------------------------------------------------")
print(results)