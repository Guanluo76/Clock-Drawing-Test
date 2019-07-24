"""
The scale module. The main body of scale test app.
"""

from __future__ import absolute_import
from functools import reduce

import numpy as np
import cv2 as cv

from apps.app import App
from utils.metas.meta_singleton import MetaSingleton
from utils.subscribe_methods import subscribe_methods


class Scale(App, metaclass=MetaSingleton):
    """
    The class to test if clock scales are proper.
    """
    @subscribe_methods
    def methods(self):
        """
        Required by parent class.
        """
        pass

    @methods.add_method
    def _all_scale_elements(self, element_img):
        """
        Test all the scale elements in the element image.

        @param ElementImage element_img: the element image of scales
        @return True if all the elements are correct
        """
        if len(element_img.elements) != 12:
            return False

        return reduce(lambda res, emt: res & emt(element_img.inscribed_circle),
                      [ True ] + element_img.elements)


import unittest


class TestScale(unittest.TestCase):
    """
    Test the scale app.
    """
    def test_all_scale_elements(self):
        """
        Test _all_scale_elements method.
        """
        self.assertIsNotNone(Scale._all_scale_elements.__doc__)


if __name__ == '__main__':
    unittest.main()

