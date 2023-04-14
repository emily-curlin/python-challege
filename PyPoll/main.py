import os 
import csv
from collections import Counter

#define variables
total_votes=0
ccs_percent_votes=0
ccs_total_votes=0
dg_percent_votes=0
dg_total_votes=0
rad_percent_votes=0
rad_total_votes=0
candidates_dict= {}


csvpath = os.path.join ('Resources', 'election_data.csv')
with open(csvpath, "r") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    dictionary= csv.DictReader(csvfile)
    print(candidates_dict)
    csv_header = next(csvreader)
    candidates_list=[]
    total_votes= 0
    
    #loop through rows
    for row in csvreader:
        #Total number of votes cast 
        total_votes = total_votes + 1
    
        #A list of candidates who received votes
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
    

#Total number of votes each candidate won 
for key in candidates_list.key():
    print(key) 
    
for value in candidates_list.values():
    print(value) 

for key, value in some_dict.items():
    print(key, value)

'''name = "    
if name in some_dict:
    print(f"{name} is in some_dict and has {some_dict['John']} votes.")

if name in some_dict:
    # This is not the first time someone has voted for name...
    # Increment their vote count by 1...
    some_dict[name] = some_dict[name] + 1
else:
    # This is the first time soeone has voted for name...
    # Add name to dict and set initial vote count to 1...
    some_dict[name] = 1








print ("Election Results")

print ("------------------------")

print (f"Total Votes: {total_votes}")

print ("-------------------------")

#print (f"Charles Casper Stockham: {ccs_percent_votes}%  ({ccs_total_votes})")
#print (f"Diana GeGette: {dg_percent_votes}%  ({dg_total_votes})")
#print (f"Raymon Anthony Doane: {rad_percent_votes}%  ({rad_total_votes})")

print ("-------------------------")

#print (f"Winner: {most_pop_votes}")

print ("-------------------------")

'''