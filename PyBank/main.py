import csv
import os

row_count = 0
net_total = []
months = []
numbers = list(range(1,87))
changes = []

with open("/Users/brendangold/DENVDEN201905DATA4/Homework/3 Python  6-18/PyBank/Resources/budget_data.csv", "r") as f:
    reader = csv.reader(f)

    next (reader)

    for row in reader:
        net_total.append(int(row[1]))
        months.append(row[0])
        row_count += 1

    numbered_net_total = dict(zip(numbers, net_total))
    numbered_months = dict(zip(numbers, months))

    

    #print(numbered_net_total)
    #print(numbered_months)
    count = 0
   
    for x in net_total:
        if count + 1 > (len(net_total) -1):
            break
        else:
            changes.append(net_total[count + 1] - x)
            count += 1

    average_changes = (sum(changes) / len(changes))
    change_length = list(range(1, len(changes)))
    numbered_changes = dict(zip(change_length, changes))
    profit_increase = (list(numbered_changes.keys())[list(numbered_changes.values()).index(max(changes))]) + 1

    

    profit_decrease = (list(numbered_changes.keys())[list(numbered_changes.values()).index(min(changes))]) + 1

    print(f"Total Months: {row_count}")
    print(f"Total: ${sum(net_total)}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in profits {numbered_months.get(profit_increase)}, ${numbered_changes.get(profit_increase -1)}")
    print(f"Greatest Decrease in Profits {numbered_months.get(profit_decrease)}, ${numbered_changes.get(profit_decrease-1)}")
  