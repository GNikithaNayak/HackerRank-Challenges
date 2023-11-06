# /***
# CHALLENGE:
# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
#   If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0.
#   If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 Hackos * (the number of days late).
#   If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 Hackos * (the number of months late).
#   If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.
# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10,000 Hackos.

# Function Description:
# Complete the libraryFine function in the editor below.
# libraryFine has the following parameter(s):
#   d1, m1, y1: returned date day, month and year, each an integer
#   d2, m2, y2: due date day, month and year, each an integer

# Returns:
# int: the amount of the fine or 0 if there is none

# Input Format:
# The first line contains 3 space-separated integers, d1,m1,y1, denoting the respective day,month, and year on which the book was returned.
# The second line contains 3 space-separated integers, d2,m2,y2, denoting the respective day,month, and year on which the book was due to be returned.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if (d2>=d1 and m2>=m1 and y2>=y1) or (m2>m1 and y2>=y1) or (y2>y1):
        fine=0
    elif d2<d1 and m2==m1 and y2>=y1:
        fine=15*abs(d2-d1)
    elif m2<m1 and y2==y1:
        fine=500*abs(m2-m1)
    else:
        fine=10000
    return fine

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()



