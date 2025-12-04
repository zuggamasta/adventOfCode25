# Advent of Code 2025
# @zuggamasta

import time
import os


FILE = "day03"

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
  
    result = 0
    
    # convert data
    for line in data:
      # find leftmost digit and it's position
      left = 0
      position = 0
      for i, number in enumerate(line):
        if i > len(line)-2:
          print("too_long")
        else:
          if int(number) > left:
            left = int(number)
            position = i
      # truncate string
      new_line = line[position+1:]
      
      # find largest digit in rest of the string
      right = 0
      for i, number in enumerate(new_line):
        if int(number) > right:
          right = int(number)
      
      intermediate = 10*left + right

      result += intermediate
      
    return(result)

load_state(FILE)