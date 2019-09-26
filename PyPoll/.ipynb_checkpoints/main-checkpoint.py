import os
import csv

pathPyPoll = os.path.join("Resources", "election_data.csv")
voted_names = []
candidate_list = []
each_votes = []
percent_votes = []

def percent(part, whole): # Create Percentage calculator function
    return round(((part/whole)*100), 3)

with open(pathPyPoll, newline='') as filePyPoll:
    PyPoll_reader = csv.reader(filePyPoll, delimiter=',')
    PyPoll_header = next(PyPoll_reader)
    
    for row in PyPoll_reader:
        voted_names.append(row[2]) # Create list of voted candidates for loops
        total_votes = len(voted_names) # Find total number of votes cast
#Total Votes: 3521001 CHECKed

    # Each unique candidate name
    for name in voted_names: # Name checker to create unique candidate list
        if name not in candidate_list:
            candidate_list.append(name)
#['Khan', 'Correy', 'Li', "O'Tooley"] CHECKed

    # Votes per candidate
    for i in range(len(candidate_list)): # For each candidate:
        if candidate_list[i] in voted_names: # Count the matching name
            each_votes.append(voted_names.count(candidate_list[i])) # Make vote list
#[2218231, 704200, 492940, 105630] CHECKed

    # % of votes
    for j in range(len(each_votes)): # For each candidate's votes
        percent_votes.append(percent(each_votes[j],total_votes)) # Make % list using '% calc'
#[63.0, 20.0, 14.0, 3.0] CHECKed

    # Find winner
    winner = candidate_list[percent_votes.index(max(percent_votes))]
#Khan CHECKed

PyPoll_export = 'Election Results.txt' # Export as txt

with open(PyPoll_export, 'w') as export_text:
    export_text.write("Election Results\n")
    export_text.write("-"*30 + "\n")
    export_text.write(f"Total Votes: {total_votes}\n")
    export_text.write("-"*30 + "\n")
    for k in range(len(candidate_list)):
        export_text.write(f"{candidate_list[k]}: {percent_votes[k]}% ({each_votes[k]}) \n")
    export_text.write("-"*30 + "\n")
    export_text.write(f"Winner: {winner} \n")
    export_text.write("-"*30)