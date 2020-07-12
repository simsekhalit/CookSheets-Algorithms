#!/bin/python3
import os


# Find left spans according to the Stock Span Technique.
def findLeftSpans(arr):
    spans = [0] * len(arr)
    spans[0] = 1

    for i in range(1, len(arr)):
        span = 1

        while i - span >= 0 and arr[i - span] >= arr[i]:
            span += spans[i - span]

        spans[i] = span

    return spans


# Find right spans according to reverse version of the Stock Span Technique.
def findRightSpans(arr):
    spans = [0] * len(arr)
    spans[-1] = 1

    for i in range(len(arr) - 2, -1, -1):
        span = 1

        while i + span < len(arr) and arr[i + span] >= arr[i]:
            span += spans[i + span]

        spans[i] = span

    return spans


# Merge left and right spans and return two sided spans.
def findSpans(arr):
    leftSpans = findLeftSpans(arr)
    rightSpans = findRightSpans(arr)

    return [leftSpans[i] + rightSpans[i] - 1 for i in range(len(arr))]


# This solution uses the Stock Span Technique.
# Firstly, find spans of all items in the array.
# Then create a dict of windows which contains mappings of window size to item value.
# Then create result array and initialize it with zeros.
# Finally, fill the result array using windows dict.
def riddle(arr):
    spans = findSpans(arr)

    windows_dict = {}

    # Create windows dict which contains the information that which windows size has which max value.
    for i in range(len(arr)):
        window = spans[i]

        if window not in windows_dict or windows_dict[window] < arr[i]:
            windows_dict[window] = arr[i]

    max_value = 0

    result = [0] * len(arr)

    # Iterate with i from from N - 1 to 1 while checking windows dict.
    # Fill the missing values with last encountered max value.
    # Or use last encountered max value again if it is greater than or equal to the windows_dict[i]
    # Purpose of the last check is that if a value has a span of N, this means it is actually in the windows of
    # N, N - 1, N - 2, ..., 1 so it should also be checked that if value of window size N is greater than
    # value of windows size N - 1
    for i in range(len(arr), 0, -1):
        if i not in windows_dict or windows_dict[i] <= max_value:
            result[i - 1] = max_value

        else:
            max_value = windows_dict[i]
            result[i - 1] = max_value

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
