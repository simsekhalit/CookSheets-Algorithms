#!/bin/python3
import gc
import os


# This solution partially uses the Counter Technique.
# There are two states that can be seen while iterating over the characters.
# One is opening state which means the same character initially repeating itself.
# Whenever the current character in the loop changes from the opening state's character,
# opening state finishes and total should be increased according to formula: n * (n + 1) / 2
# The other state is closing state. This means a string is done repeating itself because a different character is
# encountered (e.g. "aaaab..."). At that point closing_states['a'] is set to 4 because palindrome can only
# extend as much as the number of 'a' on the left side.
# For each character in the future iterations, if 'a' comes, total is increased by 1 and closing_states[a] is decreased
# by 1. Whenever a different character comes or closing_states['a'] becomes 0 closing_states is reset.
def substrCount(n, s):
    total = 0

    opening_state = [s[0], 0]
    closing_states = {}

    for a in s:
        if closing_states:
            # If the current item in the iteration exists in the closing_states increment total by 1 and
            # decrement closing_states[a] by 1.
            # Otherwise reset the closing_states dictionary.
            if a in closing_states and closing_states[a] > 0:
                total += 1
                closing_states = {a: closing_states[a] - 1}

            else:
                closing_states = {}

        # While the same character repeating, increment opening_state[1] by 1.
        if a == opening_state[0]:
            opening_state[1] += 1

        # When the repetition is finished because a new character is encountered, increase total by n * (n + 1) / 2.
        # Then start closing state for the old character and opening state for the new character.
        else:
            char = opening_state[0]
            count = opening_state[1]

            total += count * (count + 1) // 2

            closing_states[char] = count

            opening_state[0] = a
            opening_state[1] = 1

    # Any leftover items should also increment the total.
    total += opening_state[1] * (opening_state[1] + 1) // 2

    return total


if __name__ == '__main__':
    gc.disable()

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
