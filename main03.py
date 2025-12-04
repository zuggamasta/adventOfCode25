# Advent of Code 2024
# @zuggamasta

import time
import os


FILE = "example03"

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
      sorted_line = ''.join(sorted(line,reverse=True))
      result += int(sorted_line[:2])
      
    return(result)


load_state(FILE)