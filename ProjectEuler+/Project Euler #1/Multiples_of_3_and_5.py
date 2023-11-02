#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    multiples_of_3 = (n - 1) // 3
    multiples_of_5 = (n - 1) // 5
    multiples_of_15 = (n - 1) // 15
    sum = (
        3 * multiples_of_3 * (multiples_of_3 + 1) // 2 +
        5 * multiples_of_5 * (multiples_of_5 + 1) // 2 -
        15 * multiples_of_15 * (multiples_of_15 + 1) // 2
    )
    print(sum)
