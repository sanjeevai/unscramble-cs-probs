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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# SOLUTION
call_initiators = [record[0] for record in calls]
call_receivers  = [record[1] for record in calls]
text_senders    = [record[0] for record in texts] 
text_receivers  = [record[1] for record in texts]

print("These numbers could be telemarketers: ")
for number in sorted(list(set(call_initiators))):
    if number not in call_receivers + text_senders + text_receivers:
        print(number)