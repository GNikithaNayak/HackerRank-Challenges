#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest = 2
    while not n % 2:
        n //= 2
    factor = 3
    max_factor = n ** 0.5
    while factor <= max_factor:
        if not n % factor:
            largest = factor
            n //= factor
            while not n % factor:
                n //= factor
            if n == 1:
                print(largest)
                break
            max_factor = n ** 0.5
        factor += 2
    else:
        print(n)
