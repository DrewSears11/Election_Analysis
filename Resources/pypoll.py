# The Data we need to retrieve
#1. Total number of votes cast
#2. Complete List of candidates who recieved votes
#3. Percentage of votes each candidate recieved
#4. Total number of votes each candidate won
#5. Winner of the election based on popular vote

import csv

import os

#assign a variable for the file to load and to the path

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file

with open(file_to_load) as election_data:


    #to do read and analyze the data here

    #read the file object with the reader function

    file_reader = csv.reader(election_data)

    #print the header row

    headers = next(file_reader)

    print(headers)
