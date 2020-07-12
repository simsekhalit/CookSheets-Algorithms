#!/bin/python3
import os

EXPENDITURES_WINDOW: int
MAX_EXPENDITURES: int = 200


# Create a counter array for storing current state of expenditures
# After creating initialize with the first EXPENDITURES_WINDOW
def createCounterArray(expenditures):
    counterArray = [0] * (MAX_EXPENDITURES + 1)

    for x in expenditures[:EXPENDITURES_WINDOW]:
        counterArray[x] += 1

    return counterArray


# Median finder method for odd sized EXPENDITURES_WINDOW
def getMedianOdd(counterArray):
    middle = EXPENDITURES_WINDOW // 2
    tmp = 0

    for i in range(len(counterArray)):
        tmp += counterArray[i]

        if tmp > middle:
            return i


# Median finder method for even sized EXPENDITURES_WINDOW
def getMedianEven(counterArray):
    middle = EXPENDITURES_WINDOW // 2
    tmp = 0

    for i in range(len(counterArray)):
        tmp += counterArray[i]

        # Finding even median means taking average of the two numbers in the middle
        # Second condition is for the case that those two numbers are the same
        if tmp == middle:
            for j in range(i + 1, len(counterArray)):
                if counterArray[j]:
                    return (i + j) / 2

        elif tmp > middle:
            return i


def activityNotifications(expenditure, d):
    global EXPENDITURES_WINDOW
    EXPENDITURES_WINDOW = d
    total = 0

    counterArray = createCounterArray(expenditure[:EXPENDITURES_WINDOW])

    # Set median according to the case whether EXPENDITURES_WINDOW is even or odd sized
    if EXPENDITURES_WINDOW % 2 == 0:
        getMedian = getMedianEven

    else:
        getMedian = getMedianOdd

    # Slide the window by one for each iteration while updating state of the counter array and detecting notifications
    for i in range(d, len(expenditure)):
        if expenditure[i] >= getMedian(counterArray) * 2:
            total += 1

        counterArray[expenditure[i - EXPENDITURES_WINDOW]] -= 1
        counterArray[expenditure[i]] += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
