"""
The lazy_excpets module. Defines errors for lazy properties.
"""

class LazyPropertyError(ValueError):
    """
    The exception for multiple lazy properties initialization.
    """
    def __init__(self, msg=''):
        super().__init__(msg or 'amount of lazy properties doesn\'t match that'
                                ' of values')

