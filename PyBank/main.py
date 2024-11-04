# import modules
import csv
import os

# load in csv file
fileLoad = os.path.join("Resources/budget_data.csv")

# file to hold the output of the budget data
outputFile = os.path.join("Analysis/budget_data.txt")

# variables
totalMonths = 0                 # initialize total months to 0
totalProfitLosses = 0           # initialize total profit losses to 0
monthlyChanges = []             # initialize the list of monthly changes
months = []                     # initializa the list of months




# read the csv file
with open(fileLoad) as budgetData:
    # csv reader
    csvreader = csv.reader(budgetData)

    # read the header row
    header = next(csvreader)

    # move to the first row
    firstRow = next(csvreader)


    totalMonths += 1 # count of total months
    totalProfitLosses += float(firstRow[1])  # add the total profit/losses

    # establish what the previous profit/loss 
    previousProfitLoss = float(firstRow[1])
    
    # create a loop

    for row in csvreader:
        totalMonths += 1                                # count of total months
        totalProfitLosses += float(row[1])              # add the total profit/losses
        netChange = float(row[1]) - previousProfitLoss  # calculate the net changes
        monthlyChanges.append(netChange)                # add on to the list of monthly changes
        previousProfitLoss = float(row[1])              # update the previous profit loss
        months.append(row[0])                           # add the first month that a change occured, month is index 0

# Calculate the average net change per month
averageChangePerMonth = sum(monthlyChanges) / len(monthlyChanges)

# more variables
greatestIncrease = [months[0], monthlyChanges[0]]      # holds the month and the value of the greatest increase
greatestDecrease = [months[0], monthlyChanges[0]]      # holds the month and the value of the greatest decrease

# use loop to calculate the greatest increase/decrease of profit/losses
for m in range(len(monthlyChanges)):
    if (monthlyChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChanges[m]         # if the value is greater than the greatest increase, this value becomes the new greatest increase
        greatestIncrease[0] = months[m]                 # update the month

    if (monthlyChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChanges[m]         # if the value is less than the greatest decrease, this value becomes the new greatest decrease
        greatestDecrease[0] = months[m]                 # update the month



# start generating the output
output = (
    f"\nBudget Data Analysis \n"
    f"-----------------------------\n"
    f"\tTotal Months = {totalMonths}\n"
    f"\tTotal Profits and Losses = ${totalProfitLosses:,.2f}\n"
    f"\tAverage Change Per Month = ${averageChangePerMonth:,.2f}\n"
    f"\tGreatest Increase = {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f}\n"
    f"\tGreatest Decrease = {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f}\n"
    )

# print the output to the console / terminal
print(output)

#export the output variable to the txt file
with open(outputFile, "w") as textFile:
    textFile.write(output)

