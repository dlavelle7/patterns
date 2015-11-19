#!/usr/bin/env python
import sys

def main():
    true_fib = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233}
    assert fibonacci(len(true_fib)) == true_fib

def fibonacci(n):
    sequence = [0, 1]
    return sequence

if __name__ == "__main__":
    main()
