# Objective
# In this challenge, we review some basic concepts that will 
# get you started with this series. You will need to use the 
# same (or similar) syntax to read input and write output in challenges throughout HackerRank. 
# Check out the Tutorial tab for learning materials and an instructional video!

# Task
# To complete this challenge, you must save a line of input from stdin to a variable,
#  print Hello, World. on a single line, and finally print the value of your variable on a second line.

# You've got this!

# Note: The instructions are Java-based, but we support submissions in many popular languages.
#  You can switch languages using the drop-down menu above your editor, and the 
#   variable may be written differently depending on the best-practice conventions of your submission language.

# Input Format

# A single line of text denoting  (the variable whose contents must be printed).

# Output Format

# Print Hello, World. on the first line, and the contents of  on the second line.

# Sample Input

# Welcome to 30 Days of Code!
# Sample Output

# Hello, World. 
# Welcome to 30 Days of Code!




# Code implementation


# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)





# Second Day2 Challenge



import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip=int(round((meal_cost/float(100))*tip_percent))
    tax=int(round((meal_cost/float(100))*tax_percent))
    print(int(meal_cost)+tip+tax)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)