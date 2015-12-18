#!/usr/bin/env python


class FirstN(object):
    """Generator pattern (an iterable)."""

    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def next(self):
        if self.num < self.n:
            current, self.num = self.num, self.num + 1
            return current
        else:
            raise StopIteration


def firstN(n):
    """Generator function."""
    num = 0
    while num < n:
        yield num
        num += 1


assert sum(FirstN(1000000)) == 499999500000
assert sum(firstN(1000000)) == 499999500000
