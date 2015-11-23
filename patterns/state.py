from abc import ABCMeta, abstractmethod

class Base(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class BadConcrete(Base):
    # abstract method bar() not implemented:
    # Class created but error when instantiating
    def foo(self):
        return 'bad foo'

class Concrete(Base):
    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'
