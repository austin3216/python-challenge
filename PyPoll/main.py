# Import modules

import os
import csv

# Connect to csv file

csv_path = os.path.join('PyPoll/Resources/Election_data.csv')

# Create variables

total_votes = 0
candidates = []
pct_votes_cand = ["", 0]
tot_votes_cand = ["", 0]
winner = ""

# Read csv file

with open(csv_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)

    first_row = next(csv_reader)
    total_votes += 1

    for row in csv_reader:
        total_votes += 1

print(total_votes)



