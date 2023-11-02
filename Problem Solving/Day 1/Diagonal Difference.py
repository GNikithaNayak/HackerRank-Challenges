# /***
# CHALLENGE:
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# Function description:
# Complete the 'diagonalDifference' function in the editor below.
# diagonalDifference takes the following parameter:
#   int arr[n][m]: an array of integers

# Return:
# int: the absolute diagonal difference

# Input Format:
# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Output Format:
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    prim =0
    sec=0
    length = len(arr[0])
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length-count-1)]
    return abs(prim-sec)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
