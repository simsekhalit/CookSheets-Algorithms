#!/bin/python3
import os


# Go for a greedy solution.
# Sort the array then start from the end. As the first step let each of the friends buy one flower.
# Then go for a second turn and let each friend buy their second flower.
# Keep going until there are no more flowers left.
# For example if there are 3 friends, last 3 flowers (c[-1], c[-2], and c[-3]) are bought as (0 + 1) * price
# Then next 3 flowers (c[-4], c[-5] and c[-6]) are bought twice the price as (1 + 1) * price.
# This pattern goes on until no more flowers left to buy.
def getMinimumCost(k, c):
    c.sort()
    result = 0

    for i in range(len(c)):
        result += (i // k + 1) * c[-i - 1]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
