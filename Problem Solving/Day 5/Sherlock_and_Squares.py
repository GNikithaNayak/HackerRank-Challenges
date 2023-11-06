# /***
# CHALLENGE:
# Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range.

# Function Description:
# Complete the squares function in the editor below. It should return an integer representing the number of square integers in the inclusive range from a to b.
# squares has the following parameter(s):
#   int a: the lower range boundary
#   int b: the upper range boundary

# Returns:
# int: the number of square integers in the range

# Input Format:
# The first line contains , the number of test cases.
# Each of the next q lines contains two space-separated integers, a and b, the starting and ending integers in the ranges.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
