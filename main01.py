# Advent of Code 2024
# @zuggamasta

import time
import os


FILE = "day01"

def load_state(file):
  try:
    with open(file, "r") as fp:
      data = fp.read().split('\n')
      print(solve_puzzle(data))
  except:
    with open(file, "r") as fp:
      data = fp.read().split('\n')
      print(solve_puzzle(data))
    print("Mission crashed. Please try again.")


def solve_puzzle(data):
  
    position = 50
    counter = 0
    
    # convert data
    for line in data:
        if line[0] == "R":
            for i in range(int(line[1:])):
                position+=1
                if position > 99:
                    position -= 100
                if position == 0:
                    counter +=1
        else:
            for i in range(int(line[1:])):
                position-=1
                if position == 0:
                    counter +=1
                if position < 0:
                    position += 100
    return(counter)


def partOne(data):
  
    position = 50
    counter = 0

    print(position)

    # convert data
    for line in data:
        if line[0] == "R":

            for i in range(int(line[1:])):
               position+=1
               if position > 99:
                  position -= 100
        else:
            for i in range(int(line[1:])):
               position-=1
               if position < 0:
                  position += 100
           

        print(position)

        if position == 0:
            counter +=1

    return(counter)

load_state(FILE)