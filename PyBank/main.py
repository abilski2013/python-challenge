import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

Date = []
Profit_Losses = []
Change = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    csv_header = next(csvreader)
    count = []
    values = 0
    rows = 0
    rowtally = []
    for row in csvreader:
        Date.append(row[0])
        Profit_Losses.append(row[1])
        count.append(1)
        values = values + int(row[1])
        if int(rows) == 0:
            rows = int(row[1])
            Change.append(0)
        else:
            rowtally.append(int(row[1])-rows)
            rows = int(row[1])
            Change.append(int(row[1])-rows)

    def average(rowtally):
        length = len(rowtally)
        total = 0.0
        for number in rowtally:
            total += number
        return total / length

    #print(len(count))
    values = '${:,.2f}'.format(values)
    #print(average(rowtally))
    average_change = average(rowtally)
    average_change = '${:,.2f}'.format(average_change)
rowtally.insert(0,0) 
clean_csv = zip(Date, Profit_Losses, rowtally)
starter = 0
largest_increase_month = 0
largest_increase_value = 0
largest_decrease_month = 0
largest_decrease_value = 0
for column in clean_csv:
    if column[2] > largest_increase_value:
        largest_increase_month = column[0]
        largest_increase_value = column[2]
    elif column[2] < largest_decrease_value:
        largest_decrease_month = column[0]
        largest_decrease_value = column[2]

#print(largest_increase_month)
#print(largest_increase_value) 
largest_increase_value = '${:,.2f}'.format(largest_increase_value)
largest_decrease_value = '${:,.2f}'.format(largest_decrease_value)       
#print(largest_decrease_month)
#print(largest_decrease_value)
print("")
print("Financial Analysis")
print("")
print("-------------------")
print(f'Total Months: {len(count)}')
print(f'Total: {values}')
print(f'Average Changes: {average_change}')
print(f'Greatest Increase in Profits: {largest_increase_month} {largest_increase_value}')
print(f'Greatest Decrease in Profits: {largest_decrease_month} {largest_decrease_value}')

file = open('PyBank_output.txt',"w")
file.write("\n")
file.write("Financial Analysis\n")
file.write("\n")
file.write("-------------------\n")
file.write(f'Total Months: {len(count)}\n')
file.write(f'Total: {values}\n')
file.write(f'Average Changes: {average_change}\n')
file.write(f'Greatest Increase in Profits: {largest_increase_month} {largest_increase_value}\n')
file.write(f'Greatest Decrease in Profits: {largest_decrease_month} {largest_decrease_value}\n')

file.close()