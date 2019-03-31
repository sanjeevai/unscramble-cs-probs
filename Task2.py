"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
max_duration = max([int(record[-1]) for record in calls])
# max_duration = max(durations)
# print(durations)
for i, v in enumerate(calls):
    if int(v[-1]) == max_duration:
        print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(v[0], v[-1]))