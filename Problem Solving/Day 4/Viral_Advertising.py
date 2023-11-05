# /***
# CHALLENGE:
# HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.

# Function Description:
# Complete the viralAdvertising function in the editor below.
# viralAdvertising has the following parameter(s):
# int n: the day number to report

# Returns:
# int: the cumulative likes at that day

# Input Format:
# A single integer, n, the day number.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared =5
    cumulative=0
    for i in range(1,n+1):
        liked = shared//2
        cumulative+=liked
        shared = liked*3
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
