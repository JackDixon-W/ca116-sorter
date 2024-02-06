#!/usr/bin/env python3

# Week_IDs.txt

import os
import sys

dest = os.getcwd()

if len(sys.argv) >= 2:
  if "-s" in sys.argv:
    sys.stdout = open(os.devnull, 'w')

with open("Week_IDs.txt") as file:
  wList = file.read().split("\n")

for week in wList:
  curweek = week.split(" ")
  if len(sys.argv) >= 2:
    for ID in curweek:
      try:
        if sys.argv[1] == "-d":
          todelete = dest + "/" + ID
          print(f'Deleting file {todelete}')
          os.remove(todelete)
      except FileNotFoundError:
        print(f'Skipping {ID}, file not found')
      except IsADirectoryError:
        print(f'Skipping {ID}, is a directory')
  else:
    for ID in curweek:
      try:
        tocreate = dest + "/" + ID
        print(f'Creating file {tocreate}')
        newfile = open(tocreate, 'x')
      except:
        print(f'File {ID} already exists, skipping...')

