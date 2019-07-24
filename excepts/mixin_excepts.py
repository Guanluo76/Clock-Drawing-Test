"""
The minxin_excpets module. Defines exception for mixin classes.
"""

class MixinInitError(TypeError):
    """
    The exception for mixin class when instantiated.
    """
    def __init__(self, msg=''):
        super().__init__(msg or 'Can\'t instantiate mixin class')

