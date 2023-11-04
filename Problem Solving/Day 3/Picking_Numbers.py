# /***
# CHALLENGE:
# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

# Function Description:
# Complete the pickingNumbers function in the editor below.
# pickingNumbers has the following parameter(s):
# int a[n]: an array of integers

# Returns:
# int: the length of the longest subarray that meets the criterion

# Input Format:
# The first line contains a single integer n, the size of the array a.
# The second line contains n space-separated integers, each an a[i].
# ***/


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    occurrence_table = dict()
    longest_subarray_found = 0
    
    for integer in a:
        
        try:
            occurrence_table[integer] += 1
            
        except:
            occurrence_table[integer] = 1
            
    for integer in occurrence_table:
        
        try:
            current_subarray = occurrence_table[integer] + occurrence_table[integer+1]
            
        except:
            current_subarray = occurrence_table[integer]
            
        if current_subarray > longest_subarray_found:
            
            longest_subarray_found = current_subarray
            
    return longest_subarray_found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
