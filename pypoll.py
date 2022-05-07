# the data we need to retrieve
# 1. The total number of votes cast
# 2. The complete list of candiadates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
Winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] =0

        # add vote to candidates count
        candidate_votes[candidate_name] += 1

    # save results to a text file
    with open(file_to_save, "w") as txt_file:

        #Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"{'-'*25}\n"
            f"Total votes: {total_votes:,}\n"
            f"{'-'*25}\n")
        print(election_results, end="")
        # Save this final voter count to a text file
        txt_file.write(election_results)

        for candidate_name in candidate_votes:
            # Retrieve vote count and percentage.
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage to the terminal.
            print(candidate_results,)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # 1 determine if votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > Winning_percentage):
                # 2 if true then set winning_count = votes and winning_percent= vote percent
                winning_count = votes
                Winning_percentage = vote_percentage
                # 3 set the winning_candidate = candidates_name
                winning_candidate = candidate_name

        winning_candidate_Summary = (
            f"{'-'*40}\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count}\n"
            f"Winning percentage: {Winning_percentage:.1f}%\n"
            f"{'-'*40}\n")
        print(winning_candidate_Summary)
        # save the winning cadidate's results to a text file
        txt_file.write(winning_candidate_Summary)

