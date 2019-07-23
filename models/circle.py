"""
The circle module. Defines the circle class, mainly used for inscribed circle
of the clock face.
"""

from __future__ import absolute_import
from functools import reduce

import numpy as np
import cv2 as cv

from utils.lazy_property import lazy_property
from settings import config


class Circle():
    """
    The circle class.
    """
    def __init__(self, raw_img, center, radius):
        self.raw_img = raw_img
        self.center = center
        self.radius = radius

    @lazy_property
    def sectors(self):
        """
        Evaluation method for lazy property sectors. Divide the circle into 12
        different sectors and return the list of their contours.

        @return list contours of 12 sectors
        """
        def get_sector_contour(angle):
            """
            Helper function to get contour of a given sector.

            @param int angle: the positional angle of sector
            @return list contour of the sector
            """
            # create a mask to draw sector on
            mask = np.zeros(self.raw_img.shape[:2], dtype=self.raw_img.dtype)

            # draw sector on the mask
            # sector on angle, with central angle (360 / 12) / 2 = 15 to force
            # the later position test to be about in the middle of the sector
            # the actual accepted angle is limited by _RANGE
            cv.ellipse(mask, self.center, (round(self.radius),
                                           round(self.radius)), angle,
                       - 15 * type(self)._RANGE, 15 * type(self)._RANGE, 1, -1)

            # get the sector contour from mask
            return cv.findContours(mask, cv.RETR_EXTERNAL,
                                   cv.CHAIN_APPROX_SIMPLE)[0]

        return reduce(lambda result, angle: result + get_sector_contour(angle),
                      [ [] ] + list(range(-90, 270, 30)))

    def is_in_sector(self, point, sector_no=-1):
        """
        Use pointPolygonTest to see if the given point is inside the specified
        sector (one of the sectors).

        @param tuple point: a given point
               int sector_no: which sector (clockwise order, 0 ~ 11)
                              find all sectors if not specified
        @return True if the point is in the sector (one of the sectors)
        """
        if sector_no < 0:
            return reduce(lambda result, sector: result or \
                                cv.pointPolygonTest(sector, point, False) > 0,
                          [ False ] + self.sectors)
        return cv.pointPolygonTest(self.sectors[sector_no], point, False) > 0

config(Circle)


import unittest


class TestCircle(unittest.TestCase):
    """
    Test Circle class.
    """
    def test_sectors(self):
        """
        Test evaluation method for sectors.
        """
        self.assertIsNotNone(Circle.sectors.__doc__)

        # create a circle with radius 200 on the center of a  500 x 500 image
        circle = Circle(np.zeros((500, 500), dtype='uint8'), (250, 250), 200)
        self.assertEqual(len(circle.sectors), 12)

    def test_is_in_sector(self):
        """
        Test is in sector method.
        """
        self.assertIsNotNone(Circle.is_in_sector.__doc__)

        # create a circle with radius 200 on the center of a  500 x 500 image
        circle = Circle(np.zeros((500, 500), dtype='uint8'), (250, 250), 200)

        # test a point inside first sector
        self.assertTrue(circle.is_in_sector((250, 200), 0))

        # test another point outside first sector
        self.assertFalse(circle.is_in_sector((250, 300), 0))

        # while the same point locates inside the 7th sector
        self.assertTrue(circle.is_in_sector((250, 300), 6))

        # test a point inside one of the sectors
        self.assertTrue(circle.is_in_sector((250, 300)))

        # test a point outside all sectors
        self.assertFalse(circle.is_in_sector((0, 0)))


if __name__ == '__main__':
    unittest.main()

