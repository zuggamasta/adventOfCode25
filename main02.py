# Advent of Code 2024
# @zuggamasta

import time
import os


FILE = "day02"

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
  
    reverse_text = "helloWorld"
    print(reverse_text[::-1])

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
                   print("invalid: " + number)
                   invalid += int(number)

    return(invalid)


load_state(FILE)