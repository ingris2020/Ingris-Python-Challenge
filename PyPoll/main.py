# this is main.py in PyPoll
import os
import csv
import operator
import numpy as np

# initialize the variables
filename = input("Wouild you like to see the Election Results:")
total_votes = 0
candidate = ""
vote_details = {}
winner_votes = 0
winner = ""
candidate_list = {}
voter_id = []
vote_count=[] #empty list to count votes from vote details
counter= 0
vote_percentage = 0.0

# set the path
election_data_csv = os.path.join("..", "election_data.csv")

# open the budget_data.csv and read the rows
with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #loop to count total votes by counting all rows
    for row in csvreader:
        candidate=row[2]
        if candidate not in vote_details:
            vote_details.update( {candidate:1}) #1 means the start
        elif candidate in vote_details:
            d={candidate:vote_details.get(candidate)+1}
            vote_details.update(d)

print(vote_details)

#This returns the key that correspondent the max value
winner = max(vote_details.items(), key=operator.itemgetter(1))[0]
print(winner)


#vote_percentage 
#loop to obtain percentages
total_votes=sum(vote_details.values())
for candidate, votes in vote_details.items():
    vote_percentage=votes*100.0/total_votes
    print(candidate, votes, vote_percentage)

vote_count=[candidate, votes, vote_percentage]
print(vote_count) 


#Print Election Results
dashbreak="--------------------------------------------"
print("Elections Results")
print(dashbreak)
print(f"Total Votes:{total_votes}")
print(dashbreak)
for candidate, votes in vote_details.items():
    vote_percentage=votes*100.0/total_votes
    print(candidate, votes, vote_percentage)
print(dashbreak)
print(f"Winner:{winner}")
print(dashbreak)

# Write it to a text file
save_file = filename.strip(".csv") + "_result_txt"
filepath = os.path.join("..", "PyPoll_output.txt")

# open the file and write rows with description
with open(filepath, 'w') as text:
    text.write("Election Results" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Total Votes:{total_votes}" + "\n")
    text.write(dashbreak + "\n")
    for candidate, votes in vote_details.items():
        vote_percentage=votes*100.0/total_votes
        text.write(f"{candidate} {votes} {vote_percentage}" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Winner:{winner}" + "\n")
