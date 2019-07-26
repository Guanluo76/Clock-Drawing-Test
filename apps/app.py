"""
The app module. Defines template parent class for all apps.
"""

from functools import reduce


class App():
    """
    The parent class for all apps. All apps should have a methods method
    decorated by @subscribe_methods, and add other app methods with
    decorator @methods.add_method.
    """
    def __call__(self, element_img):
        """
        Run the app.

        @param ClockFace / ElementImageMixin element_img: image to be processed
        @return True if passed
        """
        return reduce(lambda res, mtd: res and mtd(self, element_img),
                      [ True ] + self.methods)

