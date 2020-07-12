## Signature Technique
The Signature Technique means that finding an efficient way to create a unique key (signature) to use as a hash key with
the dictionary-like structures. There are two different cases for this technique. One is creating a signature from
an unhashable data type such as `list`. Other is creating a common signature for equivalent items which normally have
different hash keys but needs to be considered the same by structures like
[Counters](https://docs.python.org/3/library/collections.html#collections.Counter). In this CookSheet currently only the
latter case is covered.

### 1. Common Signature For Equivalent Items
Imagine a problem which asks to find number of anagram substrings for a given string. Anagram means that two strings
have equal counts of occurring characters. For example `no` and `on`, their character counters are both
`{'n': 1, 'o': 1}`. We can consider two strings as equivalent if they are anagrams. Normally in order to count each
strings that are anagram one can trivially sort their characters and store the resulting string in a counter but this
is not efficient due to O(n logn) time complexity. There are two different methods to perform this operation
efficiently:

#### Method 1
This method stores each character in a list which has the size of the ascii table then converts the list to a tuple then
stores that tuple in a counter.
```python
from collections import Counter

def find_anagrams1(string_):
    counter = Counter()

    for i in range(len(string_)):
        for j in range(i, len(string_)):
            signature = [0] * 128

            for a in string_[i:j + 1]:
                signature[ord(a)] += 1

            # Convert signature from list to tuple so that it becomes hashable.
            signature = tuple(signature)

            counter[signature] += 1

    # In order to be anagram strings there must be at least 2 of that signature.
    return sum(filter(lambda _: _ > 1, counter.values()))
```

#### Method 2
This method generates the signatures of the substrings in a rather intelligent way. Sum and multiplication of the
ordinal values of all the characters in a substring together forms the signature.
```python
from collections import Counter

def find_anagrams2(string_):
    counter = Counter()

    for i in range(len(string_)):
        sum_ = 0
        mul = 1

        for j in range(i, len(string_)):
            ord_ = ord(string_[j])
            sum_ += ord_
            mul *= ord_

            signature = (sum_, mul)
            counter[signature] += 1

    # In order to be anagram strings there must be at least 2 of that signature.
    return sum(filter(lambda _: _ > 1, counter.values()))
```

#### Analysis
In both methods finding substrings produces **O(n<sup>2</sup>)**. But in the first method creating signatures for each
substring additionally produces **O(n)** complexity as well. Hence as a result first method has **O(n<sup>3</sup>)**
complexity. Second method is on the other hand uses a different approach about creating signatures from substrings
therefore it is total complexity remains as **O(n<sup>2</sup>)**.
The trick of the second method's approach is to use previous calculation of the signature for the current calculation
in the inner loop. Notice that `sum_` and `mul` are only reset in the outer loop. They are reused for each iteration
of the inner loop.\
It should be noted that in the second method we are actually converting the characters of each substrings to numbers
with `ord()` then work on those numbers. For example: `"no"` becomes `(110, 111)` and `"on"` becomes `(111, 110)`.
Afterwards we are generating a signature for those numbers that when their order changes, their signature will be the
same. Hence `(110, 111)` and `(111, 110)` both have the same signature.
> Pro Tip: Creating a common signature for a set of numbers independently from their order can be achieved by using
> their sum and multiplications together.

Let's examine the benchmarks of both methods:
```python
from timeit import timeit

print(timeit("find_anagrams1('soonnoon')", number=10000, globals=globals()))
print(timeit("find_anagrams2('soonnoon')", number=10000, globals=globals()))
```
Output of the above:
```
0.6869209269998464
0.1303857680004512
```
Hence it is observed that second method is roughly **428%** faster than the first method for the given test case.

### Related Problems
[HackerRank - Sherlock and Anagrams](../problems/hackerrank-sherlock-and-anagrams)
