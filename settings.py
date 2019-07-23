"""
The settings module. Saving constants for classes and config them.
"""

from __future__ import absolute_import

import numpy as np
import cv2 as cv


settings = {
            'Circularity': {
                    # the threshold value for circularity
                    '_CIRCULARITY_THRESH_VAL': 0.85,
                },

            'ImageMixin': {
                    # threshold value for binarization
                    '_BINARIZATION_THRESH_VAL': 200,

                    # minimum area acceptable for a contour
                    # any contour with area smaller than this value would be
                    # discarded
                    '_MIN_CONTOUR_AREA': 50,

                    # kernel for opening transformation
                    '_OPENING_KERNEL': \
                        cv.getStructuringElement(cv.MORPH_ELLIPSE, (20, 20)),

                    # kernel for closing transformation
                    '_CLOSING_KERNEL': \
                        cv.getStructuringElement(cv.MORPH_ELLIPSE, (40, 40)),
                },

            'Circle': {
                    # range accepted in a sector for proper position
                    # 0 ~ 1
                    '_RANGE': 0.5,
                },

            'ScaleElement': {
                    # minimum number of proper points inside the sector
                    '_MIN_FIT_POINTS': 2,
                },

            'ScaleImageMixin': {
                    # starting radian of the first sector (i.e. 12 o'clock)
                    '_START_RAD': -15 * 0.5 * (np.pi / 180),
                },
        }

def config(caller):
    """
    Assign class constants to the caller class from the settings dict.

    @param type caller: the caller class
    """
    # get the constants for the caller class
    class_config = settings[caller.__name__]

    # set all the class constants with setattr
    [ setattr(caller, attr_name, class_config[attr_name])
            for attr_name in class_config.keys() ]


import unittest


class TestSettings(unittest.TestCase):
    """
    Test config function and settings.
    """
    def test_config(self):
        """
        Test config function.
        """
        self.assertIsNotNone(config.__doc__)

        # set a class constant for this test class
        settings['TestSettings'] = dict(test_val='test')

        # config this class
        config(TestSettings)
        self.assertEqual(type(self).test_val, 'test')


if __name__ == '__main__':
    # run unittest TestSettings
    unittest.main()

