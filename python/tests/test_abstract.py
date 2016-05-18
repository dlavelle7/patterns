import unittest
from abstract import Base, Concrete, BadConcrete


class AbstractTest(unittest.TestCase):

    def _assertRaisesCustom(self, exception, message, callable, *args, **kwargs):
        try:
            callable(*args, **kwargs)
        except exception as e:
            if (str(e) != message):
                raise AssertionError("{0} != {1}".format(message, str(e)))
        else:
            raise AssertionError('No exception was raised')

    def test_abstract_methods(self):
        # non implemented abstract method
        self.assertTrue(issubclass(BadConcrete, Base))
        message = "Can't instantiate abstract class BadConcrete with abstract methods bar"
        self._assertRaisesCustom(TypeError, message, BadConcrete)

        # all abstract classes implemented
        concrete = Concrete()
        self.assertEqual('foo', concrete.foo())
        self.assertEqual('bar', concrete.bar())
