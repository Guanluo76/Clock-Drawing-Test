"""
The element_image module. Defines the parent class of all element images.
"""

from __future__ import absolute_import

import cv2 as cv

from utils.metas.meta_mixin import MetaMixin
from models.model_mixins.image_mixin import ImageMixin
from utils.lazy_property import lazy_property
from models.circle import Circle


class ElementImage(metaclass=MetaMixin, mixins=(ImageMixin, )):
    """
    The parent class for all element images. Provides a elements list for
    usage.
    """
    def __init__(self, raw_img):
        self._raw_img = raw_img

    @lazy_property
    def inscribed_circle(self):
        """
        The lazy property inscribed_circle. Returns the inscribed circle of the
        clock face.

        @return Circle inscribed circle
        """
        return Circle()

    @lazy_property
    def elements(self):
        """
        The lazy property elements. Returns the list of elements in the element
        image.

        @return list elements list
        """
        # get outer contours
        contours, _ = self._find_clean_contours(self.img,
                                                mode=cv.RETR_EXTERNAL)

        # create and return element list
        return [ type(self)._ELEMENT(contour) for contour in contours ]


import unittest


class TestElementImage(unittest.TestCase):
    """
    Test ElementImage class.
    """
    def test_inscribed_circle(self):
        """
        Test lazy property inscribed_circle.
        """
        self.assertIsNotNone(ElementImage.inscribed_circle.__doc__)

    def test_elements(self):
        """
        Test lazy property elements.
        """
        self.assertIsNotNone(ElementImage.inscribed_circle.__doc__)

if __name__ == '__main__':
    # run unittest TestElementImage
    unittest.main()

