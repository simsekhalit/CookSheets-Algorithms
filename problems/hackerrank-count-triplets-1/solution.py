#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Find combination of given number with 2. This is a supplementary method
def comb3(x):
    return x * (x - 1) * (x - 2) // 6


# Count triplets for the case r == 1
def countTripletsForR1(arr):
    counter = Counter()
    result = 0

    # Iterate over the array and find count of each number
    for x in arr:
        counter[x] += 1

    # Add each number's combination with 3 to the result if it is greater than or equal to 3
    for x in counter.values():
        if x >= 3:
            result += comb3(x)

    return result


# Iterate over the array while counting each number in the following way:
# There is a pair in the counter for each number e.g. counter[i] = [x,y]
# i represents the number
# x represents number of occurrences of that number until now.
# y represents number of total partial triplets
#
# Partial triplet means a triplet which is missing its 3rd number. Whenever 3rd number arrives in the iteration
# result is increased for each partial triplets
# Complete triplet -> (0,1,2) , partial triplet -> (0,1)
#
# For example take arr = [1,1,2,2,4] and r = 2:
# At the index 0, counter[1] is updated from [0,0] to [1,0]
# At the index 1, counter[1] is updated from [1,0] to [2,0]
# At this point counter states that there are 2 occurrences of the number 1
# At the index 2, counter[2] is updated from [0,0] to [1,2]
# At this point counter states that there is 1 occurrence of the number 2
# and two partial triplets which are (0,2) and (1,2)
# At the index 3, counter[2] is updated from [1,2] to [2,4]
# At this point counter[2] represents that there are 2 occurrences of the number 2
# and there are 4 partial triplets which are (0,2), (0,3), (1,2) and (1,3)
# At the index 4, 4 comes and completes all 4 partial triplets and result is increased by 4
# At the end result is returned
def countTriplets(arr, r):
    # r == 1 is a special case and it needs to be calculated separately
    if r == 1:
        return countTripletsForR1(arr)

    counter = {1: [0, 0]}
    result = 0

    for x in arr:
        if x in counter:
            counter[x][0] += 1

        else:
            counter[x] = [1, 0]

        if x % r != 0:
            continue

        y = x // r

        if y not in counter:
            continue

        counter[x][1] += counter[y][0]

        result += counter[y][1]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
