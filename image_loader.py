"""
The image_loader module. Fetch and read the image for tests.
"""

from __future__ import absolute_import

import cv2 as cv

from utils.meta_singleton import MetaSingleton
from image_generator import subscribe_image_generator


class ImageFetcher(metaclass=MetaSingleton):
    """
    The image fetcher. Apply the consumer mode and maintain a image name queue
    for producer and consumer.
    """
    def __init__(self, img_filename=None):
        self._img_name_list = []

    @property
    def img_filename(self):
        """
        Getter for property img_filename. Pop the next filename in the queue.

        @return string filename
        """
        return self._img_name_list.pop(0) if len(self._img_name_list) > 0 \
               else None

    @img_filename.setter
    def img_filename(self, val):
        """
        Setter for property img_filename. Add the given filename to the queue.

        @param string val: filename
        """
        if val:
            self._img_name_list.append(val)

    def next_img(self):
        """
        Return the next image in the image queue. The proxy for consumer.

        @return ndarray image
        """
        while len(self._img_name_list):
            yield self.img_filename


@subscribe_image_generator
def image_loader():
    """
    Get image names from ImageFetcher and return the loaded image.
    i.e. the consumer of image name queue.

    @return ndarray image
    """
    for image_filename in ImageFetcher().next_img():
        yield cv.imread(image_filename)


import unittest


class TestImageLoader(unittest.TestCase):
    """
    Test ImageFetcher and image_loader.
    """
    def test_image_fetcher(self):
        """
        Test ImageFetcher.
        """
        self.assertIsNotNone(ImageFetcher.img_filename.__doc__)
        self.assertIsNotNone(ImageFetcher.next_img.__doc__)

        image_fetcher = ImageFetcher()

        # add test image names into the queue
        for i in range(3):
            image_fetcher.img_filename = 'test image name %d' % (i + 1)

        # test the names in queue
        [ self.assertEqual(image_fetcher.img_filename,
            'test image name %d' % (i + 1)) for i in range(3) ]


    def test_image_loader(self):
        """
        Test image_loader.
        """
        self.assertIsNotNone(image_loader.__doc__)

        image_fetcher = ImageFetcher()

        # add image names into the queue
        for i in range(3):
            image_fetcher.img_filename = 'imgs/%d.png' % (i + 1)

        # read the names and load the images from queue
        # test if the images are not none
        for img in image_loader():
            self.assertTrue(img.any())


if __name__ == '__main__':
    # run unittest TestImageLoader
    unittest.main()

