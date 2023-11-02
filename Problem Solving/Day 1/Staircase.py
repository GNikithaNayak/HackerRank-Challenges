# /***
# CHALLENGE:
# Write a program that prints a staircase of size n.

# Function Description:
# Complete the staircase function in the editor below.
# staircase has the following parameter(s):
#   int n: an integer

# Print:
# Print a staircase as described above.

# Input Format:
# A single integer ,n, denoting the size of the staircase.

# Output Format:
# Print a staircase of size n using # symbols and spaces.
# Note: The last line must have  spaces in it.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
