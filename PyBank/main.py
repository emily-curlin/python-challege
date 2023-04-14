import os 
import csv

#Define Variables
monthly_change= 0
average_profit_or_loss= 0
greatest_increase_month= ""
greatest_increase_amount= 0
greatest_decrease_month= ""
greatest_decrease_amount= 0
revenue_change_list = []

csvpath = os.path.join ('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    first_row=next(csvreader)
    previoustotal=int(first_row[1])
    net_total_profit_or_loss=int(first_row[1])
    total_months=1

    def unique(candidates): 
        unique_list= [candidates_list]
        print(candidates_list)
        
    # Read each row of data after the header
    for row in csvreader:

        #The total number of months included in the dataset
        total_months= total_months + 1
       

        #The net total amount of "Profit/Losses" over the entire period
        net_total_profit_or_loss= net_total_profit_or_loss + int(row [1])

  
        #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        monthly_change= int(row[1]) - previoustotal
        previoustotal= int(row[1])
        revenue_change_list.append(monthly_change)


        #The greatest increase in profits (date and amount) over the entire period
        if greatest_increase_amount < monthly_change:
            greatest_increase_amount = monthly_change
            greatest_increase_month = row[0]

        #The greatest decrease in profits (date and amount) over the entire period
        if greatest_decrease_amount > monthly_change:
            greatest_decrease_amount = monthly_change
            greatest_decrease_month = row[0]    

#Revenue averge is calculated outside for loop    
revenue_average = sum(revenue_change_list)/len(revenue_change_list)

#Print Table

print ("Financial Analysis")

print ("-------------------------")

print (f"Total Months: {int(total_months)}")

print (f"Total: $ {int(net_total_profit_or_loss)}")

print (f"Average Change: $ {revenue_average:.2f}")

print (f"Greatest Increase in Profits: {greatest_increase_month} $ {greatest_increase_amount}")

print (f"Greatest Decrease in Profits: {greatest_decrease_month} $ {greatest_decrease_amount}")







