#!/bin/python3
import os
import sys


def maxMin(k, arr):
    # Sort the array
    arr.sort()

    # Initially set the result to a really high number
    min_result = sys.maxsize

    # Iterate over the array with two indices to find minimum fairness
    for i in range(len(arr) - k + 1):
        diff = arr[i + k - 1] - arr[i]

        if diff < min_result:
            min_result = diff

    return min_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
