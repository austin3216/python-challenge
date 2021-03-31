# Import modules

import os
import csv
import sys

# Connect to csv file

csv_path = os.path.join('PyPoll/Resources/Election_data.csv')

# Create variables

total_votes = 0
winner_votes = 0
candidates = {}

# Read csv file

with open(csv_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)

    # set the first row of data
    first_row = next(csv_reader)
    total_votes += 1

    # loop through the rows
    for row in csv_reader:

        # calculate total votes
        total_votes += 1
        
        # get number of times/rows candidate name repeated (votes)
        candidates[row[2]] = candidates.get(row[2], 0) + 1

# Need another loop to isolate candidate data...
    
    # calculate percentage of votes each candidate
    pct_vote = # need to format as percent... some variable for candidate votes / total_votes * 100
    
    # condition for winner
    if # candidate votes > winner_votes:
        # candidate votes = winner_votes
        winner = # candidate from list

# Print results

print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------------------")
# print(candidate list with percent and total votes) - do this in or outside of loop?
print("--------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------")

# sys.stdout = open('PollResults.txt', 'w')
