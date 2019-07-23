from __future__ import absolute_import
from functools import partial


class subscribe_methods():
    def __init__(self, func, func_list=None, trigger_name=''):
        self.func = func
        self.__doc__ = getattr(func, '__doc__')
        self.name=  func.__name__
        self.func_list = func_list or []
        self.trigger_name = trigger_name or self.name

    def add_method(self, func):
        self.func_list.append(func)
        return type(self)(func, self.func_list, self.trigger_name)

    def __get__(self, instance, cls=None, *args, **kwargs):
        if instance is None:
            return self
        if self.name == self.trigger_name:
            return self.func_list
        return partial(self.func, instance)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

