#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# probability formula is P(event) = #of favorable outcomes / total of outcomes which means to find the total number of outcomes is
#  total of outcomes = #of outcomes / P(event)


def eating_cookies(n, cache=None):
    #  total of outcomes = # of possible outcomes / P(event)
    if cache is None or type(cache) == list:
        cache = {0: 1, 1: 1, 2: 2}
    if n < 0:
        return 0
    elif n not in cache:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


print(eating_cookies(40))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
