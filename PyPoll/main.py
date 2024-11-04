# import modules
import csv
import os

# load in the CSV file
fileLoad = os.path.join("Resources/election_data.csv")

# file to hold the output of the polling data
outputFile = os.path.join("Analysis/election_data.txt")

# variables
totalVotes = 0                          # initialize total votes to 0
candidates = []                         # list of candidates
candidateVotes = {}                     # dictionary of the votes for the candidates
winningCount = 0                        # hold the winning count
winningCandidate = ""                   # hold the winning candidate


# read the CSV file
with open(fileLoad) as electionData:
    # csv reader
    csvreader = csv.reader(electionData)

    # read the header row
    header = next(csvreader)

    # rows will be lists
        # index 0 is the ballot id
        # index 1 is the county
        # index 2 is the candidate


    for row in csvreader:
        totalVotes += 1                             # count of total votes

        if row[2] not in candidates:                # check to see if the candidate is in the list of candidates
            candidates.append(row[2])               # if not on the list, add the candidate to the list
            candidateVotes[row[2]] = 1              # add the value to the dictionary 
        else:
            candidateVotes[row[2]] += 1             # the candidate is on the list - add a vote to the count 

voteOutput = ""

for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)                   # get the vote count
    votePct = (float(votes) / float(totalVotes)) * 100.00   # get the percentage of the votes


    # variable
    voteOutput += f"\t{candidate}: {votePct:.3f}% {votes}\n"

    if votes > winningCount:                            # compare the votes to the winning count 
        winningCount = votes                            # update the votes to be the new winning count
        winningCandidate = candidate                    # update the winning candidate

winningCandidateOutPut = f"Winner: {winningCandidate}\n-----------------------"        


# create output variable to hold the information
output = (
    f"\n\nElection Results\n"
    f"--------------------\n"
    f"\tTotal Votes: {totalVotes:,}\n"
    f"---------------------\n"
    f"{voteOutput}\n"
    f"----------------------\n"
    f"{winningCandidateOutPut}\n"
    )

# displays to the console/terminal
print(output)

# print the results to the txt file
with open(outputFile, "w") as textFile:
    textFile.write(output)