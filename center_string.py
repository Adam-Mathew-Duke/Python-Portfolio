'''
Name:           center_string.py
Description:    Center a string in the terminal window
Usage:          Takes one command line argument (no spaces)
Version:        1
'''

import os
import sys

# get a command line argument from the terminal
# if no arguments then the string is set to "Middle"
try:
    input_string = sys.argv[1]    
except:
    input_string = "Middle"

# get the terminal window rows and columns
terminal_size = os.get_terminal_size()
terminal_width = terminal_size.columns
terminal_height = terminal_size.lines

# If the input string is longer than the terminal width
if terminal_width < len(input_string):
    input_string = "*** Error: String is too long ***"

# find the center of the terminal window
column_middle = terminal_width//2
row_middle = terminal_height//2

# Center the input string
string_middle = len(input_string)//2
column_middle = column_middle - string_middle

# clear the terminal window
os.system('cls||clear')

# insert the row spacing
for row_index in range(row_middle):
    print(" ")

# insert the column spacing
for column_index in range(column_middle):
    print(" ", end='')

# print out the input_string in the center of the terminal window
print(input_string, end='')

# press anykey to continue
input()

# end of code
