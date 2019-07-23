"""
The scale_image_mixin module. Defines mixin behaviors of all scale-like images.
"""

from __future__ import absolute_import

import numpy as np
import cv2 as cv

from utils.mixin_template import Mixin
from utils.lazy_property import lazy_property
from settings import config


class ScaleImageMixin(Mixin):
    """
    The mixin class for scale-like element images.
    """
    @lazy_property
    def elements(self):
        """
        Evaluation method for the lazy property elements for all the scale
        image in the clockwise order.

        @return list list of elements in the elements image in clockwise order
        """
        # get outer contours
        contours, _ = self._find_clean_contours(self.img,
                                                mode=cv.RETR_EXTERNAL)

        # create and return element list
        sorted_element_list = self._sort_in_clockwise(
                [ type(self)._ELEMENT(contour, -1) for contour in contours ],
                                                self.inscribed_circle.center)
        for element in sorted_element_list:
            element._sector_no = sorted_element_list.index(element)
        return sorted_element_list

    def _sort_in_clockwise(self, elements, center):
        """
        Sort the elements in clockwise order (0 ~ 11).

        @param list elements: element list to be sorted
        @param point center: center of the clock face's inscribed circle
        @return list sorted elements
        """
        # zip the element list with their angles to the center of the circle
        sorted_element_angles = sorted(map(lambda e: (e, np.arctan2(
                                *np.subtract(e.center, center))), elements),
                                key=lambda e_ag: e_ag[1], reverse=True)

        # sort and return the element list
        return list(map(lambda e_ag: e_ag[0],
               list(filter(lambda e_ag: e_ag[1] >= type(self)._START_RAD,
                           sorted_element_angles)) +
               sorted(filter(lambda e_ag: e_ag[1] < type(self)._START_RAD,
                             sorted_element_angles), key=lambda e_ag: e_ag[1],
                      reverse=True)))

config(ScaleImageMixin)


import unittest


class TestScaleImageMixin(unittest.TestCase):
    """
    Test ScaleImageMixin class.
    """
    def test_elements(self):
        """
        Test lazy property elements.
        """
        self.assertIsNotNone(ScaleImageMixin.elements.__doc__)

    def test_sort_in_clockwise(self):
        """
        Test _sort_in_clockwise method.
        """
        self.assertIsNotNone(ScaleImageMixin._sort_in_clockwise.__doc__)


if __name__ == '__main__':
    # run unittest TestScaleElementMixin
    unittest.main()

