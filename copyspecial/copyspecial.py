#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# LAB(begin solution)
def get_special_paths(dirname):
  # Code to find all file paths & store in a list
  global list1
  global list2
  list1 = []
  list2 = []
  
  path = os.listdir(dirname)
  for fname in path:
    match = re.search('\w+__\w+__\S+',fname)
    if match:
      list1.append(os.path.abspath(match.group()))
      list2.append(match.group())
  
# Write a code to copy files to given directory
#def copy_to_dir(destn):


  
def main():

  global list2
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:1]
    #copy_to_dir (todir)
    dirname = args[1]
    get_special_paths(dirname)
    os.makedirs(todir)
    for f in list2:
      shutil.copy('./'+f, todir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  dirname = args[0]
  get_special_paths(dirname)
  print list1, list2

  #copy_to_dir (todir)
  # +++your code here+++
  # Call your functions

  
if __name__ == "__main__":
  main()
