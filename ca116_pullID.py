#!/usr/bin/env python3

import os

# Directory of ca116
cadir = "/home/womble/comsci/comsci1/ca116"

for weeknum in range(1, 11):
  curdir = cadir + "/W" + str(weeknum) + "/"
  temp = os.listdir(curdir)
  file = open("Week_IDs.txt", "a")
  for task in temp:
    if ".py" in task:
      file.write(task + " ")
    else:
      print(f'Skipping {task}')
  file.write("\n")
  file.close()
