# /***
# CHALLENGE:
# You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

# Function Description:
# Complete the queensAttack function in the editor below.
# queensAttack has the following parameters:
# - int n: the number of rows and columns in the board
# - nt k: the number of obstacles on the board
# - int r_q: the row number of the queen's position
# - int c_q: the column number of the queen's position
# - int obstacles[k][2]: each element is an array of 2 integers, the row and column of an obstacle

# Returns:
# - int: the number of squares the queen can attack

# Input Format:

# The first line contains two space-separated integers n and k, the length of the board's sides and the number of obstacles.
# The next line contains two space-separated integers rq and cq, the queen's row and column position.
# Each of the next k lines contains two space-separated integers r[i] and c[i], the row and column position of obstacle[i].
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    if n==0:
        return 0
    vset=set([tuple(item) for item in obstacles])
    if (r_q,c_q) in vset:
        return 0
    directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count=0
    for u,v in directions:
        cur=(r_q+u,c_q+v)
        while 1<=cur[0]<=n and 1<=cur[1]<=n and cur not in vset:
            cur=(cur[0]+u,cur[1]+v)
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
