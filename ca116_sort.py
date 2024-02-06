#!/usr/bin/env python3

import shutil
import os
import sys

def createWeekDirs(src):
  print(f'Beginning to create week directories')
  for weeknum in range(1, 12):
    try:
      os.mkdir(src + "/W" + str(weeknum))
      print(f'Creating directory for Week {weeknum}')
    except FileExistsError:
      print(f'Week {weeknum} directory already exists')
    except FileNotFoundError:
      print("Parent directory not found, shutting down")
      sys.exit()
    except:
      print('Unknown error has occured, shutting down')
      sys.exit()
  print("Finished creating directories")

def removeWeekDirs(src):
  print(f'Are you sure you want to remove all week directories and their contents? y/n')
  match input():
    case "y":
      pass
    case "n":
      sys.exit()
  print(f'Beginning to remove week directories')
  for weeknum in range(1, 12):
    try:
      shutil.rmtree(src + "/W" + str(weeknum))
      print(f'Removed directory for week {weeknum}')
    except FileNotFoundError:
      print(f'Directory for week {weeknum} not found, Skipping...')
  print('Finished removing directories')
  sys.exit()

curdir = os.getcwd()

if len(sys.argv) >= 2:
  if "-s" in sys.argv:
    sys.stdout = open(os.devnull, 'w')
  if "-d" in sys.argv:
    createWeekDirs(curdir)
  if "-rm" in sys.argv:
    removeWeekDirs(curdir)

with open("Week_IDs.txt") as f:
  wList = f.read().split("\n")

# Create a loop that takes a new week in every loop
# Use curweek for the current week
# curweek will also be an array, taken by splitting the current week val
# Eg. curweek = wList[0].split(" ")
# Go through each file listed here and attempt to move them
# (Assume premade folders, can add that to script later if you want)
# Use a catch statement that prints what file is not present

weeknum = 0
for week in wList:
  curweek = week.split(" ")
  curdest = curdir + "/W" + str(weeknum + 1)
  for ID in curweek:
    if len(ID) <= 3:
      continue
    try:
      shutil.move(curdir + "/" + ID, curdest + "/" + ID)
    except FileNotFoundError:
      print(f'File {ID} not found. Task presumed unstarted')
  weeknum += 1 
