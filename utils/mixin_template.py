from __future__ import absolute_import

from excepts.mixin_excepts import MixinInitError


class Mixin():
    def __init__(self, *args, **kwargs):
        raise MixinInitError

