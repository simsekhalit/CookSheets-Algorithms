#!/bin/python3
import os


# This is a supplementary method for finding left spans
def findLeftSpans(h):
    size = len(h)

    # Create the span array and initialize all values with 0
    # Put 1 on the first item since the span of the first item is always 1
    spans = [0] * size
    spans[0] = 1

    # Iterate over the items from left.
    # Pivot is the length that current item can span to farthest left.
    # Final version of the pivot is recorded as the left span of the current item.
    for i in range(1, size):
        pivot = 1

        while i - pivot >= 0 and h[i - pivot] >= h[i]:
            pivot += spans[i - pivot]

        spans[i] = pivot

    return spans


# This is a supplementary method for finding right spans
def findRightSpan(h):
    size = len(h)

    # Create the span array with all values are 0 and
    # put 1 on the last item since the span of the last item is always 1
    spans = [0] * size
    spans[-1] = 1

    # Iterate over the items from right.
    # Pivot is the length that current item can span to farthest right.
    # Final version of the pivot is recorded as the right span of the current item.
    for i in range(size - 2, -1, -1):
        pivot = 1

        while i + pivot < size and h[i + pivot] >= h[i]:
            pivot += spans[i + pivot]

        spans[i] = pivot

    return spans


# This is the 1st method for solving this problem which uses version of Stock Span Technique that does not use a stack.
# There are two supplementary methods for finding left and right spans of every single item.
# Sum of the left and right spans minus 1 yields the total span of an item
# Multiplication of span and value of an item gives the area. This way we can find max area.
def largestRectangle(h):
    max_area = 0

    leftSpans = findLeftSpans(h)
    rightSpans = findRightSpan(h)

    for i in range(len(h)):
        span = leftSpans[i] + rightSpans[i] - 1
        area = span * h[i]

        if area > max_area:
            max_area = area

    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
