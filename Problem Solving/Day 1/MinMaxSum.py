# /***
# CHALLENGE:
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Function Description:
# Complete the miniMaxSum function in the editor below.
# miniMaxSum has the following parameter(s):
#   arr: an array of 5 integers

# Print:
# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format:
# A single line of five space-separated integers.

# Output Format:
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# (The output can be greater than a 32 bit integer.)
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print ( sum-max(arr), sum-min(arr)) 

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
