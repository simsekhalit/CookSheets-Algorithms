## Stock Span Technique
Stock span technique is used for finding maximum span of each element of a given array in an efficient way. Most of the problems
involving windows can be solved with this technique. A span can basically be defined as number of elements on the left
side of an item which are less than equal to it consecutively. There are two versions of this algorithm: 
One uses a stack and other does not\
Time Complexity: O(n)\
Typical Implementation (without stack):
```python
def find_spans(array):
    # Create spans array and initialize first item with 1 since the span of first item is always 1.
    spans = [0] * len(array)
    spans[0] = 1

    # Iterate over each element while checking if span can be extended.
    for i in range(1, len(array)):
        span = 1

        # Span is extended if the item that is being checked is less than or equal to the current item.
        # Extension amount equals to the span of the item that is being checked.
        while i - span >= 0 and array[i - span] <= array[i]:
            span += spans[i - span]

        spans[i] = span

    return spans
```
Typical Implementation (with stack):
```python
def find_spans(array):
    # Create spans array and initialize first item with 1 since the span of first item is always 1.
    spans = [0] * len(array)
    spans[0] = 1

    # Create a stack with the index of the first item
    stack = [0]

    # Iterate over each element while checking if span can be extended.
    for i in range(1, len(array)):
        span = 1

        # Span is extended if the item that is being checked is less than or equal to the current item.
        # Extension amount equals to the span of the item that is being checked.
        while len(stack) != 0 and array[stack[-1]] <= array[i]:
            stack.pop()
            span += spans[i - span]

        spans[i] = span
        stack.append(i)

    return spans
```
### Related Problems
[HackerRank - Largest Rectangle](../problems/hackerrank-largest-rectangle)\
[HackerRank - Min Max Riddle](../problems/hackerrank-min-max-riddle)

### Related Resources
https://www.geeksforgeeks.org/the-stock-span-problem/
