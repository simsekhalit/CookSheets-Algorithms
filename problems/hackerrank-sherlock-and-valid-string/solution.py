#!/bin/python3
import os
from collections import Counter


# This solution uses the Counter Technique.
# First count each character in the string.
# Then find occurrences of each group.
# There are 3 different cases which are valid:
# Case 1: All the occurrences are of the same group.
# Case 2: If there are 2 groups and one of them is 1 and it's count is 1 as well, string is valid.
# Case 3: If there are 2 groups and size of one of them is N + 1 and it's count is 1
# and the size of the other group is N, string is valid.
def isValid(s):
    counter = Counter(s)
    occurrences = Counter(counter.values())

    # If there are more than 2 groups, string is definitely invalid.
    if len(occurrences) > 2:
        return "NO"

    # If there is less than equal to 1 group, string is valid.
    if len(occurrences) <= 1:
        return "YES"

    # Check for case 2.
    if 1 in occurrences and occurrences[1] == 1:
        return "YES"

    max_index = max(occurrences)

    # Check for case 3.
    if occurrences[max_index] == 1 and max_index - 1 in occurrences:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
