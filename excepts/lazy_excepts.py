class LazyPropertyError(ValueError):
    def __init__(self, msg=''):
        super().__init__(msg or 'amount of lazy properties doesn\'t match that'
                                ' of values')

