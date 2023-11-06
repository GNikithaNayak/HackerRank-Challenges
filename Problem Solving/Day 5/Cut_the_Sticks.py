# /***
# CHALLENGE:
# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.
# Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.

# Function Description:
# Complete the cutTheSticks function in the editor below. It should return an array of integers representing the number of sticks before each cut operation is performed.
# cutTheSticks has the following parameter(s):
# int arr[n]: the lengths of each stick

# Returns:
# int[]: the number of sticks after each iteration

# Input Format:
# The first line contains a single integer n, the size of arr.
# The next line contains n space-separated integers, each an arr[i], where each value represents the length of the ith stick.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import defaultdict
def cutTheSticks(arr):
    # Write your code here
    d = defaultdict(int)
    for a in arr:
        d[a] += 1
    d = sorted(list(d.items()))
    res = [len(arr)]
    for _, n in d[:-1]:
        res.append(res[-1] - n)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

