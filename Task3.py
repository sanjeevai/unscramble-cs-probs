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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Solution for Part A
codes = []
for record in calls: #n
  if (record[0][0] == "(") & (record[0][4] == ")") & (record[0][1:4] == '080'): # check if the dialer is from Bangalore
    number = record[1] # receiver number
    if ("(" in number) & (")" in number): # check for codes which have parentheses
      # now extract the code between the parentheses and add to `codes` list
      for i in range(len(number)):
        if number[i] == ")":
          code = number[1:i]
          codes.append(code) 
    elif len(number.split(" ")) == 2: # check for mobile number
      code = number[:4]
      codes.append(code)
    elif number[:3] == "140": # check for telemarketers
      codes.append("140")
    else:
      print("None of the code types present in this number: ", number)

# OUTPUT FOR PART A
print("The numbers called by people in Bangalore have codes:")
for code in sorted(list(set(codes))):
  print(code)

# OUTPUT FOR PART B
count = 0
for code in codes:
  if code == "080":
    count += 1
percentage = round(100 * count/len(codes), 2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))