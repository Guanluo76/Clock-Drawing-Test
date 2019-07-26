from __future__ import absolute_import

import numpy as np
import cv2 as cv

from apps.app import App
from utils.metas.meta_singleton import MetaSingleton
from utils.subscribe_methods import subscribe_methods
from settings import config


class Circularity(App, metaclass=MetaSingleton):
    """
    The class to test if the shape in img is circular or not.
    """
    @subscribe_methods
    def methods(self):
        pass

    @methods.add_method
    def _inscribed_circle_mtd(self, clock_face):
        """
        Compute and return the circularity of the shape with inscribed circle
        area method.

        Formula: area_of_inscribed_circle / area

        @param ClockFace clock_face: clock face of the image
               ElementMixin element: useless here
        @return bool True for being circular
        """
        radius = clock_face.inscribed_circle.radius
        area = clock_face.area

        # area of the inscribed circle
        # Formula: pi * radius ^ 2
        inscribed_circle_area = np.pi * radius * radius

        # calculate and return the circularity
        return (inscribed_circle_area / area) > \
               type(self)._CIRCULARITY_THRESH_VAL

    @methods.add_method
    def _perimeter_area_mtd(self, clock_face):
        """
        Compute and return the circularity of the shape with perimeter-area
        method.

        Formula: (4 * pi * area) / perimeter ^ 2

        @param ClockFace clock_face: clock face of the image
               ElementMixin element: useless here
        @return bool True for being circular
        """
        perimeter = cv.arcLength(clock_face.main_contour, True)
        area = clock_face.area

        # calculate and return circularity
        return ((4 * np.pi * area) / (perimeter * perimeter)) > \
               type(self)._CIRCULARITY_THRESH_VAL

config(Circularity)


import unittest


class TestCircularity(unittest.TestCase):
    """
    Test Circularity class.
    """
    def test_inscribed_circle_mtd(self):
        """
        Test _inscribed_circle_mtd method with a square and a perfect circle.
        """
        from utils.create_imgs import create_square, create_circle
        from models.clock_face import ClockFace
        from models.model_mixins.image_mixin import ImageMixin

        self.assertIsNotNone(Circularity()._inscribed_circle_mtd.__doc__)

        # square case
        square_circularity = Circularity()._inscribed_circle_mtd(
                            type('_TestClockFace1', (ClockFace, ),
                                {}, mixins=(ImageMixin, ))(create_square()))
        self.assertEqual(square_circularity, False)

        # circle case
        circle_circularity = Circularity()._inscribed_circle_mtd(
                            type('_TestClockFace2', (ClockFace, ),
                                {}, mixins=(ImageMixin, ))(create_circle()))
        self.assertEqual(circle_circularity, True)

    def test_perimeter_area_mtd(self):
        """
        Test _perimeter_area_mtd method with a suqare and a perfect circle.
        """
        from utils.create_imgs import create_square, create_circle
        from models.model_mixins.image_mixin import ImageMixin
        from models.clock_face import ClockFace

        self.assertIsNotNone(Circularity()._perimeter_area_mtd.__doc__)

        # square case
        square_circularity = Circularity()._perimeter_area_mtd(
                    type('_TestClockFace1', (ClockFace, ),
                        {}, mixins=(ImageMixin, ))(create_square()))
        self.assertEqual(square_circularity, False)

        # circle case
        circle_circularity = Circularity()._perimeter_area_mtd(
                    type('_TestClockFace2', (ClockFace, ),
                        {}, mixins=(ImageMixin, ))(create_circle()))
        self.assertEqual(circle_circularity, True)

    def test_call(self):
        """
        Test __call__ method.
        """
        from utils.create_imgs import create_square, create_circle
        from models.clock_face import ClockFace
        from models.model_mixins.image_mixin import ImageMixin

        self.assertIsNotNone(Circularity().__call__.__doc__)

        # use square for test
        self.assertFalse(Circularity()(
            type('_TestClockFace1', (ClockFace, ), {}, mixins=(ImageMixin, ))(
                                    create_square())))
        self.assertTrue(Circularity()(
            type('_TestClockFace2', (ClockFace, ), {}, mixins=(ImageMixin, ))(
                                    create_circle())))


if __name__ == '__main__':
    unittest.main()

