"""
The image_generator module. Defines ImageGenerator class and the decorator for
assigning image loader.
"""

from __future__ import absolute_import

from utils.metas.meta_singleton import MetaSingleton
from utils.lazy_property import lazy_property

import cv2 as cv


class ImageGenerator(metaclass=MetaSingleton):
    """
    Generator of images for tests. Also implemented as an decorator for
    subscribing image loader.
    """
    def __init__(self, image_loader):
        # only called when using as decorator
        # i.e. first scan of the code by interpreter to apply decorators
        self.image_loader = image_loader

    @lazy_property
    def img_iterator(self):
        """
        The lazy property img_iterator. Returns a generator for images for each
        step (test).

        @return generator image iterator
        """
        previous_img = None
        for img in self.image_loader():
            # yield the difference with previous image, specific part for
            # current step
            yield img - previous_img if not previous_img is None else img
            previous_img = img

    def __next__(self):
        """
        Get next raw image.

        @return ndarray next raw image
        """
        return next(self.img_iterator)

    def __iter__(self):
        """
        Get iterator with images fetched from self.image_loader.

        image_loader: a generator used for reading images. Subscribed to here
                      by using ImageGenerator class as a decorator. Must take
                      no arguments.

        @return generator generator for iterating images available
        """
        return self.img_iterator


    def __call__(self):
        """
        Call the function wrapped by decorator.
        """
        return self.image_loader()

# alias for decorator
subscribe_image_generator = ImageGenerator


import unittest


@unittest.skip('Skip image generator test to test experiment module. Also '
               'remember to annotate the subscribe_image_generator decorator.')
class TestImageGenerator(unittest.TestCase):
    """
    Test ImageGenerator class.
    """
    # this decorator must be annotated when not testing this module only
    # @subscribe_image_generator
    def _get_val():
        """
        Value generator, helper function for test_image_generator. Simulates
        image loader, implemented as generator and yields one value (image
        read) each time.

        @return int value
        """
        for val in range(4):
            yield val

    def test_image_generator(self):
        """
        Test image_generator. Simualtes consumer of ImageGenerator and operates
        on the values returned (image read).
        """
        from functools import reduce

        # test sum of the values returned, should be 0 + 1 + 1 + 1 = 3
        self.assertEqual(reduce(lambda pre, nxt: pre + nxt, ImageGenerator()),
                         3)


if __name__ == '__main__':
    # run unittest TestImageGenerator
    unittest.main()

