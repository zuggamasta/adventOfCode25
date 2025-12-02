# Advent of Code 2024
# @zuggamasta

import time
import os


FILE = "example02"

def load_state(file):
  try:
    with open(file, "r") as fp:
      data = fp.read().split(',')
      print(solve_puzzle(data))
  except:
    with open(file, "r") as fp:
      data = fp.read().split(',')
      print(solve_puzzle(data))
    print("Mission crashed. Please try again.")


def solve_puzzle(data):
  
    invalid = 0
    
    # convert data
    for line in data:
        # print(line)
        new_line = [int(line.split('-')[0]),int(line.split('-')[1])]
        
        for id in range(new_line[0],new_line[1]):
            number = str(id)
            length = len(number)
            if length % 2 == 0:
                length = int(length/2)
                for i, pair in enumerate(range(length)):
                  # I need to slice the right way here
                  # AB
                  # AABB
                  # AAABBB lenght/2 
                  # AABBCC length/3
                  # print (str(i) + "  <- " +number[:length] + "---" + number[length:])
                  if number[:length] == number[length:]:
                    # print("invalid: " + number)
                    invalid += int(number)

    return(invalid)

def solve_part_one(data):
  
    invalid = 0
    
    # convert data
    for line in data:
        # print(line)
        new_line = [int(line.split('-')[0]),int(line.split('-')[1])]
        
        for id in range(new_line[0],new_line[1]):
            number = str(id)
            length = len(number)
            if length % 2 == 0:
                length = int(length/2)
                # print (number[:length] + "---" + number[length:])
                if number[:length] == number[length:]:
                   # print("invalid: " + number)
                   invalid += int(number)

    return(invalid)



load_state(FILE)