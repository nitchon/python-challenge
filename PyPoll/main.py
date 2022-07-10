#PyPoll

import os
import csv

def calculations():
    ballot_count = 0
    unique_candidate= []
    vote_count = []
    vote_percentages = []
    for row in csvreader:
        ballot_count +=1
        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])
            vote_count.append(0)
        for candidate in unique_candidate:
            if row[2] == candidate:
                vote_count[unique_candidate.index(candidate)]+=1
    for vote in vote_count:
        vpcalc = (int(vote)/ballot_count)*100
        vote_percentages.append(vpcalc)
    candidate_zip=list(zip(unique_candidate,vote_count))
    winner = max(candidate_zip, key=lambda x:x[1])
    
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {ballot_count}')
    print("-------------------------")
    for candidate in unique_candidate:
        print(f'{candidate} {format(vote_percentages[unique_candidate.index(candidate)],".3f")}% ({vote_count[unique_candidate.index(candidate)]})')
    print("-------------------------")
    print(f'Winner: {winner[0]}')
    print("-------------------------")

    output_file = os.path.join("analysis","election_results.txt")
    with open(output_file, "w") as text:

        text.write(f"Election Results \n")
        text.write("----------------------------\n")
        text.write(f'Total Votes: {ballot_count}\n')
        text.write("----------------------------\n")
        for candidate in unique_candidate:
            text.write(f'{candidate} {format(vote_percentages[unique_candidate.index(candidate)],".3f")}% ({vote_count[unique_candidate.index(candidate)]})\n')
        text.write("-------------------------\n")
        text.write(f'Winner: {winner[0]}\n')
        text.write("-------------------------")   

csvpath = os.path.join("Resources","election_data.csv")



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    calculations()