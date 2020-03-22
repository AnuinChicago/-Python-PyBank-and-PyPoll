import os
import csv

# Path to collect data from the Resources folder
PyBank_csv = os.path.join('', 'Resources', 'budget_data.csv')

#variables
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
    for row in csvreader:
        Total_months.append(row[0])
        Profit_Loss2.append(float(row[1]))

    # Calculate the total number of months included in the dataset  
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total Months: {len(Total_months)}')

    #Calculate the net total amt of Profit/Losses over the entire period
    Sum =sum(Profit_Loss2)
    print(f'Total: ${Sum}') 

    #Calculate the average of the changes in Profit/Loss over the entire period   
    for i in range(1,len(Profit_Loss2)):
        change_profit_loss.append(Profit_Loss2[i] - Profit_Loss2[i-1])
        average_change = sum(change_profit_loss)/len(change_profit_loss)
        
    print(f'Average Change:${round(average_change,2)}')
        #average= diff/2 
        #print(f'{change_profit_loss}{average}')
