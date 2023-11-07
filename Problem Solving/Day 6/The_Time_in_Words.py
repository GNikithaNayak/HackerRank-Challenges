# /***
# CHALLENGE:
# Given the time in numerals we may convert it into words.
# At minutes = 0, use o' clock. For 1 <= minutes <= 30, use past, and for 3- < minutes use to. Note the space between the apostrophe and clock in o' clock. 
# Write a program which prints the time in words for the input given in the format described.

# Function Description:
# Complete the timeInWords function in the editor below.
# timeInWords has the following parameter(s):
#   int h: the hour of the day
#   int m: the minutes after the hour
  
# Returns:
# string: a time string as described

# Input Format:
# The first line contains h, the hours portion.
# The second line contains m, the minutes portion.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

desc_hour = {
    1:"one", 
    2:"two", 
    3:"three", 
    4:"four", 
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
}

desc_minute = {
    1:"one minute", 
    2:"two minutes", 
    3:"three minutes", 
    4:"four minutes", 
    5:"five minutes",
    6:"six minutes",
    7:"seven minutes",
    8:"eight minutes",
    9:"nine minutes",
    10:"ten minutes",
    11:"eleven minutes",
    12:"twelve minutes",
    13:"thirteen minutes",
    14:"fourteen minutes",
    15:"fifteen minutes",
    16:"sixteen minutes",
    17:"seventeen minutes",
    18:"eighteen minutes",
    19:"nineteen minutes",
    20:"twenty minutes",
    21:"twenty one minutes",
    22:"twenty two minutes",
    23:"twenty three minutes",
    24:"twenty four minutes",
    25:"twenty five minutes",
    26:"twenty six minutes",
    27:"twenty seven minutes",
    28:"twenty eight minutes",
    29:"twenty nine minutes",
}

quarters = {
    0:"o' clock",
    15:"quarter",
    30:"half",
    45:"quarter"
}

def timeInWords(h, m):
    hour_in_min = 60
    if m == 0:
        desc = "{} {}".format(desc_hour[h], quarters[m])
    elif (m > 0 and m < 15) or (m > 15 and m < 30):
        desc = "{} past {}".format(desc_minute[m], desc_hour[h])
    elif m == 15:
        desc = "{} past {}".format(quarters[m], desc_hour[h])
    elif m == 30:
        desc = "{} past {}".format(quarters[m], desc_hour[h])
    elif (m > 30 and m < 45) or (m > 45 and m < 60):
        desc = "{} to {}".format(desc_minute[hour_in_min - m], desc_hour[h + 1])
    elif m == 45:
        desc = "{} to {}".format(quarters[m], desc_hour[h + 1])
    return desc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()


