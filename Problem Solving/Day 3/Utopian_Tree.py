# /***
# CHALLENGE:
# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

# Function Description:
# Complete the utopianTree function in the editor below.
# utopianTree has the following parameter(s):
# int n: the number of growth cycles to simulate

# Returns:
# int: the height of the tree after the given number of cycles

# Input Format:
# The first line contains an integer,t, the number of test cases.
# t subsequent lines each contain an integer, n, the number of cycles for that test case.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    boolean = False
    count=0
    for i in range(n+1):
        if(boolean == False):
            count+=1
            boolean = True
        else:
            count*=2
            boolean=False
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

                                                                   
