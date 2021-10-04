#Storage variables
total_votes = 0
votes_by_candidate = [0, 0, 0, 0]
percent_vote_by_candidate = [0, 0, 0, 0]
candidate_names = ["Khan", "Correy", "Li", "O'Tooley"]
    #[0] Khan
    #[1] Correy
    #[2] Li
    #[3] O'Tooley
winner = ""

#Import modules
import os
import csv

#Get data from file
election_file_path = os.path.join("Resources", "election_data.csv").replace("\\","/")
with open(election_file_path,'r') as election_file_memory_location:
    election_file_read_content = csv.reader(election_file_memory_location, delimiter = ",")
    next(election_file_read_content) #skips the header, within the same WITH
    for row in election_file_read_content:
        #Calculating total votes
        total_votes += 1
        
        #Loop through candidate array to check matches, then add vote to that candidate
        for candidate_names_element in candidate_names:
            if (row[2] == candidate_names_element):
                votes_by_candidate[candidate_names.index(candidate_names_element)] += 1
#Summing up total votes
total_votes = sum(votes_by_candidate)

#Determining winner
winner = candidate_names[votes_by_candidate.index(max(votes_by_candidate))]

#Calculating and populating percentage list
for i in range(0, len(percent_vote_by_candidate)):
    percent_vote_by_candidate[i] = "{:.3%}".format(votes_by_candidate[i] / total_votes)

#Print data
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {sum(votes_by_candidate)}")
print(f"-------------------------")
for i in range(0, len(candidate_names)):
    print(f"{candidate_names[i]}: {percent_vote_by_candidate[i]} ({votes_by_candidate[i]})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Exporting data to file
export_file_path = os.path.join("Analysis","export.txt").replace("\\","/")
with open(export_file_path, 'w') as export_memory_location:
    export_writer = csv.writer(export_memory_location, lineterminator = '\n')
    export_writer.writerow(["Election Results"])
    export_writer.writerow(["-------------------------"])
    export_writer.writerow([f"Total Votes: {sum(votes_by_candidate)}"])
    export_writer.writerow(["-------------------------"])
    for i in range(0, len(candidate_names)):
        export_writer.writerow([f"{candidate_names[i]}: {percent_vote_by_candidate[i]} ({votes_by_candidate[i]})"])
    export_writer.writerow(["-------------------------"])
    export_writer.writerow([f"Winner: {winner}"])
    export_writer.writerow(["-------------------------"])