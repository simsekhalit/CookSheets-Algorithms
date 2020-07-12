#!/bin/python3
import os
from collections import Counter


# This is the 3rd method for solving this problem which uses Counter Technique
# Hold a counter which stores state of adjacent blocks which are currently expanding.
# Currently expanding means that horizontal width is still actively increasing.
# Expansion keeps continuing while new blocks' heights are greater than equal to the related block.
# Expansion stops when a new block comes which is shorter than the related block by height.
# For example look at the pattern: 5 7 8 6 9
# 5's expansion continued until the end. On the other hand 7's expansion is stopped when 6 is encountered.
# Whenever an expansion is stopped calculate the final area and compare with the max_area. Update max_area if necessary.
# Note that: when 7's expansion is completed, final area was 7 * 2 = 14
# Also when a new block comes it does not start from 1. It starts from longest possible path. Look at the 6,
# it starts from 3 because it can extend to 7 (path is 7-8-6)
# Finally at the end complete all expansions since the road is finished and there are no more buildings.
def largestRectangle(h):
    counter = Counter()

    max_area = 0

    for x in h:
        counter[x] += 1

        for y in tuple(counter):
            if x < y:
                if counter[y] + 1 > counter[x]:
                    counter[x] = counter[y] + 1

                area = y * counter.pop(y)

                if area > max_area:
                    max_area = area

            elif x > y:
                counter[y] += 1

        if x not in counter:
            counter[x] = 1

    for x, y in counter.items():
        if x * y > max_area:
            max_area = x * y

    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
