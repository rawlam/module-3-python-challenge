# import necessary sub programs
import os
import csv

# create variable to call program
def budget_analysis(csvpath):

    # establish initial values and lists
    total_months = 0
    total_profit = 0
    temp = 0
    change = 0
    total_change = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]

    # open and read csv file
    with open(csvpath, encoding='utf') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # store and skip header row
        csv_header = next(csvreader)

        # loop through data
        for row in csvreader:

            # row count = number of months
            total_months += 1

            # establishing labels with corresponding data columns
            month = row[0]
            profit = int(row[1])

            # sum value of each row
            total_profit += profit
            
            # calculate profit change between months 
            change = profit - temp

            # Sum change over the whole data set
            total_change += change

            # save previous profit value for next change calculation
            temp = profit

            # evaluate and store greatest profit change
            if change > greatest_increase[1]:
                greatest_increase = [month, profit]

            # evaluate and store greatest profit change
            if change < greatest_decrease[1]:
                greatest_decrease = [month, profit]

    # save results into a list
    result = []
    result.append("Financial Analysis")
    result.append("--------------------------------")
    result.append(f'Total Months: {total_months}')
    result.append(f'Total: ${total_profit}')
    result.append(f'Average Change: {round(total_change / (total_months - 1), 2)}')
    result.append(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
    result.append(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
    return result

# establish read and write paths
csvpath = "/Users/ronaldlam/Desktop/University_of_Toronto_2022:23/01-Data-Bootcamp/01-Weekly-Notes/03-Week-3-Python/module-3-challange/PyBank/Resources/budget_data.csv"
outputpath = "/Users/ronaldlam/Desktop/University_of_Toronto_2022:23/01-Data-Bootcamp/01-Weekly-Notes/03-Week-3-Python/module-3-challange/PyBank/analysis/results.txt"

# print results
analysis = budget_analysis(csvpath)
print("\n".join(analysis))

# create text file and write results
with open(outputpath, 'w') as file:
    file.write("\n".join(analysis))
