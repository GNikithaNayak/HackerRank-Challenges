# /***
# CHALLENGE:
# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
#   The player with the highest score is ranked number 1 on the leaderboard.
#   Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

# Function Description:
# Complete the climbingLeaderboard function in the editor below.
# climbingLeaderboard has the following parameter(s):
#   int ranked[n]: the leaderboard scores
#   int player[m]: the player's scores

# Returns:
# int[m]: the player's rank after each new score

# Input Format:
# The first line contains an integer n, the number of players on the leaderboard.
# The next line contains n space-separated integers ranked[i], the leaderboard scores in decreasing order.
# The next line contains an integer, m, the number games the player plays.
# The last line contains m space-separated integers player[j], the game scores.
# ***/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(list(set(ranked)))
    index = 0
    rank_list = []
    n = len(ranked)
    for i in player:
        while (n > index and i >= ranked[index]):
            index += 1
        rank_list.append(n+1-index) 
    return rank_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
