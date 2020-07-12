## General
This CookSheet is intended to provide some tricks about the Python language. The tricks are most consisting of 
performance related tips.

### 1. Dictionaries
The Python language has some kind of optimizations over using `{}` rather than `dict()`. This is because in the
bytecode level, `{}` is interpreted as special syntax and has some specific instructions which speeds-up operations
related to dictionary operations. In this topic, creating a dictionary and initializing a dictionary operations are
examined.

#### 1.1. Creating a dictionary
There are two ways of creating a dictionary in Python. One is with the special syntax as `a = {}` and the other is
with the constructor as `a = dict()`. Firstly, let's examine the bytecodes of these two methods:
```python
from dis import dis
dis("{}")
print("-" * 50)
dis("dict()")
```
Output of the above:
```
  1           0 BUILD_MAP                0
              2 RETURN_VALUE
--------------------------------------------------
  1           0 LOAD_NAME                0 (dict)
              2 CALL_FUNCTION            0
              4 RETURN_VALUE
```
So it is clear that `{}` uses `BUILD_MAP` instruction while `dict()` uses `CALL_FUNCTION` instruction. Latter is a
function call after all. Let's examine the performance benchmarks of these two methods:
```python
from timeit import timeit

print(timeit("a = {}"))
print(timeit("a = dict()"))
```
Output of the above:
```
0.02136518400038767
0.05324148900035652
```
Hence it is observed that `{}` is roughly **152%** faster than `dict()`. A detailed reasoning behind this result is that
there is a difference in how the objects are allocated in the background. Python allocates a fixed-size
"free list" where it can quickly allocate basic objects such as `dict`, `list`, `set` etc.. This dramatically
speeds up the process for creating new objects.\
For further information:\
https://stackoverflow.com/questions/664118/whats-the-difference-between-dict-and
https://stackoverflow.com/questions/6610606/is-there-a-difference-between-using-a-dict-literal-and-a-dict-constructor

#### 1.2. Initializing a dictionary
A dictionary can be initialized either by using another dictionary or using an iterable which contains items with
size of 2 e.g. `[(1, 0), (2, 0), (3, 0)]`. There is no difference when initializing from another dictionary between
methods `{**other}` and `dict(other)`. So let's examine the case when initializing from an iterable:
```python
from timeit import timeit

setup = """\
from itertools import repeat
data = tuple(zip(range(100), repeat(0, 100)))
"""

case1 = """\
{a: b for a, b in data}
"""

case2 = """\
dict(data)
"""

print(timeit(case1, setup))
print(timeit(case2, setup))
``` 
Output of the above:
```
0.3124946579991956
0.2419830560011178
```
Hence this time it is observed that using `dict()` is roughly 29% faster than dict comprehension. Therefore optimal
decision between two methods mostly depends on the circumstances. It should also be noted that unless this kind of
initialization has been used with immutable types such as `int`, there might occur unwanted side effects. When
initialization is required with the mutable types consider using 
[`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy) method.

### 2. Lists
Similar to dictionaries Python interprets differently the usages of `[]` and `list()`. In this topic creating a list
and initializing a list operations are examined.

#### 2.1. Creating a list
A list can either be created by using `[]` syntax or using `list()` constructor method. Let's examine the
bytecodes of the these:

##### Bytecodes
```python
from dis import dis
dis("[]")
print("-" * 50)
dis("list()")
```
Output of the above:
```
  1           0 BUILD_LIST               0
              2 RETURN_VALUE
--------------------------------------------------
  1           0 LOAD_NAME                0 (list)
              2 CALL_FUNCTION            0
              4 RETURN_VALUE
```
It is observed that bytecodes of two methods are different. Let's examine the performance benchmarks:
```python
from timeit import timeit

print(timeit("[]"))
print(timeit("list()"))
```
Output of the above:
```
0.011909509001270635
0.049610781999945175
```
Hence it is observed that creating a list with `[]` syntax is roughly **317%** faster than using `list()`.

#### 2.2 Initializing a list

There are typically four different ways to initialize a list. Let's examine their performance benchmarks:
```python
from itertools import repeat
from timeit import timeit

case1 = "[0] * 100"
case2 = "[*repeat(0, 100)]"
case3 = "[a for a in repeat(0, 100)]"
case4 = """\
tmp = []
for i in repeat(0, 100):
    tmp.append(i)
"""

print(timeit(case1))
print(timeit(case2))
print(timeit(case3))
print(timeit(case4))
```
Output of the above:
```
0.2498775439999008
0.3843762610013073
1.5005731160017604
3.405175412000972
```
Hence it is observed that `[0] * 100` syntax is roughly **54%** faster than args unpacking, **501%** faster than
list comprehension and **1263%** faster than traditional loop.

> The reasoning behind these results is the implementation of the Python takes advantage of underlying C structure
> as much as possible. For example when the array is known during initialization, this information is used.
> There are some other bytecode level optimizations which affects these results but since those are out of the scope
> of this topic, they are not mentioned.

It should also be noted that first method of initialization basically duplicates same object 100 times. While this
does not concern us with the immutable types such as `int`, we should be cautious when working with mutable types.
Even though it is dramatically slower [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy)
method might be required on some cases.
