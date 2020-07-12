#!/bin/python3
import os
from collections import Counter


# Use 2 counters.
# Data Counter which holds the number of occurrences of each number
# Frequency Counter which holds the number of frequencies exist in the database
# Note that values of Frequency Counter must never be less than 0
def freqQuery(queries):
    result = []
    dataCounter = Counter()
    frequencyCounter = Counter()

    for operation, data in queries:
        if operation == 1:
            frequency = dataCounter[data]

            if frequency > 0:
                frequencyCounter[frequency] -= 1

            frequencyCounter[frequency + 1] += 1
            dataCounter[data] += 1

        elif operation == 2:
            frequency = dataCounter[data]

            if frequency > 0:
                frequencyCounter[frequency] -= 1
                frequencyCounter[frequency - 1] += 1
                dataCounter[data] -= 1

        else:
            result.append(str(int(frequencyCounter[data] > 0)))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
