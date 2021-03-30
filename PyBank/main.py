# Bring in the CSV file contents

import os
import csv

bank_path = os.path.join('PyBank', 'Resources', 'Assignments_03-Python_PyBank_Resources_budget_data.csv')

with open(bank_path) as csvfile:

    bank_reader = csv.reader(csvfile, delimiter=',')

    bank_header = next(bank_reader)

    # Get number of months in dataset 
    
    months = list(bank_reader)
    month_count = len(months)
    print(month_count)

    # Get net total amount of Profit/Losses

        for row in months:
        
        profit_loss = float(row[1])
        total += float(profit_loss)
        print(total)










