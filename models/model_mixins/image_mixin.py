"""
The image_mixin module. Defines mixin behaviors for all images.
"""

from __future__ import absolute_import
from functools import reduce

import numpy as np
import cv2 as cv

from utils.mixin_template import Mixin
from utils.lazy_property import lazy_property
from settings import config


class ImageMixin(Mixin):
    """
    The mixin class for image preprocessing.
    """
    def _preprocess(self, raw, **kwargs):
        """
        Collection of preprocessors for image.

        Preprocessors: classmethod which only accepts an ndarray image as input
                       and gives processed image back.

        @param ndarray raw: raw image to be processed
        @param bool kwargs: flags, the preprocessors needed
        @return ndarray preprocessed image
        """
        preprocessors = {
                    'binarization': self._binarize,
                    'opening': self._opening,
                    'closing': self._closing,
                }

        return reduce(lambda img, key: preprocessors[key](img)
                                   if key in kwargs and kwargs[key] else img,
                      [ raw ] + list(preprocessors.keys()))

    def _binarize(self, img):
        """
        Binarization processor.

        @param ndarray img: image to be processed
        @return ndarray binarized image
        """
        # turn img into grayscale
        img = img if len(img.shape) < 3 else \
                     cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # binarization
        _, binarized_img = cv.threshold(img, self._BINARIZATION_THRESH_VAL,
                                        255, cv.THRESH_BINARY)
        return binarized_img

    def _opening(self, img):
        """
        Opening processor. Erosion followed by dilation. For removing noise.

        @param ndarray img: image to be processed
        @return ndarray image after opening transformation
        """
        return cv.morphologyEx(img, cv.MORPH_OPEN, self._OPENING_KERNEL)

    def _closing(self, img):
        """
        Closing processor. Dilation followed by erosion. For closing small
        holes in foreground objects.

        @param ndarray img: image to be processed
        @return ndarray image after opening transformation
        """
        return cv.morphologyEx(img, cv.MORPH_CLOSE, self._CLOSING_KERNEL)

    def _find_clean_contours(self, img, mode=cv.RETR_TREE,
                             method=cv.CHAIN_APPROX_SIMPLE):
        """
        Discard the inessential contours that has area smaller than threshold
        value, and return the rest.

        @param ndarray img: image to be processed
        @return tuple (contours[], hierachy[]) contours and hierachy filtered
        """
        contours, hierachy = cv.findContours(img, mode, method)

        contours_info = list(zip(contours, hierachy[0]))
        clean_contours_info = list(filter(lambda contour_info: \
                                        cv.contourArea(contour_info[0]) > \
                                        self._MIN_CONTOUR_AREA, contours_info))

        return map(list, zip(*clean_contours_info))

    @lazy_property
    def img(self):
        """
        The lazy property img. Preprocessed raw image.

        @return ndarray img preprocessed with binarization
        """
        return self._preprocess(self._raw_img,
                                binarization=True,
                                opening=False,
                                closing=False)

config(ImageMixin)


import unittest


class TestImageMixin(unittest.TestCase):
    """
    Test ImageMixin class.
    """
    def test_preprocess(self):
        """
        Test _preprocess method.
        """
        self.assertIsNotNone(ImageMixin._preprocess.__doc__)

    def test_find_clean_contours(self):
        """
        Test _find_clean_contours method.
        """
        self.assertIsNotNone(ImageMixin._find_clean_contours.__doc__)

    def test_binarize(self):
        """
        Test _binarize method.
        """
        self.assertIsNotNone(ImageMixin._binarize.__doc__)

    def test_opening(self):
        """
        Test _opening method.
        """
        self.assertIsNotNone(ImageMixin._opening.__doc__)

    def test_closing(self):
        """
        Test _closing method.
        """
        self.assertIsNotNone(ImageMixin._closing.__doc__)

    def test_img(self):
        """
        Test lazy property img.
        """
        self.assertIsNotNone(ImageMixin.img.__doc__)


if __name__ == '__main__':
    # run unittest TestImageMixin
    unittest.main()

