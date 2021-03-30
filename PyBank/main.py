# Bring in the CSV file contents

import os
import csv

bank_path = os.path.join('GitHub', 'python-challenge', 'PyBank', 'Resources', 'Budget_data.csv')

columns = []
rows = []

with open(bank_path) as csvfile:

    bank_reader = csv.reader(csvfile, delimiter=',')
    columns = next(bank_reader)

    # Get number of months in dataset 
    
    months = list(bank_reader)
    month_count = len(months)
    print(month_count)

    # Get net total amount of Profit/Losses

    total = 0

    for row in bank_reader:
        rows.append(row)
        
        profit_loss = int(row[1])
        total += int(profit_loss)
        print(total)










