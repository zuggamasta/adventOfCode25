# Advent of Code 2025
# @zuggamasta

import time
import os

my_map = []
new_map = []

FILE = "day04"

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
  
    global my_map
    result = 0

    # convert data
    for line in data:
      my_map.append(list(line))
      new_map.append(list(line))
    
    for y,line in enumerate(my_map):
      roll_count = 0

      for x, pos in enumerate(line):
        neighbors = []          
        if y>0 and x>0:
            neighbors.append(my_map[y-1][x-1]) # top left

        if x>0:
            neighbors.append(my_map[y ][x-1]) # left
    
        if y<len(my_map)-1 and x > 0:
            neighbors.append(my_map[y+1][x-1]) # bottom left

        if y<len(my_map)-1:
            neighbors.append(my_map[y+1][x ]) # bottom

        if y<len(my_map)-1 and x<len(line)-1:
            neighbors.append(my_map[y+1][x+1]) # bottom right

        if x<len(line)-1:
            neighbors.append(my_map[y ][x+1]) # right

        if y>0 and x<len(line)-1:
            neighbors.append(my_map[y-1][x+1]) # right top

        if y>0 :
            neighbors.append(my_map[y-1][x ]) # top


        intermediate = ''.join(neighbors)
        roll_count = intermediate.count('@')
        if roll_count < 4 and my_map[y][x] == '@':
            new_map[y][x] = 'x'
            result += 1

    print_map(new_map)
    return(result)

def print_map(map):

  os.system('clear')
  i = 0
  for line in map:
    i+=1
    if i == 40:
      return
    for pos in line:
      print(pos,end='')
    print()
  time.sleep(0.05)


load_state(FILE)