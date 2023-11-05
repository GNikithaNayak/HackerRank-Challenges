# /***
# CHALLENGE:
# An integer d is a divisor of an integer n if the remainder of n%d=0.
# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

# Function Description:
# Complete the findDigits function in the editor below.
# findDigits has the following parameter(s):
# int n: the value to analyze
  
# Returns:
# int: the number of digits in n that are divisors of n
  
# Input Format:
# The first line is an integer, t, the number of test cases.
# The t subsequent lines each contain an integer, n.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    return sum(n % int(c) == 0 for c in str(n) if c != "0")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
