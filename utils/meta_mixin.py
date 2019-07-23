class MetaMixin(type):
    def __new__(cls, name, bases, classdict, mixins):
        rclass = super().__new__(cls, name, bases, classdict)

        for mixin in mixins:
            [ setattr(rclass, attr_name, getattr(mixin, attr_name)) \
                    if not attr_name in rclass.__dict__ else None
                    for attr_name in mixin.__dict__.keys() ]

        return rclass


import unittest


class TestMetaMixin(unittest.TestCase):
    class _Mixin():
        def _mixin_behavior(self):
            return 'hi'

        def __call__(self):
            return 'call'

    class _Test(metaclass=MetaMixin, mixins=(_Mixin, )):
        pass


    def test_meta_mixin(self):
        t = type(self)._Test()
        print(t._mixin_behavior())
        print(t())


if __name__ == '__main__':
    unittest.main()

