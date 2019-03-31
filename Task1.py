"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
telephone_numbers = []
for record in texts:
    for telephone_number in record[:2]:
        if telephone_number not in telephone_numbers:
            telephone_numbers.append(telephone_number)

for record in calls:
    for telephone_number in record[:2]:
        if telephone_number not in telephone_numbers:
            telephone_numbers.append(telephone_number)

print("There are {0} different telephone numbers in the records.".format(len(telephone_numbers)))
