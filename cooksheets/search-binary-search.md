## Search - Binary Search
The idea of binary search is to use the information that the array is sorted.\
Time complexity is O(log n)\
Typical implementation:
```python
def binary_search(array, search_item):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
    
        if array[mid] < search_item: 
            left = mid + 1
        elif array[mid] == search_item:
            return mid
        else:
            right = mid - 1
```

### Related Problems
[HackerRank - Minimum Time Required](../problems/hackerrank-minimum-time-required)

### Related Resources
https://www.geeksforgeeks.org/binary-search/
