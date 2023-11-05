# /***
# CHALLENGE:
# Given a sequence of n integers, p(1),p(2),...,p(n) where each element is distinct and satisfies 1<=p(x)<=n. 
# For each x where 1<=x<=n, that is x increments from 1 to n, find any integer y such that p(p(y)) = x and keep a history of the values of y in a return array.

# Function Description:
# Complete the permutationEquation function in the editor below.
# permutationEquation has the following parameter(s):
# int p[n]: an array of integers

# Returns:
# int[n]: the values of y for all x in the arithmetic sequence 1 to n

# Input Format:
# The first line contains an integer n, the number of elements in the sequence.
# The second line contains n space-separated integers p[i] where 1<=i<=n.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    output = []
    
    for num in range(1, max(p)+1):
        output.append(p.index(p.index(num)+1)+1)
        
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
