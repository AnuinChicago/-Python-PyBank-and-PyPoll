import os
import csv

# Path to collect data from the Resources folder
PyBank_csv = os.path.join('', 'Resources', 'budget_data.csv')

#variables and lists
Sum =0
diff=0
Profit_Loss2 =[]
change_profit_loss = []
Total_months =[]


# Read in the CSV file
with open(PyBank_csv, encoding ='utf-8') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Loop through the data
    # Calculate the total number of months included in the dataset 
    for row in csvreader:
        Total_months.append(row[0])
        Profit_Loss2.append(float(row[1]))
 
    
    #Calculate the average of the changes in Profit/Loss over the entire period 
    

    for i in range(1,len(Profit_Loss2)):
        change_profit_loss.append(Profit_Loss2[i] - Profit_Loss2[i-1])
        average_change = sum(change_profit_loss)/len(change_profit_loss)
        greatest_profit = max(change_profit_loss)
        greatest_loss = min(change_profit_loss)
        #if change_profit_loss[i] > max(change_profit_loss):
        #    max_month = Total_months[0]
    #if change_profit_loss < min(change_profit_loss):
        
      #  min_month =row[0]    
   
    #Calculate the net total amt of Profit/Losses over the entire period
    Sum =sum(Profit_Loss2)
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total Months: {len(Total_months)}')
    print(f'Total: ${Sum}') 
    print(f'Average Change:${round(average_change,2)}')
    
    #Calculate the greatest increase in profit
    print(f'Greatest increase in profit is ${greatest_profit}')

    #Calculate the greatest decrease in Profit
    print(f'Greatst decrease in profit is ${greatest_loss}')

# Set variable for output file
output_file = os.path.join("PyBank_final.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the rows
    writer.writerow(['Financial Analysis'])
    writer.writerow(['-----------------------'])
    writer.writerow([f'Total Months: {len(Total_months)}'])
    writer.writerow([f'Total: ${Sum}'])
    writer.writerow([f'Average Change:${round(average_change,2)}'])
    writer.writerow([f'Greatest increase in profit is ${greatest_profit}'])
    writer.writerow([f'Greatst decrease in profit is ${greatest_loss}'])