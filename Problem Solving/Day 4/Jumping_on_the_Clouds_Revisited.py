/***
CHALLENGE:
A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.
There is an array of clouds,  and an energy level e=100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k)%n]. If it lands on a thundercloud, c[i]=1, its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud 0.
Given the values of n, k, and the configuration of the clouds as an array c, determine the final value of e after the game ends.

Function Description:
Complete the jumpingOnClouds function in the editor below.
jumpingOnClouds has the following parameter(s):
  int c[n]: the cloud types along the path
  int k: the length of one jump

Returns:
int: the energy level remaining.

Input Format:
The first line contains two space-separated integers, n and k, the number of clouds and the jump distance.
The second line contains n space-separated integers  where . Each cloud is described as follows:
  If c[i]=0, then cloud i is a cumulus cloud.
  If c[i]=1, then cloud i is a thunderhead.
***/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    i = 0
    while True:
        i = (i + k) % len(c)
        e -= 1 + (2 * c[i])
        if i == 0:
            break
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

