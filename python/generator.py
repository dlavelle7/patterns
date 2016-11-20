#!/usr/bin/env python


class FirstN(object):
    """Generator pattern. This example is both an iterable and an iterator."""

    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        """An iterable has __iter__() which returns an iterator."""
        return self

    def next(self):
        """An iterator has next() returning the next item in the iteration."""
        if self.num < self.n:
            current, self.num = self.num, self.num + 1
            return current
        else:
            raise StopIteration


def firstN(n):
    """Generator function.

    Generator functions allow you to declare a function that behaves like an
    iterator (i.e it can be used in a for loop).
    """
    num = 0
    while num < n:
        yield num
        num += 1


# Generator expression
first_n_gen_exp = (x for x in range(1000000))


assert sum(FirstN(1000000)) == 499999500000
assert sum(firstN(1000000)) == 499999500000
assert sum(first_n_gen_exp) == 499999500000
