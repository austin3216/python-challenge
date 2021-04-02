# Import modules

import os
import csv

# Connect to csv file

csv_path = os.path.join('/Users/amber/Desktop/GitHub/python-challenge/PyPoll/Resources/Election_data.csv')

# Create variables

total_votes = 0
winner_votes = 0
candidates = {}
winner = ""

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

# Define the results for printing to terminal and text file

results1 = (f"Election Results \n--------------------------------------\n\
Total Votes: {total_votes} \n--------------------------------------\n")

# terminal print

print(results1)

# text file creation and print

with open('Election_Results', 'w') as txt_file:
    txt_file.write(results1)

# Loop through repeated candidate data, isolate individual data
for candidate, votes in candidates.items():    

    # calculate percentage of votes for each candidate
    pct_vote = '{0:.2f}'.format((votes / total_votes * 100))

    # print candidates with their % votes and total vote counts
    results2 = (f"{candidate}: {pct_vote} ({votes})\n")

    print(results2)

    # append results to text file

    with open('Election_Results', 'a') as file_object:
        file_object.write(results2)
    
    # set condition for winner
    if votes > winner_votes:
        
        # I had this reversed (votes = winner_votes); credit Han-se (professor)
        winner_votes = votes
        winner = candidate

results3 = (f"--------------------------------------\n\
Winner: {winner}\n--------------------------------------")

print(results3)

# append results to text file

with open('Election_Results', 'a') as file_object:
        file_object.write(results3)