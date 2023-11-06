# /***
# CHALLENGE:
# Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.

# Function Description:
# Complete the equalizeArray function in the editor below.
# equalizeArray has the following parameter(s):
# int arr[n]: an array of integers
  
# Returns:
# int: the minimum number of deletions required

# Input Format:
# The first line contains an integer n, the number of elements in arr.
# The next line contains n space-separated integers arr[i].
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    cnt = Counter(arr)
    count = 0
    for i, v in cnt.most_common()[1:]:
        count += v
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


