#!/bin/python3
import os


# This solution uses Two Pointer Technique.
# Firstly, the array is sorted.
# Then the array is iterated over with two pointers while checking for pairs that satisfy the required condition.
def pairs(k, arr):
    arr.sort()

    output = 0

    j = 1

    # Iterate over the array with two pointers
    for i in range(len(arr)):
        while True:
            # If the second pointer goes beyond the end then search is over return the output.
            if j == len(arr):
                return output

            diff = arr[j] - arr[i]

            # If diff is less than the target value then second pointer should be incremented.
            if diff < k:
                j += 1

            # If diff is equal to the target value then increment output and both pointers by 1.
            elif diff == k:
                output += 1
                j += 1
                break

            # If diff is greater than the target value then increment the first pointer.
            else:
                break


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
