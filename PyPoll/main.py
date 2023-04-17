import os 
import csv
from collections import Counter

#define variables
total_votes=0

candidate_list= []
candidate_votes={}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

file_to_save = os.path.join("Analysis", "PyPoll.txt")
csvpath = os.path.join ('Resources', 'election_data.csv')
with open(csvpath, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #loop through rows
    for row in csvreader:
        #Total number of votes cast 
        total_votes = total_votes + 1
        #Format results for printing
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:}\n"
        f"-------------------------\n")
        candidate_name= row[2]
      
        #A list of candidates who received votes
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            #track number of votes for each candidate, starting at 0, candidate votes serves as dictionary
            candidate_votes[candidate_name] = 0
            #add votes for each candidate by looping through rows
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        #Obtain vote count and percentage
        for candidate_name in candidate_votes:
            #pulls candidate/ total votes name out of dictionary (value,key)
            votes = candidate_votes.get(candidate_name)
            #calculate vote percentage
            vote_percentage = (votes) / (total_votes) * 100
            candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n")
            print(candidate_results)
            #txt_file.write(candidate_results)
            #Identify winning candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
                print(f"-------------------------\n" f"Winner:{winning_candidate}" f"\n-------------------------\n")
    

print(election_results)
#print(candidate_results)

#with open(file_to_save, "w") as txt_file:
                
#print(election_results)
#print(candidate_results)
#print(f"-------------------------\n" f"Winner:{winning_candidate}" f"\n-------------------------\n")