#PyBank

import os
import csv

def calculations():
    total_months = 0
    net_total = 0
    change_total = 0
    intial = 0 
    tracking_change = []
    date = []
    for row in csvreader:
        total_months +=1
        date.append(row[0])
        net_total = net_total + int(row[1])
        if total_months == 1:
            final = int(row[1])
            monthly_change = 0
            tracking_change.append(monthly_change)
            change_total = change_total + monthly_change
            intial = final
        else:
            final = int(row[1])
            monthly_change = final - intial
            tracking_change.append(monthly_change)
            change_total = change_total + monthly_change
            intial = final
    average_change = change_total/(len(tracking_change)-1)
    greatest_inc = max(tracking_change)
    inc_date = date[tracking_change.index(greatest_inc)]
    greatest_dec = min(tracking_change)
    dec_date = date[tracking_change.index(greatest_dec)]

    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {inc_date} (${greatest_inc})')
    print(f'Greatest Decrease in Profits: {dec_date} (${greatest_dec})')
    output_file = os.path.join("analysis","budget_summary.txt")
    with open(output_file, "w") as text:
        text.write(f"Financial Analysis \n")
        text.write("----------------------------\n")
        text.write(f'Total Months: {total_months}\n')
        text.write(f'Total: ${net_total}\n')
        text.write(f'Average Change: ${average_change}\n')
        text.write(f'Greatest Increase in Profits: {inc_date} (${greatest_inc})\n')
        text.write(f'Greatest Decrease in Profits: {dec_date} (${greatest_dec})\n')

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    print("Financial Analysis")
    print("----------------------------")
    calculations()
    