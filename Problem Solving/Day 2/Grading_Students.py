# /*** 
# CHALLENGE:
# HackerLand University has the following grading policy:
#   a. Every student receives a grade in the inclusive range from 0 to 100.
#   b. Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
#   a.If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#   b. If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

# Function Description:
# Complete the function gradingStudents in the editor below.
# gradingStudents has the following parameter(s):
#   int grades[n]: the grades before rounding

# Returns:
# int[n]: the grades after rounding as appropriate

# Input Format:
# The first line contains a single integer, n, the number of students.
# Each line i of the n subsequent lines contains a single integer, grades[i].
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if(grades[i]>37):
            if((grades[i]%5)!=0):
                if(5-(grades[i]%5)<3):
                    grades[i]+=5-(grades[i]%5)
    return (grades)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



