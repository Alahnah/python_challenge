import os

import csv

CSV_PATH = os.path.join( 'resources','budget_data.csv')
PROFIT_IDX = 1

month_count = 0
total_profit = 0
avg_change = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        month_count = month_count + 1
        current_profit = int(row[PROFIT_IDX])
        total_profit = total_profit + current_profit
    
    print("Financial Analysis:")
    print("..................................................")
    print("total Months: " + str(month_count))
    print("Total: " + str(total_profit))

    revenue_change = []

    for x in range(1,):
        
        revenue_change.append((int(month_count[x]) - int(month_count[x-1])))

        revenue_change = int(month_count[x]) - int(month_count[x-1])
        avg_change.append(avg_change)
    avg_change = sum(revenue_change) / len(revenue_change)
    
    print("Average Change: " + str(avg_change))

    # max increase and decrease
    max_rev = max(avg_change)
    min_rev = min(avg_change)

    print("Greatest Increase in Profits: " + str(max_rev))
    print("Greatest Decrease in Profits: " + str(min_rev)

#output text
         
     file = open("output.txt","w")
    file.write("Financial Analysis:")
    file.write("....................................................")
    file.write("total Months: " + str(month_count))
    file.write("Total: " + str(total_profit))
    file.write(("Average Change: " + str(avg_change))
    file.write("Greatest Increase in Profits: " + str(max_rev))
    file .write("Winner: " + str(max_candidate))
    file.write("Greatest Decrease in Profits: " + str(min_rev)
    file.close()