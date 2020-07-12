#!/bin/python3
import os
from collections import Counter


# This solution uses the Signature Technique
def sherlockAndAnagrams(s):
    counter = Counter()
    answer = 0

    # Iterate over the string.
    for i in range(len(s)):
        add = 0
        mul = 1

        # Iterate over the substrings of each length.
        for j in range(i, len(s)):

            # Sum and multiplication of each characters in the substring yields the signature
            add += ord(s[j])
            mul *= ord(s[j])
            signature = (add, mul)

            # Store each signature in the Counter
            counter[signature] += 1

    # For each value in the Counter find the number of pairs with the formula: n * (n - 1) / 2
    # Then add the number of pairs to the answer
    for count in counter.values():
        answer += count * (count - 1) // 2

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
