# Data Structures and Algorithms Nanodegree

## Project: Unscramble Computer Science Problems

## Project Overview

In this project, I will complete five tasks based on a fabricated set of calls
and texts exchanged during September 2016. I will use Python to analyze and
answer questions about the texts and calls contained in the data set. Lastly, I
will perform run time analysis of my solution and determine its efficiency.

Deconstruct a series of open-ended problems into smaller components (e.g.,
inputs, outputs, series of functions)

## Motivation

Refresher of the following topics:

- Applying Python knowledge to breakdown problems into their inputs and outputs
- Perform an efficiency analysis
- Warm up Python skills for upcoming projects

## About the data

The text and call data re provided in CSV files. In each file, the data is
already read and stored as lists of lists.

Each sub-list of the list of texts is structured in this way:
<pre>
<code>
a <span class="hljs-type">text</span> = [    Sending telephone <span class="hljs-type">number</span> (<span class="hljs-type">string</span>),
        receiving telephone <span class="hljs-type">number</span> (<span class="hljs-type">string</span>), 
        timestamp <span class="hljs-keyword">of</span> <span class="hljs-type">text</span> message (<span class="hljs-type">string</span>)]
</code>
</pre>

Each element in the list of phone calls is structured in this way:

<pre><code>a <span class="hljs-operator"><span class="hljs-keyword">call</span> = [    <span class="hljs-keyword">Calling</span> telephone <span class="hljs-built_in">number</span> (<span class="hljs-keyword">string</span>), 
        receiving telephone <span class="hljs-built_in">number</span> (<span class="hljs-keyword">string</span>), 
        <span class="hljs-keyword">start</span> <span class="hljs-keyword">timestamp</span> <span class="hljs-keyword">of</span> telephone <span class="hljs-keyword">call</span> (<span class="hljs-keyword">string</span>),
        <span class="hljs-keyword">duration</span> <span class="hljs-keyword">of</span> telephone <span class="hljs-keyword">call</span> <span class="hljs-keyword">in</span> seconds (<span class="hljs-keyword">string</span>)]</span>
</code></pre>

All telephone numbers are 10 numerical digits long. Each telephone number starts
with a code indicating the location and/or type of the telephone number. There
are three different kinds of telephone numbers, each with a different format:

- Fixed lines start with an area code enclosed in brackets. The area codes vary
  in length but always begin with 0. Example: `(022)40840621`.
- Mobile numbers have no parentheses, but have a space in the middle of the
  number to help readability. The mobile code of a mobile number is its first
  four digits and they always start with 7, 8 or 9. Example: `93412 66159`.
- Telemarketers' numbers have no parentheses or space, but start with the code
  140. Example: `1402316533`.

## Files

.
├── Analysis.txt
├── Task0.py---Display the first record of texts and the last record of calls?
├── Task1.py---Calculate different telephone numbers present in the records?
├── Task2.py---Find which telephone number spent the longest time on the phone.
├── Task3.py---Find all of the area codes and mobile prefixes called by people
|              in Bangalore.
├── Task4.py---Identify telemarketer based on their calling and texting behavior.
├── calls.csv--#UNTRACKED. calls data
└── texts.csv--#UNTRACKED. texts data

## Software Requirements

This project uses Python 3.6.8.