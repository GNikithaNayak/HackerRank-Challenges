# /***
# CHALLENGE:
# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (arrivalTime<=0) to arrived late (arrivalTime>0).
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.

# Note: Non-positive arrival times (a[i]<=0) indicate the student arrived early or on time; positive arrival times (a[i]>0) indicate the student arrived a[i] minutes late.

# Function Description:
# Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.
# angryProfessor has the following parameter(s):
#   int k: the threshold number of students
#   int a[n]: the arrival times of the n students
  
# Returns:
# string: either YES or NO
  
# Input Format:
# The first line of input contains t, the number of test cases.
# Each test case consists of two lines.

# The first line has two space-separated integers, n and k, the number of students (size of a) and the cancellation threshold.
# The second line contains n space-separated integers (a[1],a[2],...,a[n]) that describe the arrival times for each student.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    return "YES" if sum(x <= 0 for x in a) < k else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
