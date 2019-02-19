import unittest
from python.abstract import Base, Concrete


class BadConcrete(Base):
    # abstract method bar() not implemented:
    # Class created but error when instantiating
    def foo(self):
        return 'bad foo'


class AbstractTest(unittest.TestCase):

    def test_abstract_methods(self):
        # non implemented abstract method
        self.assertTrue(issubclass(BadConcrete, Base))
        with self.assertRaises(TypeError) as exc_context:
            BadConcrete()
        expected = ("Can't instantiate abstract class BadConcrete with "
                    "abstract methods bar")
        self.assertEqual(str(exc_context.exception), expected)

        # all abstract classes implemented
        concrete = Concrete()
        self.assertEqual('foo', concrete.foo())
        self.assertEqual('bar', concrete.bar())
