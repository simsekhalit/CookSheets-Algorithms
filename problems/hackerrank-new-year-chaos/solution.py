#!/bin/python3


# This solution uses the fact that a person can bribe as most 2 people.
# While iterating over the people, there is always an expected next person.
# If the next person is missing it means that person received a bribe and put it in missing people set
# Missing people can be at most size of 2.
# When the current person during iteration is one of the missing people remove it from missing people set.
# It should also be noted that since missing people can be at size of 2, one of them might bribe other.
def minimumBribes(q):
    missing_people = set()
    next_person = 1
    total_bribes = 0

    for a in q:
        # The purpose of this while loop is that if the current person is not the expected next person,
        # we should add the expected next person to missing people and increment next people by 1
        # while not changing current person.
        while True:
            # If the current person is the next person then total bribes is increased by the amount of size of
            # missing people.
            if a == next_person:
                total_bribes += len(missing_people)
                next_person += 1
                break

            # If the current person is one of the missing people, it is no longer missing we found it!
            elif a in missing_people:
                missing_people.discard(a)

                # Also check the case if missing people were 2 people and one of them bribed other.
                # If the original number of the current person is greater than the other missing person it means
                # he bribed so increase total bribes by 1.
                if len(missing_people) > 0 and a > next(iter(missing_people)):
                    total_bribes += 1

                break

            # If size of missing people set was already 2 and there is a new missing person then it is too chaotic.
            elif len(missing_people) == 2:
                print("Too chaotic")
                return

            # Add the current person to missing people set.
            else:
                missing_people.add(next_person)
                next_person += 1

    print(total_bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
