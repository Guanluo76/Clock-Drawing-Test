from __future__ import absolute_import
from functools import reduce

import numpy as np
import cv2 as cv

from utils.metas.meta_singleton_mixin import MetaSingletonMixin
from models.model_mixins.image_mixin import ImageMixin
from models.circle import Circle
from utils.lazy_property import lazy_property, multi_lazy_properties


class ClockFace(metaclass=MetaSingletonMixin, mixins=(ImageMixin, )):
    """
    The clock face.
    """
    def __init__(self, raw_img):
        self._raw_img = raw_img

    @lazy_property
    def img(self):
        """
        Evaluation method of lazy property img.

        @return ndarray img preprocessed
        """
        return self._preprocess(self._raw_img,
                                binarization=True,
                                opening=False,
                                closing=False)

    @multi_lazy_properties('longest_contour')
    def longest_contour(self):
        pass

    @longest_contour.add
    def main_contour(self):
        pass

    @longest_contour.add
    def area(self):
        pass

    @longest_contour.function
    def _get_contours_and_area(self):
        """
        Evaluation method for lazy properties longest_contour, main_contour,
        and area.

        1. Longest contour: the longest contour in the clock face.
        2. Main contour: the contour with largest area, i.e. main contour of the
                         shape.
        3. Area: the area of main contour, i.e. area of main contour.

        @return tuple (longest_contour, main_contour, area)
        """
        # get contours and hierachy info
        contours, hierachy = self._find_clean_contours(self.img)

        # zip contours and hierachy together
        contours_info = list(zip(contours[1:], hierachy[0][1:]))

        # build iterator for reduce operation
        # longest_contour, main_contour, area
        contours_info = [ (contours[0], contours[0],
                           cv.contourArea(contours[0])) ] + contours_info

        # compute and return
        return reduce(lambda res, nxt: (nxt[0] if cv.arcLength(nxt[0], True) > \
                                        cv.arcLength(res[0], True) \
                                        else res[0], # longest_contour
                                        nxt[0] if cv.contourArea(nxt[0]) > \
                                        cv.contourArea(res[1]) else res[1],
                                        # main_contour
                                        cv.contourArea(nxt[0]) if \
                                        cv.contourArea(nxt[0]) > res[2] else \
                                        res[2]), # area
                                        contours_info)

    @lazy_property
    def inscribed_circle(self):
        """
        Evaluation method for lazy property inscribed circle. Find the
        inscribed circle of the shape in img, its center and radius.

        Method: 1. using distance transform to get the distance from each inside
                   pixel to the given contour.
                2. find the largest distance in the collection (i.e. radius).
                3. find the location of largest distance (i.e. center).

        @return Circle inscribed circle
        """
        # create a mask with the given contour for distance transform
        mask = np.zeros(self.img.shape[0:2], dtype=self.img.dtype)
        cv.drawContours(mask, [ self.main_contour ], 0, (255, 0, 0), cv.FILLED)

        # distance transform
        distance_collection = cv.distanceTransform(mask, cv.DIST_L2, 5,
                                                   cv.DIST_LABEL_PIXEL)

        # get radius
        _, radius, _, center = cv.minMaxLoc(distance_collection)

        return Circle(self.img, center, radius)


import unittest


class TestClockFace(unittest.TestCase):
    """
    Test ClockFace class.
    """
    # defines test ClockFace class for unittest
    _TestClockFace = type('_TestClockFace', (ClockFace, ), {},
                          mixins=(ImageMixin, ))

    def test_get_contours_and_area(self):
        """
        Test _get_contours_and_area method with a square.
        """
        from utils.create_imgs import create_square

        self.assertIsNotNone(ClockFace._get_contours_and_area.__doc__)

        # square, side 50
        # perimeter 200, area 2500
        square_clock_face =  type(self)._TestClockFace(create_square())
        square_longest_contour, square_main_contour, square_area = \
                                square_clock_face._get_contours_and_area()

        self.assertAlmostEqual(cv.arcLength(square_longest_contour, True), 200)
        self.assertAlmostEqual(cv.arcLength(square_main_contour, True), 200)
        self.assertAlmostEqual(square_area, 2500)

    def test_inscribed_circle(self):
        """
        Test evaluation method for inscribed_circle with a square.
        """
        from utils.create_imgs import create_square

        self.assertIsNotNone(ClockFace.inscribed_circle.__doc__)

        # square, side 50
        # i.e. inscribed circle has radius 25
        square_image = type(self)._TestClockFace(create_square())

        # test center and radius
        self.assertEqual(square_image.inscribed_circle.center, (50, 50))
        self.assertAlmostEqual(square_image.inscribed_circle.radius, 25, -1)


if __name__ == '__main__':
    # run unittest TestClockFace
    unittest.main()

