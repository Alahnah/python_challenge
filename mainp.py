import os

import csv

CSV_PATH = os.path.join( 'resources','election_data.csv')

vote_count = 0
candidate = []
candidate_vote_count = {}

count = 0
perc_count = 0
max_candidate = ""

with open(CSV_PATH) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #total votes
    for row in csvreader:
        vote_count = vote_count + 1
    
        candidate_name = row[2]

        #new candidate name
        if candidate_name not in candidate:
            
            #add name to end of list & total vote count/candidate
            candidate.append(candidate_name)
            candidate_vote_count[candidate_name] = 0
        
        candidate_vote_count[candidate_name] += 1

    print("Election Results:")
    print("....................................................")
    print("Total Votes: " + str(vote_count))
    print("....................................................")
    for candidate_name in candidate:
        votes = candidate_vote_count[candidate_name]
        percentage = float(votes) / float(vote_count) * 100
        results = (f"{candidate_name}: {percentage:}% ({votes:})")
        print(results)


   
    # popular vote 

    if (votes > count) and (percentage > perc_count):
        count = votes
        perc_count = percentage 

        max_candidate = candidate_name
        print("...............................................")
        print("Winner: " + str(max_candidate))
        print("...............................................")

# to text file

    file = open("output.txt","w")
    file.write("Election Results:")
    file.write("....................................................")
    file.write("Total Votes: " + str(vote_count))
    file.write("....................................................")
    file.write(results)
    file.write("...............................................")
    file .write("Winner: " + str(max_candidate))
    file.write("...............................................")
    file.close()