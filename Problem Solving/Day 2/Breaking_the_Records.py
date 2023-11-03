# /*** 
# CHALLENGE:
# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.
# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

# Function Description:
# Complete the breakingRecords function in the editor below.
# breakingRecords has the following parameter(s):
#   int scores[n]: points scored per game
                                                                                     
# Returns:
# int[2]: An array with the numbers of times she broke her records.
# Index 0 is for breaking most points records, and index 1 is for breaking least points records.

# Input Format

# The first line contains an integer n, the number of games.
# The second line contains n space-separated integers describing the respective values of score0, score1,..., scoren-1.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxi=scores[0]
    mini=scores[0]
    maxcount =0
    mincount=0
    for i in range(len(scores)):
        if(scores[i]>maxi):
            maxi = scores[i]
            maxcount+=1
        if(scores[i]<mini):
            mini = scores[i]
            mincount+=1
    return [maxcount, mincount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

                                                                                     
