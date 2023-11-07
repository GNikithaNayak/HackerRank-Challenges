# /***
# CHALLENGE:
# Given a sequence of integers a, a triplet (a[i],a[j],a[k]) is beautiful if:
#   i < j < k
#   a[j] - a[i] = a[k] - a[j] = d
# Given an increasing sequenc of integers and the value of d, count the number of beautiful triplets in the sequence.

# Function Description:
# Complete the beautifulTriplets function in the editor below.
# beautifulTriplets has the following parameters:
#   int d: the value to match
#   int arr[n]: the sequence, sorted ascending

# Returns:
# int: the number of beautiful triplets

# Input Format:
# The first line contains 2 space-separated integers, n and d, the length of the sequence and the beautiful difference.
# The second line contains n space-separated integers arr[i].
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    triplets = 0
    for i in arr:
        if i+d in arr and i+d*2 in arr:
            triplets += 1
    return triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()




