"""
The subscribe_methods module. Provides functionality of subscribing multiple
methods into a list.
"""

from __future__ import absolute_import
from functools import partial


class subscribe_methods():
    """
    The subscribe_methods decorator. Used to create a list and subscribe
    multiple methods into it for later calls.
    """
    def __init__(self, func, func_list=None, trigger_name=''):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name=  func.__name__
        self.func_list = func_list or []
        self.trigger_name = trigger_name or self.name

    def add_method(self, func):
        """
        Add the method into methods list.

        @param method func
        @return subscribe_methods decorated method
        """
        self.func_list.append(func)
        return type(self)(func, self.func_list, self.trigger_name)

    def __get__(self, instance, cls=None, *args, **kwargs):
        """
        The descriptor protocol of python. When the list method is visited,
        return the methods list instead.

        @return list methods list
        """
        if instance is None:
            return self
        if self.name == self.trigger_name:
            return self.func_list
        return partial(self.func, instance)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


import unittest


class TestSubscribeMethods(unittest.TestCase):
    """
    Test subscribe_methods decorator class.
    """
    class _Test():
        """
        The class for test.
        """
        @subscribe_methods
        def methods(self):
            pass

        @methods.add_method
        def method1(self):
            pass

        @methods.add_method
        def method2(self):
            pass

    def test_subscribed_methods(self):
        """
        Test subscribe_methods decorator with the test class.
        """
        # create a test class object
        test = type(self)._Test()

        # check the length of methods list
        self.assertEqual(len(test.methods), 2)


if __name__ == '__main__':
    # run TestSubscribeMethods
    unittest.main()

