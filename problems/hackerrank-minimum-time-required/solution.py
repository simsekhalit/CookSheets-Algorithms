#!/bin/python3
import os


# Find upper and lower bounds
def findBounds(machines, goal):
    max_power = 0
    total_effect = 0

    for m in machines:
        if m > max_power:
            max_power = m

        total_effect += 1 / m

    lower_bound = int(goal // total_effect)
    upper_bound = lower_bound + max_power

    return lower_bound, upper_bound


# Calculate total production of all machines for given days
def findProduction(machines, days):
    production = 0

    for m in machines:
        production += days // m

    return production


# Find lower and upper bounds of possible solution range. Then perform binary search.
# Note that it is possible that more than one number of days can be equal to same production amount so we must also find
# the lowest one
def minTime(machines, goal):
    lower_bound, upper_bound = findBounds(machines, goal)

    min_days = upper_bound

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        production = findProduction(machines, mid)

        if production < goal:
            lower_bound = mid + 1

        else:
            min_days = mid
            upper_bound = mid - 1

    return min_days


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
