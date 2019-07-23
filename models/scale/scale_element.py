"""
The scale_element module.
"""

from __future__ import absolute_import
from functools import reduce

from utils.meta_mixin import MetaMixin
from utils.subscribe_methods import subscribe_methods
from models.element import Element
from models.model_mixins.scale_element_mixin import ScaleElementMixin
from settings import config


class ScaleElement(Element,
                   metaclass=MetaMixin, mixins=(ScaleElementMixin, )):
    def __init__(self, contour, sector_no):
        super().__init__(contour)
        self._sector_no = sector_no

    @subscribe_methods
    def properness_tests(self):
        pass

    @properness_tests.add_method
    def is_proper_position(self, circle):
        return circle.is_in_sector(self.center, self._sector_no) and \
               (type(self)._MIN_FIT_POINTS <= \
                       reduce(lambda points_no, nxt: points_no + \
               circle.is_in_sector(tuple(nxt), self._sector_no),
                                   [ 0 ] + self.box_points.tolist()))

config(ScaleElement)


import unittest


class TestScaleElement(unittest.TestCase):
    def test_get_angle_center(self):
        self.assertIsNotNone(ScaleElement._get_angle_center.__doc__)


if __name__ == '__main__':
    pass

