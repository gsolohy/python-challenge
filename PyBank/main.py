import os
import csv

pathPyBank = os.path.join("Resources","budget_data.csv")

month_list = []
profit_list = []
profit_change = []
net_change = 0

with open(pathPyBank, newline='') as filePyBank:
    PyBank_reader = csv.reader(filePyBank, delimiter=',') # File read
    PyBank_header = next(PyBank_reader) # Header Row Skip

    for row in PyBank_reader:
        month_list.append(row[0]) # Convert to list to extract month for change & month count
        profit_list.append(row[1]) # Convert to list to calculate change
        net_change += int(row[1]) # Net. Complete.
        
    for i in range(1, len(profit_list)):
        profit_change.append(int(profit_list[i]) - int(profit_list[(i-1)]))
        avg_change = round(sum(profit_change)/len(profit_change),2) # Sum change / Num change
        max_increase = max(profit_change) # Greatest Increase
        max_decrease = min(profit_change) # Greatest Decrease
        
        max_inc_month = month_list[profit_change.index(max_increase)+1] # Skip First Month
        max_dec_month = month_list[profit_change.index(max_decrease)+1] # Match Month Offset

#print(len(month_list))
#print(net_change)
#print(avg_change)
#print(max_inc_month, end=' ')
#print(max_increase)
#print(max_dec_month, end=' ')
#print(max_decrease)
#CHECK

PyBank_export = 'Financial Analysis.txt' # Export as txt

with open(PyBank_export, 'w') as export_text:
    export_text.write("Financial Analysis\n")
    export_text.write("-"*30 + "\n")
    export_text.write(f"Total Months: {len(month_list)} \nTotal: ${net_change}\n")
    export_text.write(f"Average Change: ${avg_change}\n")
    export_text.write(f"Greatest Increase in Profits: {max_inc_month} (${max_increase})\n")
    export_text.write(f"Greatest Decrease in Profits: {max_dec_month} (${max_decrease})")