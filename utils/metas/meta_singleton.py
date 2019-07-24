"""
The meta_singleton module. Provides functionality for creating singletons.
"""

class MetaSingleton(type):
    """
    The metaclass for singletons.
    """

    # instances list, store the instantiated singleton instances
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """
        When instantiating, check the instances list if a singleton instance
        already exists. If so, return the existing instance, else create a new
        one and return.

        @return object instance for singleton class
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args,
                                                                     **kwargs)
        return cls._instances[cls]


import unittest


class TestMetaSingleton(unittest.TestCase):
    """
    Test MetaSingleton class.
    """
    class _Singleton(metaclass=MetaSingleton):
        """
        The singleton class for test.
        """
        pass

    def test_meta_singleton(self):
        """
        Test MetaSingleton class with the _Singleton test class.
        """
        self.assertIsNotNone(MetaSingleton.__call__.__doc__)

        # create singleton instances for test
        singleton1 = type(self)._Singleton()
        singleton2 = type(self)._Singleton()

        # check if the instances are the same in memory
        self.assertEqual(id(singleton1), id(singleton2))


if __name__ == '__main__':
    # run unittest TestMetaSingleton
    unittest.main()

