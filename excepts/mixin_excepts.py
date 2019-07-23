class MixinInitError(TypeError):
    def __init__(self, msg=''):
        super().__init__(msg or 'Can\'t instantiate mixin class')

