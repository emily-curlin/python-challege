 #loop through rows
    for row in csvreader:
        #Total number of votes cast 
        total_votes = total_votes + 1
        #Define candidates
        candidate_name= row[2]
        #A list of candidates who received votes
        if candidate_name not in candidate_list:
            candidate_list.append(row[2])
        #track number of votes for each candidate, starting at 0, candidate votes serves as dictionary
            candidate_votes[candidate_name] = 0
        #add votes for each candidate by looping through rows
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        #Obtain vote count and percentage
    for candidate_name in candidate_votes:
        #pulls candidate/ total votes name out of dictionary (value,key)
        votes = candidate_votes.get(candidate_name)
        #calculate vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n")
        print(candidate_results)
        #Identify winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            print(winning_count)