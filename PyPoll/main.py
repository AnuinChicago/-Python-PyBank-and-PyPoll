import os
import csv

# Path to collect data from the Resources folder
PyPoll_csv = os.path.join('', 'Resources', 'election_data.csv')

#declare lists etc
Candidates = []
Total_voters = []
count = 0
Total_votes = []
percent_votes = []
candidate_percent = []
highest_index = 0

# Read in the CSV file
with open(PyPoll_csv, encoding ='utf-8') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        # Calculate the total number of voters
        Total_voters.append(row[0])

        #Calculate the list of Candidates who received votes and total votes each candidate won
        candidate = row[2]
        if candidate in Candidates:
            candidate_index = Candidates.index(candidate)
            Total_votes[candidate_index] = Total_votes[candidate_index] +1
        else:
            Candidates.append(candidate)
            Total_votes.append(1)

    
    #Calculate the % votes for each candidate 
    highest_count =Total_votes[0]       
    for i in range(len(Candidates)):
        percent_votes = round((Total_votes[i]/len(Total_voters))*100, 1)
        candidate_percent.append(percent_votes)
    #Calculate the Winner
        if Total_votes[i] > highest_count:
            highest_count = Total_votes[i]
            highest_index = i  
       
   
    print("Election Results")
    print("-------------------------")
    print(f'Total Voters: {len(Total_voters)}')    
    print("-------------------------")
    for i in range(len(Candidates)):
        print(f'{Candidates[i]}: {candidate_percent[i]}% ({Total_votes[i]})')
    print("-------------------------")
    print(f'Winner:{Candidates[highest_index]}')
   
 
           