"""
The element module. Defines the parent class of all elements.
"""

from functools import reduce

class Element():
    """
    The parent class for all elements. All elements should have a
    properness_tests method decorated by @subscribe_methods, and add other
    element methods with decorator @properness_tests.add_method.
    """
    def __init__(self, contour):
        self._contour = contour

    def angle(self):
        """
        Angle of the outer rectangle.
        """
        raise NotImplementedError

    def center(self):
        """
        Center of the element.
        """
        raise NotImplementedError

    def box_points(self):
        """
        Vertices of the outer rectangle.
        """
        raise NotImplementedError

    def __call__(self, circle):
        """
        Run all the properness tests and return the result.

        @param Circle circle: inscribed circle of clock face
        @return True if passed
        """
        return reduce(lambda res, test: res and test(self, circle),
                      [ True ] + self.properness_tests)


import unittest


class TestElement(unittest.TestCase):
    def test_angle(self):
        """
        Test angle.
        """
        self.assertIsNotNone(Element.angle.__doc__)

    def test_center(self):
        """
        Test midpoint.
        """
        self.assertIsNotNone(Element.center.__doc__)

    def test_box_points(self):
        """
        Test is_proper.
        """
        self.assertIsNotNone(Element.box_points.__doc__)


if __name__ == '__main__':
    # run unittest TestElement
    unittest.main()


