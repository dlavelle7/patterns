#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Different varieties of decorators."""
import time


def log_ex_time(original_func):
    def new_func():
        start = time.time()
        result = original_func()
        end = time.time()
        print "{0} took {1} secs to execute".format(original_func, end - start)
        return result
    return new_func


def decorator_with_args(*dec_args, **dec_kwargs):
    def actual_decorator(original_func):
        def new_func():
            print 'Decorator args: ', dec_args, dec_kwargs
            return original_func()
        return new_func
    return actual_decorator


def decorated_function_with_args(original_func):
    def new_func(*args, **kwargs):
        print "Decorated function args: ", args, kwargs
        result = original_func(*args, **kwargs)
        return result
    return new_func


def decorator_has_self_instance(callable_func):
    """Access Spam instance from within a decorator"""
    def look_at_self(*args, **kwargs):
        self = args[0]
        print "'self' is of type {0}".format(type(self))
        return callable_func(*args, **kwargs)
    return look_at_self


@log_ex_time
def bar():
    time.sleep(0.5)
    print 'bar'


@decorator_with_args('dec1', blah='blah2')
def foo():
    print 'foo'


@decorated_function_with_args
def baz(*args, **kwargs):
    print 'baz function args: ', args, kwargs


class Spam(object):

    @decorator_has_self_instance
    def eggs(self, arg):
        print "{0}".format(arg)


if __name__ == "__main__":
    bar()
    foo()
    baz('baz1', bazzy='bazzy2')
    spam = Spam()
    spam.eggs("I have to push the pram a lot")
