import os
import pandas as pd
data_file = "resources/budget_data.csv"
data_file_pd = pd.read_csv(data_file)

months = data_file_pd["Date"].count()
#print(months)
total_profit = data_file_pd["Profit/Losses"].sum()
#print(total_profit)
total_profit = '${:,.2f}'.format(total_profit)
change_from_last = data_file_pd["Profit/Losses"] - data_file_pd["Profit/Losses"].shift(1)
data_file_pd["Change"] = change_from_last
#print(data_file_pd)

average_change = data_file_pd["Change"].mean()
#print(average_change)
average_change = '${:,.2f}'.format(average_change)
max_change_value = data_file_pd["Change"].max()
max_change_decrease = data_file_pd["Change"].min()
#print(max_change_value)
#print(max_change_decrease)
max_increase_date = data_file_pd.loc[data_file_pd["Change"] == max_change_value, :]
#print(max_increase_date)
max_decrease_date = data_file_pd.loc[data_file_pd["Change"] == max_change_decrease, :]
#print(max_decrease_date)
max_date = max_increase_date.iloc[0,0]
min_date = max_decrease_date.iloc[0,0]
max_change_value = '${:,.2f}'.format(max_change_value)
max_change_decrease = '${:,.2f}'.format(max_change_decrease)


print("Financial Analysis\b")
print("------------------\b")
print(f'Total Months: {months}\b')
print(f'Total: {total_profit}\b')
print(f'Average Change: {average_change}\b')
print(f'Greatest Increase: {max_date} ({max_change_value})\b')
print(f'Greatest Decrease: {min_date} ({max_change_decrease})\b')

file = open('PyBank_output.txt',"w")
file.write("Financial Analysis\n")
file.write("------------------\n")
file.write(f'Total Months: {months}\n')
file.write(f'Total: {total_profit}\n')
file.write(f'Average Change: {average_change}\n')
file.write(f'Greatest Increase: {max_date} ({max_change_value})\n')
file.write(f'Greatest Decrease: {min_date} ({max_change_decrease})\n')
file.close()