# The Data we need to retrieve
#1. Total number of votes cast


#4. Total number of votes each candidate won
#5. Winner of the election based on popular vote

#add our dependencies

import csv

import os

#assign a variable for the file to load and to the path

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")


#Initalize a total votes counter

total_votes = 0

#2. Complete List of candidates who recieved votes
#create a candidate options list (array using []) and candidate votes dictionary

candidate_options = []

#declare the empty dictionary (dictionary uses {})

candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


# open the election results and read the file

with open(file_to_load) as election_data:


    #to do read and analyze the data here

    #read the file object with the reader function

    file_reader = csv.reader(election_data)

    #print the header row

    headers = next(file_reader)

    # print each row in the csv file

    for row in file_reader:

        # add the total number of votes count

        total_votes += 1

        #print candidate names from each row

        candidate_name = row[2]

        #create an if loop so we do not print duplicate names

        if candidate_name not in candidate_options:

        #add the candidate name to the candidate list

            candidate_options.append(candidate_name)

        # begin tracking candidate votes

            candidate_votes[candidate_name] = 0 

        #add a vote to that candidates name

        candidate_votes[candidate_name] += 1

#3. Percentage of votes each candidate recieved

# Iterate through the candidate list 

for candidate_name in candidate_votes:

    #Retreive vote count of a candidate

    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes

    vote_percentage = float(votes) / float(total_votes) * 100

     #  To do: print out each candidate's name, vote count, and percentage of
     # votes to the terminal.

     
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         
         winning_count = votes
         
         winning_percentage = vote_percentage
         
         # And, set the winning_candidate equal to the candidate's name.
        
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.

winning_candidate_summary = (
    
    f"-------------------------\n"
    
    f"Winner: {winning_candidate}\n"
    
    f"Winning Vote Count: {winning_count:,}\n"
    
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    
    f"-------------------------\n")

print(winning_candidate_summary)


