# /***
# CHALLENGE:
# John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.
# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

# Function Description:
# Complete the circularArrayRotation function in the editor below.
# circularArrayRotation has the following parameter(s):
#   int a[n]: the array to rotate
#   int k: the rotation count
#   int queries[1]: the indices to report

# Returns:
# int[q]: the values in the rotated a as requested in m

# Input Format:
# The first line contains 3 space-separated integers,n,k, and q, the number of elements in the integer array, the rotation count and the number of queries.
# The second line contains n space-separated integers, where each integer i describes array element a[i] (where 0<=i<n).
# Each of the q subsequent lines contains a single integer, queries[i] , an index of an element in a to return.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    x = k % len(a)
    a = a[-x:] + a[:-x]
    res = []
    for q in queries:
        res.append(a[q])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
