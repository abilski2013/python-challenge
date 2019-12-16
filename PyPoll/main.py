import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    countvotes = []
    candidates = []
    candidate1 = []
    candidate2 = []
    candidate3 = []
    candidate4 = []

    for row in csvreader:
        countvotes.append(1)
        if row[2] not in candidates:
            candidates.append(row[2])
        
        if row[2] == candidates[0]:
            candidate1.append(1)
        elif row[2] == candidates[1]:
            candidate2.append(1)
        elif row[2] == candidates[2]:
            candidate3.append(1)
        elif row[2] == candidates[3]:
            candidate4.append(1)


total_votes = len(countvotes)
candidate1_votes = len(candidate1)
candidate2_votes = len(candidate2)
candidate3_votes = len(candidate3)
candidate4_votes = len(candidate4)

candidate1_percent = candidate1_votes/total_votes
candidate2_percent = candidate2_votes/total_votes
candidate3_percent = candidate3_votes/total_votes
candidate4_percent = candidate4_votes/total_votes

if candidate1_votes > candidate2_votes and candidate3_votes and candidate4_votes:
    winner = candidates[0]
elif candidate2_votes > candidate1_votes and candidate3_votes and candidate4_votes:
    winner = candidates[1]
elif candidate3_votes > candidate2_votes and candidate1_votes and candidate4_votes:
    winner = candidates[2]
elif candidate4_votes > candidate2_votes and candidate3_votes and candidate1_votes:
    winner = candidates[3]


print("\n")
print("Election Results\n")
print("--------------------------\n")
print(f'Total Votes: {total_votes}\n')
print("--------------------------\n")
print(f'{candidates[0]}: {"{:.2%}".format(candidate1_percent)} ({candidate1_votes}) ')
print(f'{candidates[1]}: {"{:.2%}".format(candidate2_percent)} ({candidate2_votes}) ')
print(f'{candidates[2]}: {"{:.2%}".format(candidate3_percent)} ({candidate3_votes}) ')
print(f'{candidates[3]}: {"{:.2%}".format(candidate4_percent)} ({candidate4_votes}) \n')
print("--------------------------\n")
print(f'Winner: {winner}')

file = open('PyPoll_output.txt',"w")
file.write("\n")
file.write("Election Results\n")
file.write("--------------------------\n")
file.write(f'Total Votes: {total_votes}\n')
file.write("--------------------------\n")
file.write(f'{candidates[0]}: {"{:.2%}".format(candidate1_percent)} ({candidate1_votes}) \n')
file.write(f'{candidates[1]}: {"{:.2%}".format(candidate2_percent)} ({candidate2_votes}) \n')
file.write(f'{candidates[2]}: {"{:.2%}".format(candidate3_percent)} ({candidate3_votes}) \n')
file.write(f'{candidates[3]}: {"{:.2%}".format(candidate4_percent)} ({candidate4_votes}) \n')
file.write("--------------------------\n")
file.write(f'Winner: {winner}')

file.close()
