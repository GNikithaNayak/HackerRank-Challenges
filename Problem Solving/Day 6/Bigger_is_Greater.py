# /***
# CHALLENGE:
# Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
#   It must be greater than the original word
#   It must be the smallest word that meets the first condition

# Function Description:
# Complete the biggerIsGreater function in the editor below.
# biggerIsGreater has the following parameter(s):
# string w: a word

# Returns:
# - string: the smallest lexicographically higher string possible or no answer

# Input Format:
# The first line of input contains T, the number of test cases.
# Each of the next T lines contains w.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    arr = list(w)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
    if i <= 0:
        return 'no answer'
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
       
    return "".join(arr)
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()


