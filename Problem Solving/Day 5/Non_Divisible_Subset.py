# /***
# CHALLENGE:
# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.

# Function Description:
# Complete the nonDivisibleSubset function in the editor below.
# nonDivisibleSubset has the following parameter(s):
#   int S[n]: an array of integers
#   int k: the divisor

# Returns:
# int: the length of the longest subset of S meeting the criteria

# Input Format:
# The first line contains 2 space-separated integers, n and kk, the number of values in S and the non factor.
# The second line contains n space-separated integers, each an S[i], the unique values of the set.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    x = [0 for _ in range(k)]
    for ss in s:
        x[ss % k] += 1
    res = min(1, x[0])
    x = x[1:]
    for i in range(len(x) // 2):
        res += max(x[i], x[-(i+1)])
    if len(x) % 2 == 1:
        res += min(1, x[len(x) // 2])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
