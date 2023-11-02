#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    A, B, C = 1, 2, 3
    evens_sum = 2
    while C < n:
        if not C % 2:
            evens_sum += C
        A, B, C = B, C, B + C
    print(evens_sum)
