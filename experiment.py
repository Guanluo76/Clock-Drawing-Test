"""
The experiment module.
"""

from __future__ import absolute_import
from functools import reduce, partial

from utils.metas.meta_singleton import MetaSingleton
from utils.lazy_property import lazy_property
from image_generator import ImageGenerator


class Experiment(metaclass=MetaSingleton):
    """
    The experiment class, representing a CDT tests.
    """
    def __init__(self):
        self.img_generator = ImageGenerator()

    @lazy_property
    def score_tests(self):
        """
        The lazy property score_tests. Return the list of all tests.

        @return list tests
        """
        from models.clock_face import ClockFace
        from models.scale.scale_image import ScaleImage
        from apps.circularity.circularity import Circularity
        from apps.scale.scale import Scale

        # get clock face from the first image
        clock_face = ClockFace(next(self.img_generator))

        # list of the test functions
        return [
                partial(Circularity(), clock_face),
                partial(Scale(),
                    ScaleImage(clock_face, next(self.img_generator))),
            ]

    @lazy_property
    def score(self):
        """
        The lazy property score. Run the tests and store final score of the
        experiment.

        @return int 0 ~ (number of tests) score of the CDT
        """
        # go through all the tests and return the result
        return reduce(lambda pre, nxt: pre + nxt(), [ 0 ] + self.score_tests)


import unittest


# @unittest.skip('Skip experiment test to test image_generator module.')
class TestExperiment(unittest.TestCase):
    """
    Test Experiment class.
    """
    def test_score(self):
        """
        Test scoring with the given images.
        """
        from image_loader import ImageFetcher

        self.assertIsNotNone(Experiment.score.__doc__)

        # read in images
        for i in range(2):
            ImageFetcher().img_filename = 'imgs/%d.png' % (i + 1)

        # run the experiment and test the score
        self.assertEqual(Experiment().score, 2)


if __name__ == '__main__':
    # run unittest TestExperiment
    unittest.main()

