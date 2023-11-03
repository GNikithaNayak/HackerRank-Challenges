# /***
# CHALLENGE:
# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.
# Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])?

# Function Description:
# Complete the countApplesAndOranges function in the editor below. 
# It should print the number of apples and oranges that land on Sam's house, each on a separate line.
# countApplesAndOranges has the following parameter(s):
#   s: integer, starting point of Sam's house location.
#   t: integer, ending location of Sam's house location.
#   a: integer, location of the Apple tree.
#   b: integer, location of the Orange tree.
#   apples: integer array, distances at which each apple falls from the tree.
#   oranges: integer array, distances at which each orange falls from the tree.

# Input Format:
#   The first line contains two space-separated integers denoting the respective values of s and t.
#   The second line contains two space-separated integers denoting the respective values of a and b.
#   The third line contains two space-separated integers denoting the respective values of m and n.
#   The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
#   The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

# Output Format:
# Print two integers on two different lines:
#   The first integer: the number of apples that fall on Sam's house.
#   The second integer: the number of oranges that fall on Sam's house.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    acount = 0
    bcount = 0
    for i in range(len(apples)):
        temp = a+apples[i]
        if(temp in range(s,t+1)):
            acount+=1
    for i in range(len(oranges)):
        temp = b+oranges[i]
        if(temp in range(s,t+1)):
            bcount+=1
    print (acount)
    print (bcount)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
