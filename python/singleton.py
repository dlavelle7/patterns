class Singleton(object):
    """Singleton design pattern."""

    instance = None

    def __new__(cls, value):
        if not Singleton.instance:
            # Call objects __new__, as cls(value) will bring you back here
            Singleton.instance = super(Singleton, cls).__new__(cls, value)
        return Singleton.instance  # return instance of 'cls' to __init__

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{0} with value {1}".format(repr(self), self.value)


foo = Singleton('foo')
print foo

# Udates the same class instance, with new values
bar = Singleton('bar')
print bar

baz = Singleton('baz')
print baz

# Test
assert baz.value == bar.value == foo.value
assert id(foo) == id(bar) == id(baz)
