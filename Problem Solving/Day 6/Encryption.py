# /***
# CHALLENGE:
# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. 

# Function Description:
# Complete the encryption function in the editor below.
# encryption has the following parameter(s):
# string s: a string to encrypt

# Returns:
# string: the encrypted string

# Input Format:
# One line of text, the string s
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    num_rows = math.floor(math.sqrt(len(s)))
    num_columns = math.ceil(math.sqrt(len(s)))
    
    encoded = ''
    
    for c1 in range(num_columns):
        for c2 in range(num_columns):
            if c1 + c2 * num_columns >= len(s):
                break
            encoded += s[c1 + c2 * num_columns]
        encoded += ' '
    
    return encoded


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
