# /***
# CHALLENGE:
# A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with.
# Consider a positive whole number n with d digits. 
# We square  to arrive at a number that is either 2*d digits long or (2*d)-1 digits long. Split the string representation of the square into two parts,  and . 
# The right hand part, r must be d digits long. The left is the remaining substring. 
# Convert those two substrings back to integers, add them and see if you get n.

# Function Description:
# Complete the kaprekarNumbers function in the editor below.
# kaprekarNumbers has the following parameter(s):
#   int p: the lower limit
#   int q: the upper limit
  
# Prints:
# It should print the list of modified Kaprekar numbers, space-separated on one line and in ascending order. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE. No return value is required.

# Input Format:
# The first line contains the lower integer limit p.
# The second line contains the upper integer limit q.

# Note: Your range should be inclusive of the limits.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar_nums = []
    
    for n in range(p, q+1):
        d = len(str(n))
        n_squared = int(math.pow(n, 2))
        n_squared_str = str(n_squared)
        if len(n_squared_str) >= 2:
            l = int(n_squared_str[:d-1]) if len(n_squared_str) % 2 == 1 else int(n_squared_str[:d])
            r = int(n_squared_str[d-1:]) if len(n_squared_str) % 2 == 1 else int(n_squared_str[d:])
        if n == 1 or (n > 3 and l + r == n):
            kaprekar_nums.append(str(n))
    
    if len(kaprekar_nums) >= 1:
        print(' '.join(kaprekar_nums))
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)


