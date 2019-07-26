"""
The lazy_property module. Provides lazy property functionality.
"""

from __future__ import absolute_import

from excepts.lazy_excepts import LazyPropertyError


class _LazyProperty():
    """
    Decorator that converts a method with a single self argument into a lazy
    evaluated property
    """
    def __init__(self, func, name=None):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name = name or func.__name__

    def __get__(self, instance, cls=None):
        """
        Call the function and put the return value in instance.__dict__ to
        implement lazy property
        """
        if instance is None:
            return self
        res = instance.__dict__[self.name] = self.func(instance)
        return res


class _MultiLazyProperties():
    """
    Decorator that links methods with a single self argument and use same
    initializing function together and converts them into lazy property.

    i.e. all of the property values would only be evaluated after at least one
          of them is used.
    """
    def __init__(self, func, name=None):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name = name or func.__name__

        type(self).name_list += [ self.name ]

    def add(self, func):
        """
        Add a new property.
        """
        return type(self)(func)

    def function(self, func):
        """
        Add the initializing function. The function must return same amount of
        values as that of the properties, and must take at most one argument
        (self or cls).
        """
        type(self).result_func = func
        return func

    def _make_result_name_list(self, caller):
        """
        Call the evaluation function and zip the properties' name list and
        result list together.

        @param instance / class caller: caller of the evaluation function
        @return 2-d list name-value pair list
        """
        result = type(self).result_func(caller) if \
                                    type(self).result_func.__code__. \
                                    co_argcount else type(self).result_func()

        if not len(result) == len(type(self).name_list):
            raise LazyPropertyError

        return zip(type(self).name_list, result)

    def __get__(self, instance, cls=None):
        """
        Call the function and put the return value in instance.__dict__ to
        implement lazy property.
        """
        if instance is None:
            return self

        if not self.name in instance.__dict__:
            for name, val in self._make_result_name_list(instance or cls):
                instance.__dict__[name] = val

        return instance.__dict__[self.name]


def multi_lazy_properties(name=''):
    """
    Create a new delegate multi_lazy_properties class.

    @param str name: name of the first lazy property
    """
    return type(name + '_multi_lazy_properties', (_MultiLazyProperties, ),
                                                 dict(name_list=[],
                                                     result_func=None))

lazy_property = _LazyProperty


import unittest


class TestLazyProperty(unittest.TestCase):
    """
    Test lazy_property.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # count number of times evaluation method is called
        self.eval_times = 0

    @lazy_property
    def foo(self):
        self.eval_times += 1
        return 'foo'

    def test_lazy_property(self):
        first_eval = self.foo
        second_eval = self.foo
        self.assertEqual(self.eval_times, 1)
        self.assertEqual([ first_eval, second_eval ], [ 'foo', 'foo' ])


class TestMultiLazyProperty(unittest.TestCase):
    """
    Test multi_lazy_properties.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # count number of times evaluation method is called
        self.eval_times = 0
        type(self).eval_times2 = 0

    # set of multiple lazy properties with method
    @multi_lazy_properties('foo')
    def foo(self):
        pass

    @foo.add
    def bar(self):
        pass

    @foo.function
    def foo_bar_values(self):
        self.eval_times += 1
        return 'foo', 'bar'

    # another set of multiple lazy properties with classmethod
    @multi_lazy_properties('foo2')
    def foo2(self):
        pass

    @foo2.add
    def bar2(self):
        pass

    @classmethod
    @foo2.function
    def foo_bar_values2(cls):
        cls.eval_times2 += 1
        return 'foo2', 'bar2'

    def test_multi_lazy_property(self):
        """
        Test the multiple lazy properties.
        """
        # set of multiple lazy properties with method
        foo_first_eval = self.foo
        foo_second_eval = self.foo

        bar_first_eval = self.bar
        bar_second_eval = self.bar

        self.assertEqual(self.eval_times, 1)
        self.assertEqual([ foo_first_eval, foo_second_eval ], [ 'foo', 'foo' ])
        self.assertEqual([ bar_first_eval, bar_second_eval ], [ 'bar', 'bar' ])
        self.assertEqual(self.foo_bar_values(), ('foo', 'bar'))

        # another set of multiple lazy properties with classmethod
        foo2_first_eval = self.foo2
        foo2_second_eval = self.foo2

        bar2_first_eval = self.bar2
        bar2_second_eval = self.bar2

        self.assertEqual(self.eval_times2, 1)
        self.assertEqual([ foo2_first_eval, foo2_second_eval ],
                         [ 'foo2', 'foo2' ])
        self.assertEqual([ bar2_first_eval, bar2_second_eval ],
                         [ 'bar2', 'bar2' ])
        self.assertEqual(self.foo_bar_values2(), ('foo2', 'bar2'))


if __name__ == '__main__':
    unittest.main()

