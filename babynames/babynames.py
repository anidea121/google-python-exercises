#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
#import global

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
dict1 = {}
year = []
#f = None

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  global name
  global year
  global dict1

  #Finding year
  for line in filename:
    match = re.search('Popularity in \d\d\d\d', line)
    if match:
      list1 = re.search('\d\d\d\d', match.group())
      break
  year = list1.group()

  #Finding names and rank
  string2 = []
  string3 = []

  #Running through each line in a file 
  for line in filename:

    #Find all strings within <td>\w+</td>
    match1 = re.findall('<td>\w+</td>', line)

    #If match is found, carefully strip <td> from either ends and store in a list
    if match1:
      list2 = []
      for string in match1:
        #Instead of printing, store it in a dictionary - dict[name] = rank
        string2 = re.search('>\w+<',string)
        string3 = re.search('[a-zA-Z0-9]+',string2.group())
        list2.append(string3.group())

      #Store the items of list in dictionary - data structure.
      dict1[list2[1]] = list2[0]
      dict1[list2[2]] = list2[0]

  return dict1


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.


  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  print args[0:]

  #Reading baby/d/d/d/d.html and outputting baby/d/d/d/d.html.smmary.txt
  filename = open(args[0],'r')
  global name
  name = args[0]
  extract_names (filename)

  #Sort keys in dictionary before printing or outputting in order
  keys = dict1.keys()
  keys.sort()

  if summary:

    #Opening a file to write based on name defined in main function
    opname = name + '.' + 'summary.txt'
    f = open(opname, 'w')
    f.write(year + '\n')

    #Print in sorted order
    for key in keys:
      #print "%s %s" %(key, dict1[key])
      f.write("%s %s\n" %(key, dict1[key]))

  else:
    #print in stdout
    print year
    for key in keys:
      print "%s %s" %(key, dict1[key])

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
  main()
