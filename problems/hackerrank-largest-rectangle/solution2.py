#!/bin/python3
import os


# This is a supplementary method for finding left spans
def findLeftSpans(h):
    size = len(h)

    # Create the span array with all values are 0 and
    # put 1 on the first item since the span of the first item is always 1
    spans = [0] * size
    spans[0] = 1

    # Create the stack and put first item to stack.
    stack = [0]

    for i in range(1, size):
        # Pop top of the stack as long as it is greater than or equal to the current element
        # Because stack must contain only elements that current element would not be able to span to
        while len(stack) != 0 and h[stack[-1]] >= h[i]:
            stack.pop()

        # If stack is empty then it means current element spans to all the way to the left
        if len(stack) == 0:
            spans[i] = i + 1

        # Otherwise current element can only span as far as to the element which is on the top of the stack
        else:
            spans[i] = i - stack[-1]

        # Add the current element to the top of the stack
        stack.append(i)

    return spans


# This is a supplementary method for finding right spans
def findRightSpan(h):
    size = len(h)

    # Create the span array with all values are 0 and
    # put 1 on the last item since the span of the last item is always 1
    spans = [0] * size
    spans[-1] = 1

    # Create the stack and put last item to stack.
    stack = [size - 1]

    for i in range(size - 2, -1, -1):
        # Pop top of the stack as long as it is greater than or equal to the current element
        # Because stack must contain only elements that current element would not be able to span to
        while len(stack) != 0 and h[stack[-1]] >= h[i]:
            stack.pop()

        # If stack is empty then it means current element spans to all the way to the right
        if len(stack) == 0:
            spans[i] = size - i

        # Otherwise current element can only span as far as to the element which is on the top of the stack
        else:
            spans[i] = stack[-1] - i

        # Add the current element to the top of the stack
        stack.append(i)

    return spans


# This is the 2nd method for solving this problem which uses version of Stock Span Technique that uses a stack.
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
