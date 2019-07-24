"""
The meta_singleton_mixin module.
"""

from __future__ import absolute_import

from utils.metas.meta_singleton import MetaSingleton
from utils.metas.meta_mixin import MetaMixin


class MetaSingletonMixin(MetaSingleton, MetaMixin):
    """
    A metaclass with both singleton and mixin features.
    """
    pass


import unittest


class TestMetaSingletonMixin(unittest.TestCase):
    """
    Test MetaSingletonMixin class.
    """

    class _Mixin():
        """
        Mixin class for testing.
        """
        def mixin_behavior(self):
            """
            Mixin behavior for testing.

            @return str flag string defined in implementation class
            """
            return self._mixin_str

    class _SingletonMixin(metaclass=MetaSingletonMixin, mixins=(_Mixin, )):
        """
        Singleton mixin class for testing.
        """
        def __init__(self):
            self._mixin_str = 'mixin str'

    def test_meta_singleton_mixin(self):
        """
        Test MetaSingletonMixin.
        """
        singleton_mixin1 = type(self)._SingletonMixin()
        singleton_mixin2 = type(self)._SingletonMixin()

        # test singleton
        self.assertEqual(id(singleton_mixin1), id(singleton_mixin2))

        # test mixin
        self.assertEqual(singleton_mixin1.mixin_behavior(), 'mixin str')
        self.assertEqual(singleton_mixin2.mixin_behavior(), 'mixin str')


if __name__ == '__main__':
    # run unittest TestMetaSingletonMixin
    unittest.main()

