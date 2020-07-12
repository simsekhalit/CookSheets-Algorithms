#!/bin/python3
import os


def isBalanced(s):
    # Empty string is balanced
    if len(s) == 0:
        return "YES"

    # If length is an odd number, string cannot be balanced
    if len(s) % 2 != 0:
        return "NO"

    opening_brackets = {"{", "(", "["}
    closing_brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    stack = []

    # Iterate over the string using the stack
    # If opening bracket is detected, add to stack and continue
    # If closing bracket is detected, look for its match. If not found string is unbalanced
    for c in s:
        if c in opening_brackets:
            stack.append(c)
        else:
            # If the stack is empty it is not possible that a closing bracket has its match in the stack
            if len(stack) == 0:
                return "NO"

            top = stack.pop()

            if top != closing_brackets[c]:
                return "NO"

    # If stack is not empty this means there are redundant opening bracket(s) left at the end of the string
    if len(stack) != 0:
        return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
