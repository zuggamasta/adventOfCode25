# Advent of Code 2025
# @zuggamasta

import time
import os


FILE = "day05"

def load_state(file):
  try:
    with open(file, "r") as fp:
      data = fp.read().split('\n\n')
      print(solve_puzzle(data))
  except:
    with open(file, "r") as fp:
      data = fp.read().split('\n\n')
      print(solve_puzzle(data))
    print("Mission crashed. Please try again.")


def solve_puzzle(data):
  
    ranges = data[0].split('\n')
    ids = data[1].split('\n')
    result = 0

    for id in ids:
      fresh = False
      for range in ranges:
        min_max = [int(range.split('-')[0]),int(range.split('-')[1])]
        if min_max[0] <= int(id) <= min_max[1]:
          fresh = True
        if fresh:
          result+=1
          break


    return(result)


load_state(FILE)