# import necessary sub programs
import os
import csv

# create variable to call program
def election_analysis(csvpath):

    # define lists and intial values
    candidates = []
    percentage_votes = []
    total_candidate_votes = []
    total_cast_votes = 0
    vote_1_total = 0
    vote_2_total = 0
    vote_3_total = 0

    # open and read csv file
    with open(csvpath, encoding='utf') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # store and skip header row
        csv_header = next(csvreader)

        # loop through data
        for row in csvreader:

            # row count = number of votes
            total_cast_votes += 1

            # pull unique candidates and input them into a list
            if row[2] not in candidates:
                candidates.append(row[2])

            # for each candidate, count their vote totals
            if candidates[0] == row[2]:
                vote_1_total += 1
            elif candidates[1] == row[2]:
                vote_2_total += 1
            elif candidates[2] == row[2]:
                vote_3_total += 1

    # input candidate vote totals into a list
    total_candidate_votes.append(vote_1_total)
    total_candidate_votes.append(vote_2_total)
    total_candidate_votes.append(vote_3_total)

    # input candidate vote percentatges into a list
    percentage_votes.append(round(vote_1_total / total_cast_votes * 100, 3))
    percentage_votes.append(round(vote_2_total / total_cast_votes * 100, 3))
    percentage_votes.append(round(vote_3_total / total_cast_votes * 100, 3))

    # combine all three lists into a zip
    poll = list(zip(candidates, percentage_votes, total_candidate_votes))

    # determine max value in votes column and define variables for each column
    winner, winning_percentage, winning_votes = max(poll, key=lambda x: x[2])

    # save results into a list
    result = []
    result.append("Electon Results")
    result.append("--------------------------------")
    result.append(f'Total Votes: {total_cast_votes}')
    result.append("--------------------------------")
    result.append(f'{poll[0][0]}: {poll[0][1]}% ({poll[0][2]})')
    result.append(f'{poll[1][0]}: {poll[1][1]}% ({poll[1][2]})')
    result.append(f'{poll[2][0]}: {poll[2][1]}% ({poll[2][2]})')
    result.append("--------------------------------")
    result.append(f'Winner: {winner}')
    result.append("--------------------------------")
    return result

# establish read and write paths
csvpath = "/Users/ronaldlam/Desktop/University_of_Toronto_2022:23/01-Data-Bootcamp/01-Weekly-Notes/03-Week-3-Python/module-3-challange/PyPoll/Resources/election_data.csv"
outputpath = "/Users/ronaldlam/Desktop/University_of_Toronto_2022:23/01-Data-Bootcamp/01-Weekly-Notes/03-Week-3-Python/module-3-challange/PyPoll/analysis/results.txt"

# print results
analysis = election_analysis(csvpath)
print("\n".join(analysis))

# create text file and write results
with open(outputpath, 'w') as file:
    file.write("\n".join(analysis))
