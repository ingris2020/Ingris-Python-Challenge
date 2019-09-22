# this is main.py in PyPoll
import os
import csv

# initialize the variables
#filename = input("Wouild you like to see the Election Results:")
total_votes = 0
candidate = ""
vote_details = {}
winner_votes = 0
winner = ""
candidate_list = []
voter_id = []
vote_count=[] #empty list to count votes from vote details
counter= 0
candidate_total = []

# set the path
election_data_csv = os.path.join("..", "election_data.csv")

# open the budget_data.csv and read the rows
with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #loop to count total votes by counting all rows
    for row in csvreader:
        voter_id.append(row[0])
        candidate_list.append(row[2])
        vote_details[row[0]]=row[2] 

#Total election votes 
total_votes = len(vote_details)

#List of candidate names
candidate_name= list(set(candidate_list))

#Loop to tally votes per candidate
for vote in range(len(candidate_name)):
    count =0
    for i in vote_details.values():
        if i == candidate_name[vote]:
            count = count + 1
    vote_count.append(count)

#Candidate with max votes    
max_vote_index = vote_count.index(max(vote_count))
#
candidate_percentage = []
max_votes  = vote_count[0]
max_index = 0
#Calculate Percentages per candidate
for p in range(len(vote_details)):
    vote_percentage = int(vote_count[p])/total_votes*100
    candidate_percentage.append(vote_percentage)
    if vote_count[p]>max_vote_index:
        max_votes = vote_count[p]
        print(max_votes)
        max_index = count
winner=candidate_list[max_index]

candidate_percentage=[round(p,2) for i in candidate_percentage]

print(candidate_percentage)
print(total_votes)
print(candidate_name)
print(winner)
print(max_index)
"""
print(winner_votes)
print(total_votes)
print(candidate_name)
print(max_vote)
print(winner)
"""
"""#Print Election Results
dashbreak="-------------------------------------"
print("Elections Results")
print(dashbreak)
print(f"Total Votes:{total_votes}")
print(dashbreak)
#loop to display percentages
for i in range(len(candidate_name)):
    print(candidate_name[i] + ":" + str(pe))
print(f"Winner:{winner}")
print(dashbreak

# Write it to a text file
save_file = filename.strip(".csv") + "_result_txt"
filepath = os.path.join("..", "PyPoll_output.txt")

# open the file and write rows with description
with open(filepath, 'w') as text:
    text.write("Election Results" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Total Votes:{total_votes}" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Percentage of Votes:{}" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Winner:{winner}" + "\n")"""