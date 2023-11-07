# /***
# CHALLENGE:
# The distance between two array values is the number of indices between them.
# Given a, find the minimum distance between any pair of equal elements in the array. 
# If no such value exists, return -1.

# Function Description:
# Complete the minimumDistances function in the editor below.
# minimumDistances has the following parameter(s):
# int a[n]: an array of integers

# Returns:
# int: the minimum distance found or -1 if there are no matching elements

# Input Format:
# The first line contains an integer n, the size of array a.
# The second line contains n space-separated integers a[i].
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    n=len(a)
    minimum=n+1         #Initializing with n+1 because if no updates take place we should return -1 as there are no matching pairs
    # Note:- If any matching pairs is found the distance would be less than n
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]==a[j]:
                if j-i<minimum:
                    minimum=j-i
    if minimum==n+1:
        return -1
    return minimum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

