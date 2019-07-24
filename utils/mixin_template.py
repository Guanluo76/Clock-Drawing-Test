"""
The mixin_template module. Defines template parent class for all mixins.
"""

from __future__ import absolute_import

from excepts.mixin_excepts import MixinInitError


class Mixin():
    """
    The parent class for all mixins. All mixins shouldn't be able to be
    instantiated.
    """
    def __init__(self, *args, **kwargs):
        """
        Raise error when trying to instantiate a mixin class.
        """
        raise MixinInitError

