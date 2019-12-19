import os
import pandas as pd
data_file = "resources/election_data.csv"
data_file_df = pd.read_csv(data_file)
#print(data_file_df.head())
total_votes = data_file_df["Voter ID"].count()
#print(total_votes)
candidates = data_file_df["Candidate"].unique()
vote_count = []
for name in candidates:
    name = data_file_df.loc[data_file_df["Candidate"] == name, :]
    vote_count.append(name["Voter ID"].count())

Candidates_votes_df = pd.DataFrame({
    "Candidates": candidates,
    "Votes": vote_count
})

max_votes = Candidates_votes_df["Votes"].max()
winner = Candidates_votes_df.loc[Candidates_votes_df["Votes"] == max_votes, :]
winner_name = winner.iloc[0,0]

Candidates_votes_df["Percentage"] = Candidates_votes_df["Votes"]/total_votes
new_sort_df = Candidates_votes_df.sort_values("Percentage", ascending=False)
new_sort_df_index = new_sort_df.reset_index(drop=True)

print("Election Results\n")
print("-----------------\n")
print(f'Total Votes: {total_votes}\n')
print("-----------------\n")
print(f'{new_sort_df_index}\n')
print("-----------------\n")
print(f'Winner: {winner_name}')

file = open('PyPoll_output.txt',"w")
file.write("Election Results\n")
file.write("-----------------\n")
file.write(f'Total Votes: {total_votes}\n')
file.write("-----------------\n")
file.write(f'{new_sort_df_index}\n')
file.write("-----------------\n")
file.write(f'Winner: {winner_name}')

file.close()