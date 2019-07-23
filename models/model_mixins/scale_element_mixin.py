"""
The scale_element_mixin module. Defines mixin behaviors for all scale-like
elements.
"""

from __future__ import absolute_import

import cv2 as cv

from utils.mixin_template import Mixin
from utils.lazy_property import multi_lazy_properties

class ScaleElementMixin(Mixin):
    @multi_lazy_properties('angle')
    def angle(self):
        pass

    @angle.add
    def center(self):
        pass

    @angle.add
    def box_points(self):
        pass

    @angle.function
    def _get_angle_center_box_points(self):
        """
        Evaluation method of lazy properties angle and midpoint.

        @return tuple (angle, center, box_points)
        """
        center, (width, height), angle = cv.minAreaRect(self._contour)
        return angle, center, cv.boxPoints((center, (width, height), angle))


import unittest


class TestScaleElementMixin(unittest.TestCase):
    """
    Test ScaleElementMixin class.
    """
    def test_get_angle_center_box_points(self):
        """
        Test _get_angle_center_box_points method.
        """
        self.assertIsNotNone(
                ScaleElementMixin._get_angle_center_box_points.__doc__)


if __name__ == '__main__':
    # run unittest TestScaleElementMixin
    unittest.main()

