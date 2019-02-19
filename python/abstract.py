from abc import ABCMeta, abstractmethod


class Base(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    """All abstract methods from the super class must be implemented."""

    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'
