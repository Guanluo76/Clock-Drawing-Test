"""
The meta_mixin module. Provides functionality for mixins.
"""

class MetaMixin(type):
    """
    The metaclass for mixins. User classes should set this as metaclass, and
    add the mixins into the mixins list.
    e.g. class User(metaclass=MetaMixin, mixins=(Mixin1, Mixin2)):
    """
    def __new__(cls, name, bases, classdict, mixins):
        """
        Add the attributes from mixin classes to the user class when creating
        a new class from this metaclass.

        @param type mixins: the mixin classes
        @return type user classes created
        """
        # create a new class from type
        rclass = super().__new__(cls, name, bases, classdict)

        # add attributes
        for mixin in mixins:
            [ setattr(rclass, attr_name, getattr(mixin, attr_name)) \
                    if not attr_name in rclass.__dict__ else None
                    for attr_name in mixin.__dict__.keys() ]

        return rclass


import unittest


class TestMetaMixin(unittest.TestCase):
    """
    Test MetaMixin.
    """
    class _Mixin():
        """
        The mixin class for test.
        """
        def _mixin_behavior(self):
            """
            The mixin behavior for test.

            @return str test string
            """
            return 'mixin test'

        def __call__(self):
            return 'call'

    class _Test(metaclass=MetaMixin, mixins=(_Mixin, )):
        """
        The user class for test.
        """
        pass

    def test_meta_mixin(self):
        """
        Test meta_mixin.
        """
        # create a test class object
        test = type(self)._Test()

        # check the mixin attributes
        self.assertEqual(test._mixin_behavior(), 'mixin test')
        self.assertEqual(test(), 'call')


if __name__ == '__main__':
    # run unittest TestMetaMixin
    unittest.main()

