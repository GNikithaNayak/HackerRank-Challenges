/***
CHALLENGE:
We define a magic square to be an nxn matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

Function Description:
Complete the formingMagicSquare function in the editor below.
formingMagicSquare has the following parameter(s):
int s[3][3]: a 3x3 array of integers

Returns:
int: the minimal total cost of converting the input square to a magic square

Input Format:
Each of the 3 lines contains three space-separated integers of row s[i].
***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

    
def formingMagicSquare(s):
    # Write your code here
    # List of all possible 3x3 magic squares
    magic_squares = [
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 5, 4], [1, 5, 9], [8, 3, 2]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    ]
    
    min_cost = float('inf')
    
    # Check the cost for each magic square and find the minimum cost
    for magic_square in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(magic_square[i][j] - s[i][j])
        min_cost = min(min_cost, cost)
    
    return min_cost

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

