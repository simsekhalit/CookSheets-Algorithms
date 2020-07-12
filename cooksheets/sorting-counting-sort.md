## Sorting - Counting Sort
Counting sort is a sorting technique based on keys between a specific range.\
Memory Complexity: O(n)\
Time Complexity: O(n)\
Typical Implementation:
```python
# Max range is the maximum value of any item can be in the array.
def counting_sort(array, max_range):
    # Result array
    result = [0] * len(array)

    # Counter array for storing count of each individual item
    counter = [0] * max_range

    # Update counter for each item
    for item in array:
        counter[item] += 1

    # Update counter array in a way that counter[i] stores real position of i

    for i in range(1, max_range):
        counter[i] += counter[i - 1]

    # Update the result array
    for i in range(len(array)):
        item = array[i]
        result[counter[item] - 1] = item
        counter[item] -= 1

    return result
```

### Related Problems
[HackerRank - Fraudulent Activity Notification](../problems/hackerrank-fraudulent-activity-notifications)

### Related Resources
https://www.geeksforgeeks.org/counting-sort/
