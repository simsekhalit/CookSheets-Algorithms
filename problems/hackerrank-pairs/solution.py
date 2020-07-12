#!/bin/python3
import os


# This solution uses a Set.
# Firstly the array is stored in a set.
# Then the array is iterated over while checking if pair of the current element is in the set.
def pairs(k, arr):
    output = 0

    lookup_set = set(arr)

    for a in arr:
        if a + k in lookup_set:
            output += 1

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
