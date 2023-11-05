# /***
# CHALLENGE:
# You have two strings of lowercase English letters. You can perform two types of operations on the first string:
#   Append a lowercase English letter to the end of the string.
#   Delete the last character of the string. Performing this operation on an empty string results in an empty string.
# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s.
# If it's possible, print Yes. Otherwise, print No.

# Function Description:
# Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.
# appendAndDelete has the following parameter(s):
#   string s: the initial string
#   string t: the desired string
#   int k: the exact number of operations that must be performed

# Returns:
# string: either Yes or No

# Input Format:
# The first line contains a string s, the initial string.
# The second line contains a string t, the desired final string.
# The third line contains an integer k, the number of operations.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    i = 0
    while i < min(len(s), len(t)) and s[i] == t[i]:
        i += 1
    x = len(s) + len(t) - (2 * i)
    if x <= k and ((k - x) % 2 == 0 or (len(s) + len(t)) <= k):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
